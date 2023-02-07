# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/Collaborator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2
from ..uac import Organization_pb2 as uac_dot_Organization__pb2
from ..uac import Team_pb2 as uac_dot_Team__pb2
from ..uac import RoleService_pb2 as uac_dot_RoleService__pb2
from ..common import CommonService_pb2 as common_dot_CommonService__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16uac/Collaborator.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x14uac/UACService.proto\x1a\x16uac/Organization.proto\x1a\x0euac/Team.proto\x1a\x15uac/RoleService.proto\x1a\x1a\x63ommon/CommonService.proto\"\xe1\x01\n\x17\x43ollaboratorPermissions\x12Q\n\x11\x63ollaborator_type\x18\x01 \x01(\x0e\x32\x36.ai.verta.common.CollaboratorTypeEnum.CollaboratorType\x12\x38\n\ncan_deploy\x18\x02 \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x39\n\x0b\x63\x61n_predict\x18\x03 \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\"\xd5\x05\n\x16\x41\x64\x64\x43ollaboratorRequest\x12\x12\n\nentity_ids\x18\x01 \x03(\t\x12\x12\n\nshare_with\x18\x02 \x01(\t\x12Q\n\x11\x63ollaborator_type\x18\x03 \x01(\x0e\x32\x36.ai.verta.common.CollaboratorTypeEnum.CollaboratorType\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x61te_created\x18\x05 \x01(\x04\x12\x14\n\x0c\x64\x61te_updated\x18\x06 \x01(\x04\x12\x38\n\ncan_deploy\x18\x07 \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x39\n\x0b\x63\x61n_predict\x18\n \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x46\n\x11\x61uthz_entity_type\x18\x08 \x01(\x0e\x32+.ai.verta.common.EntitiesEnum.EntitiesTypes\x12\x39\n\npermission\x18\t \x01(\x0b\x32%.ai.verta.uac.CollaboratorPermissions\x1a\x8a\x02\n\x08Response\x12\x32\n\x14self_allowed_actions\x18\x05 \x03(\x0b\x32\x14.ai.verta.uac.Action\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x38\n\x16\x63ollaborator_user_info\x18\x02 \x01(\x0b\x32\x16.ai.verta.uac.UserInfoH\x00\x12?\n\x19\x63ollaborator_organization\x18\x03 \x01(\x0b\x32\x1a.ai.verta.uac.OrganizationH\x00\x12/\n\x11\x63ollaborator_team\x18\x04 \x01(\x0b\x32\x12.ai.verta.uac.TeamH\x00\x42\x0e\n\x0c\x63ollaborator\"\xe9\x01\n\x12RemoveCollaborator\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x12\n\nshare_with\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61te_deleted\x18\x03 \x01(\x04\x12\x46\n\x11\x61uthz_entity_type\x18\x04 \x01(\x0e\x32+.ai.verta.common.EntitiesEnum.EntitiesTypes\x1aN\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x32\n\x14self_allowed_actions\x18\x05 \x03(\x0b\x32\x14.ai.verta.uac.Action\"\xc3\x03\n\x1bGetCollaboratorResponseItem\x12\x13\n\x07user_id\x18\x01 \x01(\tB\x02\x18\x01\x12Q\n\x11\x63ollaborator_type\x18\x02 \x01(\x0e\x32\x36.ai.verta.common.CollaboratorTypeEnum.CollaboratorType\x12\x32\n\x0eshare_via_type\x18\x03 \x01(\x0e\x32\x1a.ai.verta.uac.ShareViaEnum\x12\x10\n\x08verta_id\x18\x04 \x01(\t\x12\x38\n\ncan_deploy\x18\x05 \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x39\n\x0b\x63\x61n_predict\x18\x08 \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x46\n\x11\x61uthz_entity_type\x18\x06 \x01(\x0e\x32+.ai.verta.common.EntitiesEnum.EntitiesTypes\x12\x39\n\npermission\x18\x07 \x01(\x0b\x32%.ai.verta.uac.CollaboratorPermissions\"\xb9\x01\n\x0fGetCollaborator\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12/\n\npagination\x18\x02 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x1a\x62\n\x08Response\x12?\n\x0cshared_users\x18\x01 \x03(\x0b\x32).ai.verta.uac.GetCollaboratorResponseItem\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"\xad\x02\n\x0cGetResources\x12*\n\tresources\x18\x01 \x01(\x0b\x32\x17.ai.verta.uac.Resources\x12\x16\n\x0cworkspace_id\x18\x02 \x01(\x04H\x00\x12\x18\n\x0eworkspace_name\x18\x03 \x01(\tH\x00\x12\x15\n\rresource_name\x18\x04 \x01(\t\x12/\n\npagination\x18\x05 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x12\x11\n\towner_ids\x18\x06 \x03(\x04\x1aW\n\x08Response\x12\x34\n\x04item\x18\x01 \x03(\x0b\x32&.ai.verta.uac.GetResourcesResponseItem\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\x42\x0b\n\tworkspace\"\x95\x03\n\x18GetResourcesResponseItem\x12\x32\n\x07service\x18\n \x01(\x0e\x32!.ai.verta.uac.ServiceEnum.Service\x12\x13\n\x0bresource_id\x18\x0b \x01(\t\x12\x15\n\rresource_name\x18\r \x01(\t\x12\x31\n\rresource_type\x18\x0c \x01(\x0b\x32\x1a.ai.verta.uac.ResourceType\x12\x14\n\x0cworkspace_id\x18\x02 \x01(\x04\x12\x12\n\x08owner_id\x18\x03 \x01(\x04H\x00\x12\x32\n\x0egroup_owner_id\x18\x0e \x01(\x0b\x32\x18.ai.verta.common.GroupIdH\x00\x12\x34\n\nvisibility\x18\x04 \x01(\x0e\x32 .ai.verta.uac.ResourceVisibility\x12@\n\x11\x63ustom_permission\x18\t \x01(\x0b\x32%.ai.verta.uac.CollaboratorPermissionsB\x10\n\x0eowner_tracking\"\xc3\x04\n\x0bSetResource\x12\x32\n\x07service\x18\x01 \x01(\x0e\x32!.ai.verta.uac.ServiceEnum.Service\x12\x13\n\x0bresource_id\x18\x08 \x01(\t\x12\x15\n\rresource_name\x18\t \x01(\t\x12\x31\n\rresource_type\x18\n \x01(\x0b\x32\x1a.ai.verta.uac.ResourceType\x12\x16\n\x0cworkspace_id\x18\x02 \x01(\x04H\x00\x12\x18\n\x0eworkspace_name\x18\x03 \x01(\tH\x00\x12\x12\n\x08owner_id\x18\x04 \x01(\x04H\x01\x12\x32\n\x0egroup_owner_id\x18\x0c \x01(\x0b\x32\x18.ai.verta.common.GroupIdH\x01\x12\x34\n\nvisibility\x18\x05 \x01(\x0e\x32 .ai.verta.uac.ResourceVisibility\x12Q\n\x11\x63ollaborator_type\x18\x06 \x01(\x0e\x32\x36.ai.verta.common.CollaboratorTypeEnum.CollaboratorType\x12\x38\n\ncan_deploy\x18\x07 \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x39\n\x0b\x63\x61n_predict\x18\x0b \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x1a\n\n\x08ResponseB\x0b\n\tworkspaceB\x10\n\x0eowner_tracking\"I\n\x0f\x44\x65leteResources\x12*\n\tresources\x18\x01 \x01(\x0b\x32\x17.ai.verta.uac.Resources\x1a\n\n\x08Response\"K\n\x0eResourceAdmins\x12\x10\n\x08user_ids\x18\x01 \x03(\t\x12\x10\n\x08team_ids\x18\x02 \x03(\t\x12\x15\n\rtotal_records\x18\x03 \x01(\x03\"\xc0\x01\n\x11GetResourceAdmins\x12\x32\n\x07service\x18\x01 \x01(\x0e\x32!.ai.verta.uac.ServiceEnum.Service\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x31\n\rresource_type\x18\x03 \x01(\x0b\x32\x1a.ai.verta.uac.ResourceType\x12/\n\npagination\x18\x04 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\"\xb6\x01\n\x14ModifyResourceAdmins\x12\x32\n\x07service\x18\x01 \x01(\x0e\x32!.ai.verta.uac.ServiceEnum.Service\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x31\n\rresource_type\x18\x03 \x01(\x0b\x32\x1a.ai.verta.uac.ResourceType\x12\x10\n\x08user_ids\x18\x04 \x03(\t\x12\x10\n\x08team_ids\x18\x05 \x03(\t*7\n\x0cShareViaEnum\x12\x0b\n\x07USER_ID\x10\x00\x12\x0c\n\x08\x45MAIL_ID\x10\x01\x12\x0c\n\x08USERNAME\x10\x02*f\n\x12ResourceVisibility\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bORG_DEFAULT\x10\x01\x12\x0e\n\nORG_CUSTOM\x10\x02\x12\x0b\n\x07PRIVATE\x10\x03\x12\x15\n\x11WORKSPACE_DEFAULT\x10\x04\x32\xae#\n\x13\x43ollaboratorService\x12v\n\x0cgetResources\x12\x1a.ai.verta.uac.GetResources\x1a#.ai.verta.uac.GetResources.Response\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/collaborator/getResources\x12\xa6\x01\n$getResourcesSpecialPersonalWorkspace\x12\x1a.ai.verta.uac.GetResources\x1a#.ai.verta.uac.GetResources.Response\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v1/collaborator/getResourcesSpecialPersonalWorkspace\x12u\n\x0bsetResource\x12\x19.ai.verta.uac.SetResource\x1a\".ai.verta.uac.SetResource.Response\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/collaborator/setResource:\x01*\x12Z\n\x0f\x64\x65leteResources\x12\x1d.ai.verta.uac.DeleteResources\x1a&.ai.verta.uac.DeleteResources.Response\"\x00\x12~\n\x11getResourceAdmins\x12\x1f.ai.verta.uac.GetResourceAdmins\x1a\x1c.ai.verta.uac.ResourceAdmins\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/collaborator/getResourceAdmins\x12{\n\x11\x61\x64\x64ResourceAdmins\x12\".ai.verta.uac.ModifyResourceAdmins\x1a\x13.ai.verta.uac.Empty\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/collaborator/addResourceAdmins:\x01*\x12\x81\x01\n\x14removeResourceAdmins\x12\".ai.verta.uac.ModifyResourceAdmins\x1a\x13.ai.verta.uac.Empty\"0\x82\xd3\xe4\x93\x02*\"%/v1/collaborator/removeResourceAdmins:\x01*\x12\xb1\x01\n\x1e\x61\x64\x64OrUpdateProjectCollaborator\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\":\x82\xd3\xe4\x93\x02\x34\"//v1/collaborator/addOrUpdateProjectCollaborator:\x01*\x12\x9c\x01\n\x19removeProjectCollaborator\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\"2\x82\xd3\xe4\x93\x02,**/v1/collaborator/removeProjectCollaborator\x12\x92\x01\n\x17getProjectCollaborators\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\"0\x82\xd3\xe4\x93\x02*\x12(/v1/collaborator/getProjectCollaborators\x12\xb1\x01\n\x1e\x61\x64\x64OrUpdateDatasetCollaborator\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\":\x82\xd3\xe4\x93\x02\x34\"//v1/collaborator/addOrUpdateDatasetCollaborator:\x01*\x12\x9c\x01\n\x19removeDatasetCollaborator\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\"2\x82\xd3\xe4\x93\x02,**/v1/collaborator/removeDatasetCollaborator\x12\x92\x01\n\x17getDatasetCollaborators\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\"0\x82\xd3\xe4\x93\x02*\x12(/v1/collaborator/getDatasetCollaborators\x12\xb7\x01\n!addOrUpdateRepositoryCollaborator\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\"=\x82\xd3\xe4\x93\x02\x37\"2/v1/collaborator/addOrUpdateRepositoryCollaborator:\x01*\x12\xa2\x01\n\x1cremoveRepositoryCollaborator\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\"5\x82\xd3\xe4\x93\x02/*-/v1/collaborator/removeRepositoryCollaborator\x12\x98\x01\n\x1agetRepositoryCollaborators\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\"3\x82\xd3\xe4\x93\x02-\x12+/v1/collaborator/getRepositoryCollaborators\x12\xb3\x01\n\x1f\x61\x64\x64OrUpdateEndpointCollaborator\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\";\x82\xd3\xe4\x93\x02\x35\"0/v1/collaborator/addOrUpdateEndpointCollaborator:\x01*\x12\x9e\x01\n\x1aremoveEndpointCollaborator\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\"3\x82\xd3\xe4\x93\x02-*+/v1/collaborator/removeEndpointCollaborator\x12\x94\x01\n\x18getEndpointCollaborators\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\"1\x82\xd3\xe4\x93\x02+\x12)/v1/collaborator/getEndpointCollaborators\x12\xcd\x01\n,addOrUpdateEndpointCollaboratorCommonService\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\"H\x82\xd3\xe4\x93\x02\x42\"=/v1/collaborator/addOrUpdateEndpointCollaboratorCommonService:\x01*\x12\xb8\x01\n\'removeEndpointCollaboratorCommonService\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\"@\x82\xd3\xe4\x93\x02:*8/v1/collaborator/removeEndpointCollaboratorCommonService\x12\xae\x01\n%getEndpointCollaboratorsCommonService\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\">\x82\xd3\xe4\x93\x02\x38\x12\x36/v1/collaborator/getEndpointCollaboratorsCommonService\x12\xc1\x01\n&addOrUpdateRegisteredModelCollaborator\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\"B\x82\xd3\xe4\x93\x02<\"7/v1/collaborator/addOrUpdateRegisteredModelCollaborator:\x01*\x12\xac\x01\n!removeRegisteredModelCollaborator\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\":\x82\xd3\xe4\x93\x02\x34*2/v1/collaborator/removeRegisteredModelCollaborator\x12\xa2\x01\n\x1fgetRegisteredModelCollaborators\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/collaborator/getRegisteredModelCollaborators\x12\xc1\x01\n&addOrUpdateMonitoredEntityCollaborator\x12$.ai.verta.uac.AddCollaboratorRequest\x1a-.ai.verta.uac.AddCollaboratorRequest.Response\"B\x82\xd3\xe4\x93\x02<\"7/v1/collaborator/addOrUpdateMonitoredEntityCollaborator:\x01*\x12\xac\x01\n!removeMonitoredEntityCollaborator\x12 .ai.verta.uac.RemoveCollaborator\x1a).ai.verta.uac.RemoveCollaborator.Response\":\x82\xd3\xe4\x93\x02\x34*2/v1/collaborator/removeMonitoredEntityCollaborator\x12\xa2\x01\n\x1fgetMonitoredEntityCollaborators\x12\x1d.ai.verta.uac.GetCollaborator\x1a&.ai.verta.uac.GetCollaborator.Response\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/collaborator/getMonitoredEntityCollaboratorsB>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uac.Collaborator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac'
  _GETCOLLABORATORRESPONSEITEM.fields_by_name['user_id']._options = None
  _GETCOLLABORATORRESPONSEITEM.fields_by_name['user_id']._serialized_options = b'\030\001'
  _COLLABORATORSERVICE.methods_by_name['getResources']._options = None
  _COLLABORATORSERVICE.methods_by_name['getResources']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/collaborator/getResources'
  _COLLABORATORSERVICE.methods_by_name['getResourcesSpecialPersonalWorkspace']._options = None
  _COLLABORATORSERVICE.methods_by_name['getResourcesSpecialPersonalWorkspace']._serialized_options = b'\202\323\344\223\0027\0225/v1/collaborator/getResourcesSpecialPersonalWorkspace'
  _COLLABORATORSERVICE.methods_by_name['setResource']._options = None
  _COLLABORATORSERVICE.methods_by_name['setResource']._serialized_options = b'\202\323\344\223\002!\"\034/v1/collaborator/setResource:\001*'
  _COLLABORATORSERVICE.methods_by_name['getResourceAdmins']._options = None
  _COLLABORATORSERVICE.methods_by_name['getResourceAdmins']._serialized_options = b'\202\323\344\223\002$\022\"/v1/collaborator/getResourceAdmins'
  _COLLABORATORSERVICE.methods_by_name['addResourceAdmins']._options = None
  _COLLABORATORSERVICE.methods_by_name['addResourceAdmins']._serialized_options = b'\202\323\344\223\002\'\"\"/v1/collaborator/addResourceAdmins:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeResourceAdmins']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeResourceAdmins']._serialized_options = b'\202\323\344\223\002*\"%/v1/collaborator/removeResourceAdmins:\001*'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateProjectCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateProjectCollaborator']._serialized_options = b'\202\323\344\223\0024\"//v1/collaborator/addOrUpdateProjectCollaborator:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeProjectCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeProjectCollaborator']._serialized_options = b'\202\323\344\223\002,**/v1/collaborator/removeProjectCollaborator'
  _COLLABORATORSERVICE.methods_by_name['getProjectCollaborators']._options = None
  _COLLABORATORSERVICE.methods_by_name['getProjectCollaborators']._serialized_options = b'\202\323\344\223\002*\022(/v1/collaborator/getProjectCollaborators'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateDatasetCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateDatasetCollaborator']._serialized_options = b'\202\323\344\223\0024\"//v1/collaborator/addOrUpdateDatasetCollaborator:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeDatasetCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeDatasetCollaborator']._serialized_options = b'\202\323\344\223\002,**/v1/collaborator/removeDatasetCollaborator'
  _COLLABORATORSERVICE.methods_by_name['getDatasetCollaborators']._options = None
  _COLLABORATORSERVICE.methods_by_name['getDatasetCollaborators']._serialized_options = b'\202\323\344\223\002*\022(/v1/collaborator/getDatasetCollaborators'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateRepositoryCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateRepositoryCollaborator']._serialized_options = b'\202\323\344\223\0027\"2/v1/collaborator/addOrUpdateRepositoryCollaborator:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeRepositoryCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeRepositoryCollaborator']._serialized_options = b'\202\323\344\223\002/*-/v1/collaborator/removeRepositoryCollaborator'
  _COLLABORATORSERVICE.methods_by_name['getRepositoryCollaborators']._options = None
  _COLLABORATORSERVICE.methods_by_name['getRepositoryCollaborators']._serialized_options = b'\202\323\344\223\002-\022+/v1/collaborator/getRepositoryCollaborators'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateEndpointCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateEndpointCollaborator']._serialized_options = b'\202\323\344\223\0025\"0/v1/collaborator/addOrUpdateEndpointCollaborator:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeEndpointCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeEndpointCollaborator']._serialized_options = b'\202\323\344\223\002-*+/v1/collaborator/removeEndpointCollaborator'
  _COLLABORATORSERVICE.methods_by_name['getEndpointCollaborators']._options = None
  _COLLABORATORSERVICE.methods_by_name['getEndpointCollaborators']._serialized_options = b'\202\323\344\223\002+\022)/v1/collaborator/getEndpointCollaborators'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateEndpointCollaboratorCommonService']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateEndpointCollaboratorCommonService']._serialized_options = b'\202\323\344\223\002B\"=/v1/collaborator/addOrUpdateEndpointCollaboratorCommonService:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeEndpointCollaboratorCommonService']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeEndpointCollaboratorCommonService']._serialized_options = b'\202\323\344\223\002:*8/v1/collaborator/removeEndpointCollaboratorCommonService'
  _COLLABORATORSERVICE.methods_by_name['getEndpointCollaboratorsCommonService']._options = None
  _COLLABORATORSERVICE.methods_by_name['getEndpointCollaboratorsCommonService']._serialized_options = b'\202\323\344\223\0028\0226/v1/collaborator/getEndpointCollaboratorsCommonService'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateRegisteredModelCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateRegisteredModelCollaborator']._serialized_options = b'\202\323\344\223\002<\"7/v1/collaborator/addOrUpdateRegisteredModelCollaborator:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeRegisteredModelCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeRegisteredModelCollaborator']._serialized_options = b'\202\323\344\223\0024*2/v1/collaborator/removeRegisteredModelCollaborator'
  _COLLABORATORSERVICE.methods_by_name['getRegisteredModelCollaborators']._options = None
  _COLLABORATORSERVICE.methods_by_name['getRegisteredModelCollaborators']._serialized_options = b'\202\323\344\223\0022\0220/v1/collaborator/getRegisteredModelCollaborators'
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateMonitoredEntityCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['addOrUpdateMonitoredEntityCollaborator']._serialized_options = b'\202\323\344\223\002<\"7/v1/collaborator/addOrUpdateMonitoredEntityCollaborator:\001*'
  _COLLABORATORSERVICE.methods_by_name['removeMonitoredEntityCollaborator']._options = None
  _COLLABORATORSERVICE.methods_by_name['removeMonitoredEntityCollaborator']._serialized_options = b'\202\323\344\223\0024*2/v1/collaborator/removeMonitoredEntityCollaborator'
  _COLLABORATORSERVICE.methods_by_name['getMonitoredEntityCollaborators']._options = None
  _COLLABORATORSERVICE.methods_by_name['getMonitoredEntityCollaborators']._serialized_options = b'\202\323\344\223\0022\0220/v1/collaborator/getMonitoredEntityCollaborators'
  _SHAREVIAENUM._serialized_start=3843
  _SHAREVIAENUM._serialized_end=3898
  _RESOURCEVISIBILITY._serialized_start=3900
  _RESOURCEVISIBILITY._serialized_end=4002
  _COLLABORATORPERMISSIONS._serialized_start=184
  _COLLABORATORPERMISSIONS._serialized_end=409
  _ADDCOLLABORATORREQUEST._serialized_start=412
  _ADDCOLLABORATORREQUEST._serialized_end=1137
  _ADDCOLLABORATORREQUEST_RESPONSE._serialized_start=871
  _ADDCOLLABORATORREQUEST_RESPONSE._serialized_end=1137
  _REMOVECOLLABORATOR._serialized_start=1140
  _REMOVECOLLABORATOR._serialized_end=1373
  _REMOVECOLLABORATOR_RESPONSE._serialized_start=1295
  _REMOVECOLLABORATOR_RESPONSE._serialized_end=1373
  _GETCOLLABORATORRESPONSEITEM._serialized_start=1376
  _GETCOLLABORATORRESPONSEITEM._serialized_end=1827
  _GETCOLLABORATOR._serialized_start=1830
  _GETCOLLABORATOR._serialized_end=2015
  _GETCOLLABORATOR_RESPONSE._serialized_start=1917
  _GETCOLLABORATOR_RESPONSE._serialized_end=2015
  _GETRESOURCES._serialized_start=2018
  _GETRESOURCES._serialized_end=2319
  _GETRESOURCES_RESPONSE._serialized_start=2219
  _GETRESOURCES_RESPONSE._serialized_end=2306
  _GETRESOURCESRESPONSEITEM._serialized_start=2322
  _GETRESOURCESRESPONSEITEM._serialized_end=2727
  _SETRESOURCE._serialized_start=2730
  _SETRESOURCE._serialized_end=3309
  _SETRESOURCE_RESPONSE._serialized_start=871
  _SETRESOURCE_RESPONSE._serialized_end=881
  _DELETERESOURCES._serialized_start=3311
  _DELETERESOURCES._serialized_end=3384
  _DELETERESOURCES_RESPONSE._serialized_start=871
  _DELETERESOURCES_RESPONSE._serialized_end=881
  _RESOURCEADMINS._serialized_start=3386
  _RESOURCEADMINS._serialized_end=3461
  _GETRESOURCEADMINS._serialized_start=3464
  _GETRESOURCEADMINS._serialized_end=3656
  _MODIFYRESOURCEADMINS._serialized_start=3659
  _MODIFYRESOURCEADMINS._serialized_end=3841
  _COLLABORATORSERVICE._serialized_start=4005
  _COLLABORATORSERVICE._serialized_end=8531
# @@protoc_insertion_point(module_scope)
