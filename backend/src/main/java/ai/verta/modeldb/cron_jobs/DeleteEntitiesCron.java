package ai.verta.modeldb.cron_jobs;

import ai.verta.modeldb.DatasetVisibilityEnum;
import ai.verta.modeldb.ModelDBConstants;
import ai.verta.modeldb.ProjectVisibility;
import ai.verta.modeldb.WorkspaceTypeEnum;
import ai.verta.modeldb.authservice.AuthService;
import ai.verta.modeldb.authservice.RoleService;
import ai.verta.modeldb.collaborator.CollaboratorOrg;
import ai.verta.modeldb.entities.CommentEntity;
import ai.verta.modeldb.entities.DatasetEntity;
import ai.verta.modeldb.entities.DatasetVersionEntity;
import ai.verta.modeldb.entities.ExperimentEntity;
import ai.verta.modeldb.entities.ExperimentRunEntity;
import ai.verta.modeldb.entities.ProjectEntity;
import ai.verta.modeldb.entities.versioning.BranchEntity;
import ai.verta.modeldb.entities.versioning.CommitEntity;
import ai.verta.modeldb.entities.versioning.RepositoryEntity;
import ai.verta.modeldb.utils.ModelDBHibernateUtil;
import ai.verta.uac.ModelResourceEnum;
import ai.verta.uac.UserInfo;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.TimerTask;
import java.util.stream.Collectors;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.query.Query;

public class DeleteEntitiesCron extends TimerTask {
  private static final Logger LOGGER = LogManager.getLogger(DeleteEntitiesCron.class);
  private final AuthService authService;
  private final RoleService roleService;
  private static final String DATASET_GLOBAL_SHARING = "_DATASET_GLOBAL_SHARING";
  private static final String REPOSITORY_GLOBAL_SHARING = "_REPO_GLOBAL_SHARING";

  public DeleteEntitiesCron(AuthService authService, RoleService roleService) {
    this.authService = authService;
    this.roleService = roleService;
  }

  /** The action to be performed by this timer task. */
  @Override
  public void run() {
    LOGGER.info("DeleteEntitiesCron wakeup");

    try (Session session = ModelDBHibernateUtil.getSessionFactory().openSession()) {
      // Update project timestamp
      deleteProjects(session);

      // Update experiment timestamp
      deleteExperiments(session);

      // Update experimentRun timestamp
      deleteExperimentRuns(session);

      // Update dataset timestamp
      deleteDatasets(session);

      // Update datasetVersion timestamp
      deleteDatasetVersions(session);

      // Update repository timestamp
      deleteRepositories(session);
    } catch (Exception ex) {
      LOGGER.error("DeleteEntitiesCron Exception: ", ex);
    }

    LOGGER.info("DeleteEntitiesCron finish tasks and reschedule");
  }

  private void deleteProjects(Session session) {
    LOGGER.debug("Project deleting");
    String alias = "pr";
    String deleteProjectsQueryString =
        new StringBuilder("FROM ")
            .append(ProjectEntity.class.getSimpleName())
            .append(" ")
            .append(alias)
            .append(" WHERE ")
            .append(alias)
            .append(".")
            .append(ModelDBConstants.DELETED)
            .append(" = :deleted ")
            .toString();

    int lowerBound = 0;
    final int pagesize = 500;
    Query countQuery =
        session.createQuery("SELECT COUNT(" + alias + ") " + deleteProjectsQueryString);
    countQuery.setParameter("deleted", true);
    Long count = (Long) countQuery.uniqueResult();
    LOGGER.debug("Total projectEntities {} for deletion", count);

    while (lowerBound < count) {
      List<String> roleBindingNames = new LinkedList<>();
      Transaction transaction = session.beginTransaction();

      Query projectDeleteQuery = session.createQuery(deleteProjectsQueryString);
      projectDeleteQuery.setParameter("deleted", true);
      projectDeleteQuery.setFirstResult(lowerBound);
      projectDeleteQuery.setMaxResults(pagesize);
      LOGGER.debug("Project delete query: {}", projectDeleteQuery.getQueryString());
      List<ProjectEntity> projectEntities = projectDeleteQuery.list();

      List<String> projectIds = new ArrayList<>();
      for (ProjectEntity projectEntity : projectEntities) {
        projectIds.add(projectEntity.getId());
        session.delete(projectEntity);
      }

      String updateDeletedStatusExperimentQueryString =
          new StringBuilder("UPDATE ")
              .append(ExperimentEntity.class.getSimpleName())
              .append(" exp ")
              .append("SET exp.")
              .append(ModelDBConstants.DELETED)
              .append(" = :deleted ")
              .append(" WHERE exp.")
              .append(ModelDBConstants.PROJECT_ID)
              .append(" IN (:projectIds)")
              .toString();
      Query deletedExperimentQuery = session.createQuery(updateDeletedStatusExperimentQueryString);
      deletedExperimentQuery.setParameter("deleted", true);
      deletedExperimentQuery.setParameter("projectIds", projectIds);
      deletedExperimentQuery.executeUpdate();

      String updateDeletedStatusExperimentRunQueryString =
          new StringBuilder("UPDATE ")
              .append(ExperimentRunEntity.class.getSimpleName())
              .append(" expr ")
              .append("SET expr.")
              .append(ModelDBConstants.DELETED)
              .append(" = :deleted ")
              .append(" WHERE expr.")
              .append(ModelDBConstants.PROJECT_ID)
              .append(" IN (:projectIds)")
              .toString();
      Query deletedExperimentRunQuery =
          session.createQuery(updateDeletedStatusExperimentRunQueryString);
      deletedExperimentRunQuery.setParameter("deleted", true);
      deletedExperimentRunQuery.setParameter("projectIds", projectIds);
      deletedExperimentRunQuery.executeUpdate();

      transaction.commit();

      // Get roleBindings by accessible projects
      getRoleBindingsOfAccessibleProjects(projectEntities, roleBindingNames);
      LOGGER.debug("num bindings after Projects {}", roleBindingNames.size());

      // Remove all role bindings
      if (!roleBindingNames.isEmpty()) {
        roleService.deleteRoleBindings(roleBindingNames);
      }
      lowerBound += pagesize;
    }
    LOGGER.debug("Project Deleted successfully : Deleted projects count {}", count);
  }

  private void getRoleBindingsOfAccessibleProjects(
      List<ProjectEntity> allowedProjects, List<String> roleBindingNames) {
    UserInfo unsignedUser = authService.getUnsignedUser();
    for (ProjectEntity project : allowedProjects) {
      String projectId = project.getId();

      if (project.getProject_visibility() == ProjectVisibility.PUBLIC.getNumber()) {
        String publicReadRoleBindingName =
            roleService.buildRoleBindingName(
                ModelDBConstants.ROLE_PROJECT_PUBLIC_READ,
                projectId,
                authService.getVertaIdFromUserInfo(unsignedUser),
                ModelResourceEnum.ModelDBServiceResourceTypes.PROJECT.name());
        if (publicReadRoleBindingName != null) {
          roleBindingNames.add(publicReadRoleBindingName);
        }
      }

      // Delete workspace based roleBindings
      List<String> workspaceRoleBindingNames =
          roleService.getWorkspaceRoleBindings(
              project.getWorkspace(),
              WorkspaceTypeEnum.WorkspaceType.forNumber(project.getWorkspace_type()),
              projectId,
              ModelDBConstants.ROLE_PROJECT_ADMIN,
              ModelResourceEnum.ModelDBServiceResourceTypes.PROJECT,
              ProjectVisibility.forNumber(project.getProject_visibility())
                  .equals(ProjectVisibility.ORG_SCOPED_PUBLIC),
              "_GLOBAL_SHARING");
      roleBindingNames.addAll(workspaceRoleBindingNames);
    }

    roleService.deleteAllResources(
        allowedProjects.stream().map(ProjectEntity::getId).collect(Collectors.toList()),
        ModelResourceEnum.ModelDBServiceResourceTypes.PROJECT);
  }

  private void deleteExperiments(Session session) {
    LOGGER.debug("Experiment deleting");
    String deleteExperimentQueryString =
        new StringBuilder("FROM ")
            .append(ExperimentEntity.class.getSimpleName())
            .append(" ex WHERE ex.")
            .append(ModelDBConstants.DELETED)
            .append(" = :deleted ")
            .toString();

    int lowerBound = 0;
    final int pagesize = 500;
    Query countQuery = session.createQuery("SELECT COUNT(ex) " + deleteExperimentQueryString);
    countQuery.setParameter("deleted", true);
    Long count = (Long) countQuery.uniqueResult();
    LOGGER.debug("Total experimentEntities {} for deletion", count);

    while (lowerBound < count) {
      List<String> roleBindingNames = new LinkedList<>();
      Transaction transaction = session.beginTransaction();

      Query experimentDeleteQuery = session.createQuery(deleteExperimentQueryString);
      experimentDeleteQuery.setParameter("deleted", true);
      experimentDeleteQuery.setFirstResult(lowerBound);
      experimentDeleteQuery.setMaxResults(pagesize);
      LOGGER.debug("Experiment delete query: {}", experimentDeleteQuery.getQueryString());
      List<ExperimentEntity> experimentEntities = experimentDeleteQuery.list();
      List<String> experimentIds = new ArrayList<>();
      for (ExperimentEntity experimentEntity : experimentEntities) {
        experimentIds.add(experimentEntity.getId());
        session.delete(experimentEntity);

        String ownerRoleBindingName =
            roleService.buildRoleBindingName(
                ModelDBConstants.ROLE_EXPERIMENT_OWNER,
                experimentEntity.getId(),
                experimentEntity.getOwner(),
                ModelResourceEnum.ModelDBServiceResourceTypes.EXPERIMENT.name());
        if (ownerRoleBindingName != null) {
          roleBindingNames.add(ownerRoleBindingName);
        }
      }

      String updateDeletedStatusExperimentRunQueryString =
          new StringBuilder("UPDATE ")
              .append(ExperimentRunEntity.class.getSimpleName())
              .append(" expr ")
              .append("SET expr.")
              .append(ModelDBConstants.DELETED)
              .append(" = :deleted ")
              .append(" WHERE expr.")
              .append(ModelDBConstants.EXPERIMENT_ID)
              .append(" IN (:experimentIds)")
              .toString();
      Query deletedExperimentRunQuery =
          session.createQuery(updateDeletedStatusExperimentRunQueryString);
      deletedExperimentRunQuery.setParameter("deleted", true);
      deletedExperimentRunQuery.setParameter("experimentIds", experimentIds);
      deletedExperimentRunQuery.executeUpdate();

      if (!roleBindingNames.isEmpty()) {
        roleService.deleteRoleBindings(roleBindingNames);
      }
      transaction.commit();
      lowerBound += pagesize;
    }

    LOGGER.debug("Experiment deleted successfully : Deleted experiments count {}", count);
  }

  private void deleteExperimentRuns(Session session) {
    LOGGER.debug("ExperimentRun deleting");
    String deleteExperimentRunQueryString =
        new StringBuilder("FROM ")
            .append(ExperimentRunEntity.class.getSimpleName())
            .append(" expr WHERE expr.")
            .append(ModelDBConstants.DELETED)
            .append(" = :deleted ")
            .toString();

    int lowerBound = 0;
    final int pagesize = 500;
    Query countQuery = session.createQuery("SELECT COUNT(expr) " + deleteExperimentRunQueryString);
    countQuery.setParameter("deleted", true);
    Long count = (Long) countQuery.uniqueResult();
    LOGGER.debug("Total experimentRunEntities {} for deletion", count);

    while (lowerBound < count) {
      List<String> roleBindingNames = new LinkedList<>();
      Transaction transaction = session.beginTransaction();

      Query experimentRunDeleteQuery = session.createQuery(deleteExperimentRunQueryString);
      experimentRunDeleteQuery.setParameter("deleted", true);
      experimentRunDeleteQuery.setFirstResult(lowerBound);
      experimentRunDeleteQuery.setMaxResults(pagesize);
      LOGGER.debug("ExperimentRun delete query: {}", experimentRunDeleteQuery.getQueryString());
      List<ExperimentRunEntity> experimentRunEntities = experimentRunDeleteQuery.list();
      List<String> experimentRunIds = new ArrayList<>();
      for (ExperimentRunEntity experimentRunEntity : experimentRunEntities) {
        experimentRunIds.add(experimentRunEntity.getId());
        session.delete(experimentRunEntity);

        String ownerRoleBindingName =
            roleService.buildRoleBindingName(
                ModelDBConstants.ROLE_EXPERIMENT_RUN_OWNER,
                experimentRunEntity.getId(),
                experimentRunEntity.getOwner(),
                ModelResourceEnum.ModelDBServiceResourceTypes.EXPERIMENT_RUN.name());
        if (ownerRoleBindingName != null) {
          roleBindingNames.add(ownerRoleBindingName);
        }
      }
      // Delete the ExperimentRun comments
      if (!experimentRunIds.isEmpty()) {
        removeEntityComments(session, experimentRunIds, ExperimentRunEntity.class.getSimpleName());
      }
      if (!roleBindingNames.isEmpty()) {
        roleService.deleteRoleBindings(roleBindingNames);
      }
      transaction.commit();
      lowerBound += pagesize;
    }

    LOGGER.debug("ExperimentRun deleted successfully : Deleted experimentRuns count {}", count);
  }

  private void removeEntityComments(Session session, List<String> entityIds, String entityName) {
    String commentDeleteHql =
        new StringBuilder()
            .append("From CommentEntity ce where ce.")
            .append(ModelDBConstants.ENTITY_ID)
            .append(" IN (:entityIds) AND ce.")
            .append(ModelDBConstants.ENTITY_NAME)
            .append(" =:entityName")
            .toString();
    Query commentDeleteQuery = session.createQuery(commentDeleteHql);
    commentDeleteQuery.setParameterList("entityIds", entityIds);
    commentDeleteQuery.setParameter("entityName", entityName);
    LOGGER.debug("Comments delete query : {}", commentDeleteQuery.getQueryString());
    List<CommentEntity> commentEntities = commentDeleteQuery.list();
    for (CommentEntity commentEntity : commentEntities) {
      session.delete(commentEntity);
    }
  }

  private void deleteDatasets(Session session) {
    LOGGER.debug("Dataset deleting");
    String alias = "dt";
    String deleteDatasetsQueryString =
        new StringBuilder("FROM ")
            .append(DatasetEntity.class.getSimpleName())
            .append(" ")
            .append(alias)
            .append(" WHERE ")
            .append(alias)
            .append(".")
            .append(ModelDBConstants.DELETED)
            .append(" = :deleted ")
            .toString();

    int lowerBound = 0;
    final int pagesize = 500;
    Query countQuery =
        session.createQuery("SELECT COUNT(" + alias + ") " + deleteDatasetsQueryString);
    countQuery.setParameter("deleted", true);
    Long count = (Long) countQuery.uniqueResult();
    LOGGER.debug("Total datasetEntities {} for deletion", count);

    while (lowerBound < count) {
      Transaction transaction = session.beginTransaction();

      Query datasetDeleteQuery = session.createQuery(deleteDatasetsQueryString);
      datasetDeleteQuery.setParameter("deleted", true);
      datasetDeleteQuery.setFirstResult(lowerBound);
      datasetDeleteQuery.setMaxResults(pagesize);
      LOGGER.debug("Dataset delete query: {}", datasetDeleteQuery.getQueryString());
      List<DatasetEntity> datasetEntities = datasetDeleteQuery.list();

      List<String> datasetIds = new ArrayList<>();
      for (DatasetEntity datasetEntity : datasetEntities) {
        datasetIds.add(datasetEntity.getId());
        session.delete(datasetEntity);
      }

      String updateDeletedStatusDatasetVersionQueryString =
          new StringBuilder("UPDATE ")
              .append(DatasetVersionEntity.class.getSimpleName())
              .append(" dv ")
              .append("SET dv.")
              .append(ModelDBConstants.DELETED)
              .append(" = :deleted ")
              .append(" WHERE dv.")
              .append(ModelDBConstants.DATASET_ID)
              .append(" IN (:datasetIds)")
              .toString();
      Query deletedDatasetVersionQuery =
          session.createQuery(updateDeletedStatusDatasetVersionQueryString);
      deletedDatasetVersionQuery.setParameter("deleted", true);
      deletedDatasetVersionQuery.setParameter("datasetIds", datasetIds);
      deletedDatasetVersionQuery.executeUpdate();

      transaction.commit();

      // Remove roleBindings by accessible datasets
      List<String> roleBindingNames = new LinkedList<>();
      deleteRoleBindingsOfAccessibleDatasets(datasetEntities, roleBindingNames);
      LOGGER.debug("num bindings after Datasets {}", roleBindingNames.size());

      // Remove all role bindings
      if (!roleBindingNames.isEmpty()) {
        roleService.deleteRoleBindings(roleBindingNames);
      }
      lowerBound += pagesize;
    }
    LOGGER.debug("Dataset Deleted successfully : Deleted datasets count {}", count);
  }

  private void deleteRoleBindingsOfAccessibleDatasets(
      List<DatasetEntity> allowedDatasets, List<String> roleBindingNames) {
    UserInfo unsignedUser = authService.getUnsignedUser();
    for (DatasetEntity datasetEntity : allowedDatasets) {
      String datasetId = datasetEntity.getId();

      if (datasetEntity.getDataset_visibility()
          == DatasetVisibilityEnum.DatasetVisibility.PUBLIC.getNumber()) {
        String publicReadRoleBindingName =
            roleService.buildRoleBindingName(
                ModelDBConstants.ROLE_DATASET_PUBLIC_READ,
                datasetId,
                authService.getVertaIdFromUserInfo(unsignedUser),
                ModelResourceEnum.ModelDBServiceResourceTypes.DATASET.name());
        if (publicReadRoleBindingName != null && !publicReadRoleBindingName.isEmpty()) {
          roleBindingNames.add(publicReadRoleBindingName);
        }
      }

      // Delete workspace based roleBindings
      List<String> workspaceRoleBindingNames =
          getWorkspaceRoleBindingsForDataset(
              datasetEntity.getWorkspace(),
              WorkspaceTypeEnum.WorkspaceType.forNumber(datasetEntity.getWorkspace_type()),
              datasetEntity.getId(),
              DatasetVisibilityEnum.DatasetVisibility.forNumber(
                  datasetEntity.getDataset_visibility()));
      if (!workspaceRoleBindingNames.isEmpty()) {
        roleBindingNames.addAll(workspaceRoleBindingNames);
      }
    }

    // Remove all datasetEntity collaborators
    roleService.deleteAllResources(
        allowedDatasets.stream().map(DatasetEntity::getId).collect(Collectors.toList()),
        ModelResourceEnum.ModelDBServiceResourceTypes.DATASET);
  }

  private List<String> getWorkspaceRoleBindingsForDataset(
      String workspaceId,
      WorkspaceTypeEnum.WorkspaceType workspaceType,
      String datasetId,
      DatasetVisibilityEnum.DatasetVisibility datasetVisibility) {
    List<String> workspaceRoleBindings = new ArrayList<>();
    if (workspaceId != null && !workspaceId.isEmpty()) {
      switch (workspaceType) {
        case ORGANIZATION:
          if (datasetVisibility.equals(DatasetVisibilityEnum.DatasetVisibility.ORG_SCOPED_PUBLIC)) {
            String orgDatasetReadRoleBindingName =
                roleService.buildRoleBindingName(
                    ModelDBConstants.ROLE_DATASET_READ_ONLY,
                    datasetId,
                    new CollaboratorOrg(workspaceId),
                    ModelResourceEnum.ModelDBServiceResourceTypes.DATASET.name());
            if (orgDatasetReadRoleBindingName != null && !orgDatasetReadRoleBindingName.isEmpty()) {
              workspaceRoleBindings.add(orgDatasetReadRoleBindingName);
            }
          }
          break;
        case USER:
        default:
          break;
      }
    }
    List<String> orgWorkspaceRoleBindings =
        roleService.getWorkspaceRoleBindings(
            workspaceId,
            workspaceType,
            datasetId,
            ModelDBConstants.ROLE_DATASET_ADMIN,
            ModelResourceEnum.ModelDBServiceResourceTypes.DATASET,
            datasetVisibility.equals(DatasetVisibilityEnum.DatasetVisibility.ORG_SCOPED_PUBLIC),
            DATASET_GLOBAL_SHARING);

    if (orgWorkspaceRoleBindings != null && !orgWorkspaceRoleBindings.isEmpty()) {
      workspaceRoleBindings.addAll(orgWorkspaceRoleBindings);
    }
    return workspaceRoleBindings;
  }

  private void deleteDatasetVersions(Session session) {
    LOGGER.debug("DatasetVersion deleting");
    String alias = "dv";
    String deleteDatasetVersionsQueryString =
        new StringBuilder("FROM ")
            .append(DatasetVersionEntity.class.getSimpleName())
            .append(" ")
            .append(alias)
            .append(" WHERE ")
            .append(alias)
            .append(".")
            .append(ModelDBConstants.DELETED)
            .append(" = :deleted ")
            .toString();
    Query datasetVersionDeleteQuery = session.createQuery(deleteDatasetVersionsQueryString);
    datasetVersionDeleteQuery.setParameter("deleted", true);
    LOGGER.debug("DatasetVersion delete query: {}", datasetVersionDeleteQuery.getQueryString());

    Transaction transaction = session.beginTransaction();
    List<DatasetVersionEntity> datasetVersionEntities = datasetVersionDeleteQuery.list();

    // Remove roleBindings by accessible datasetVersions
    List<String> roleBindingNames = new LinkedList<>();
    for (DatasetVersionEntity datasetVersionEntity : datasetVersionEntities) {
      session.delete(datasetVersionEntity);

      String ownerRoleBindingName =
          roleService.buildRoleBindingName(
              ModelDBConstants.ROLE_DATASET_VERSION_OWNER,
              datasetVersionEntity.getId(),
              datasetVersionEntity.getOwner(),
              ModelResourceEnum.ModelDBServiceResourceTypes.DATASET_VERSION.name());
      if (ownerRoleBindingName != null && !ownerRoleBindingName.isEmpty()) {
        roleBindingNames.add(ownerRoleBindingName);
      }
    }
    transaction.commit();

    // Remove all role bindings
    if (!roleBindingNames.isEmpty()) {
      roleService.deleteRoleBindings(roleBindingNames);
    }
    LOGGER.debug(
        "DatasetVersion Deleted successfully : Deleted datasetVersions count {}",
        datasetVersionEntities.size());
  }

  private void deleteRepositories(Session session) {
    LOGGER.debug("Repository deleting");
    String alias = "rp";
    String deleteRepositorysQueryString =
        new StringBuilder("FROM ")
            .append(RepositoryEntity.class.getSimpleName())
            .append(" ")
            .append(alias)
            .append(" WHERE ")
            .append(alias)
            .append(".")
            .append(ModelDBConstants.DELETED)
            .append(" = :deleted ")
            .toString();
    Query repositoryDeleteQuery = session.createQuery(deleteRepositorysQueryString);
    repositoryDeleteQuery.setParameter("deleted", true);
    LOGGER.debug("Repository delete query: {}", repositoryDeleteQuery.getQueryString());

    Transaction transaction = session.beginTransaction();
    List<RepositoryEntity> repositoryEntities = repositoryDeleteQuery.list();

    for (RepositoryEntity repository : repositoryEntities) {
      String getRepositoryBranchesHql =
          new StringBuilder("From ")
              .append(BranchEntity.class.getSimpleName())
              .append(" br where br.id.")
              .append(ModelDBConstants.REPOSITORY_ID)
              .append(" = :repoId ")
              .toString();
      Query query = session.createQuery(getRepositoryBranchesHql);
      query.setParameter("repoId", repository.getId());
      List<BranchEntity> branchEntities = query.list();

      List<String> branches =
          branchEntities.stream()
              .map(branchEntity -> branchEntity.getId().getBranch())
              .collect(Collectors.toList());

      if (!branches.isEmpty()) {
        String deleteBranchesHQL =
            "DELETE FROM "
                + BranchEntity.class.getSimpleName()
                + " br where br.id.repository_id = :repositoryId AND br.id.branch IN (:branches)";
        Query deleteBranchQuery = session.createQuery(deleteBranchesHQL);
        deleteBranchQuery.setParameter("repositoryId", repository.getId());
        deleteBranchQuery.setParameterList("branches", branches);
        deleteBranchQuery.executeUpdate();
      }

      StringBuilder commitQueryBuilder =
          new StringBuilder(
              "SELECT cm FROM "
                  + CommitEntity.class.getSimpleName()
                  + " cm LEFT JOIN cm.repository repo WHERE repo.id = :repoId ");
      Query<CommitEntity> commitEntityQuery =
          session.createQuery(
              commitQueryBuilder.append(" ORDER BY cm.date_created DESC").toString());
      commitEntityQuery.setParameter("repoId", repository.getId());
      List<CommitEntity> commitEntities = commitEntityQuery.list();

      commitEntities.forEach(
          commitEntity -> {
            if (commitEntity.getRepository().contains(repository)) {
              commitEntity.getRepository().remove(repository);
              if (commitEntity.getRepository().isEmpty()) {
                session.delete(commitEntity);
              } else {
                session.update(commitEntity);
              }
            }
          });
      transaction.commit();

      deleteRoleBindingsOfAccessibleResources(Collections.singletonList(repository));
    }
    LOGGER.debug(
        "Repository Deleted successfully : Deleted repositorys count {}",
        repositoryEntities.size());
  }

  private void deleteRoleBindingsOfAccessibleResources(List<RepositoryEntity> allowedResources) {
    final List<String> roleBindingNames = Collections.synchronizedList(new ArrayList<>());
    for (RepositoryEntity repositoryEntity : allowedResources) {

      // Delete workspace based roleBindings
      List<String> repoOrgWorkspaceRoleBindings =
          roleService.getWorkspaceRoleBindings(
              repositoryEntity.getWorkspace_id(),
              WorkspaceTypeEnum.WorkspaceType.forNumber(repositoryEntity.getWorkspace_type()),
              String.valueOf(repositoryEntity.getId()),
              ModelDBConstants.ROLE_REPOSITORY_ADMIN,
              ModelResourceEnum.ModelDBServiceResourceTypes.REPOSITORY,
              repositoryEntity
                  .getRepository_visibility()
                  .equals(DatasetVisibilityEnum.DatasetVisibility.ORG_SCOPED_PUBLIC_VALUE),
              REPOSITORY_GLOBAL_SHARING);
      if (!repoOrgWorkspaceRoleBindings.isEmpty()) {
        roleBindingNames.addAll(repoOrgWorkspaceRoleBindings);
      }
    }
    // Remove all repositoryEntity collaborators
    roleService.deleteAllResources(
        allowedResources.stream()
            .map(repositoryEntity -> String.valueOf(repositoryEntity.getId()))
            .collect(Collectors.toList()),
        ModelResourceEnum.ModelDBServiceResourceTypes.REPOSITORY);

    // Remove all role bindings
    if (!roleBindingNames.isEmpty()) {
      roleService.deleteRoleBindings(roleBindingNames);
    }
  }
}
