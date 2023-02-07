# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registry/RegistryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ..common import CommonService_pb2 as common_dot_CommonService__pb2
from ..modeldb.versioning import Environment_pb2 as modeldb_dot_versioning_dot_Environment__pb2
from ..modeldb.versioning import Code_pb2 as modeldb_dot_versioning_dot_Code__pb2
from ..registry import StageService_pb2 as registry_dot_StageService__pb2
from ..uac import Collaborator_pb2 as uac_dot_Collaborator__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eregistry/RegistryService.proto\x12\x11\x61i.verta.registry\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1a\x63ommon/CommonService.proto\x1a$modeldb/versioning/Environment.proto\x1a\x1dmodeldb/versioning/Code.proto\x1a\x1bregistry/StageService.proto\x1a\x16uac/Collaborator.proto\"j\n\x0c\x44\x61taTypeEnum\"Z\n\x08\x44\x61taType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\t\n\x05\x41UDIO\x10\x02\x12\t\n\x05IMAGE\x10\x03\x12\x0b\n\x07TABULAR\x10\x04\x12\x08\n\x04TEXT\x10\x05\x12\t\n\x05VIDEO\x10\x06\"\xa6\x01\n\x0e\x41\x63tionTypeEnum\"\x8f\x01\n\nActionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\x12\n\x0e\x43LASSIFICATION\x10\x02\x12\x0e\n\nCLUSTERING\x10\x03\x12\r\n\tDETECTION\x10\x04\x12\x0e\n\nREGRESSION\x10\x05\x12\x11\n\rTRANSCRIPTION\x10\x06\x12\x0f\n\x0bTRANSLATION\x10\x07\x1a\x02\x18\x01:\x02\x18\x01\"\x9a\x01\n\x0cTaskTypeEnum\"\x89\x01\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\x12\n\x0e\x43LASSIFICATION\x10\x02\x12\x0e\n\nCLUSTERING\x10\x03\x12\r\n\tDETECTION\x10\x04\x12\x0e\n\nREGRESSION\x10\x05\x12\x11\n\rTRANSCRIPTION\x10\x06\x12\x0f\n\x0bTRANSLATION\x10\x07\"\xe8\x05\n\x0fRegisteredModel\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0ctime_created\x18\x03 \x01(\x03\x12\x14\n\x0ctime_updated\x18\x04 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0e\n\x06labels\x18\x06 \x03(\t\x12>\n\nvisibility\x18\x07 \x01(\x0e\x32*.ai.verta.common.VisibilityEnum.Visibility\x12\x14\n\x0cworkspace_id\x18\x08 \x01(\t\x12\x13\n\x0breadme_text\x18\t \x01(\t\x12\r\n\x05owner\x18\n \x01(\t\x12-\n\nattributes\x18\x0b \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x12\x1c\n\x14workspace_service_id\x18\x0c \x01(\x04\x12@\n\x11\x63ustom_permission\x18\r \x01(\x0b\x32%.ai.verta.uac.CollaboratorPermissions\x12=\n\x13resource_visibility\x18\x0e \x01(\x0e\x32 .ai.verta.uac.ResourceVisibility\x12,\n\tartifacts\x18\x0f \x03(\x0b\x32\x19.ai.verta.common.Artifact\x12\x1b\n\x13readme_text_updated\x18\x10 \x01(\x08\x12\x16\n\x0eversion_number\x18\x11 \x01(\x04\x12;\n\tdata_type\x18\x12 \x01(\x0e\x32(.ai.verta.registry.DataTypeEnum.DataType\x12\x45\n\x0b\x61\x63tion_type\x18\x13 \x01(\x0e\x32,.ai.verta.registry.ActionTypeEnum.ActionTypeB\x02\x18\x01\x12;\n\ttask_type\x18\x14 \x01(\x0e\x32(.ai.verta.registry.TaskTypeEnum.TaskType\"\xad\x02\n\x1a\x46indRegisteredModelRequest\x12\x16\n\x0eworkspace_name\x18\x01 \x01(\t\x12\x32\n\npredicates\x18\x02 \x03(\x0b\x32\x1e.ai.verta.common.KeyValueQuery\x12/\n\npagination\x18\x03 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x12\x11\n\tascending\x18\x04 \x01(\x08\x12\x10\n\x08sort_key\x18\x05 \x01(\t\x12\x0b\n\x03ids\x18\x06 \x03(\x04\x1a`\n\x08Response\x12=\n\x11registered_models\x18\x01 \x03(\x0b\x32\".ai.verta.registry.RegisteredModel\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"\xa3\x01\n\x19GetRegisteredModelRequest\x12<\n\x02id\x18\x01 \x01(\x0b\x32\x30.ai.verta.registry.RegisteredModelIdentification\x1aH\n\x08Response\x12<\n\x10registered_model\x18\x01 \x01(\x0b\x32\".ai.verta.registry.RegisteredModel\"`\n\x1eGetRegisteredModelCountRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x1a*\n\x08Response\x12\x1e\n\x16registered_model_count\x18\x01 \x01(\x03\"J\n\"RegisteredModelNamedIdentification\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eworkspace_name\x18\x02 \x01(\t\"\x85\x01\n\x1dRegisteredModelIdentification\x12G\n\x08named_id\x18\x01 \x01(\x0b\x32\x35.ai.verta.registry.RegisteredModelNamedIdentification\x12\x1b\n\x13registered_model_id\x18\x02 \x01(\x04\"\x8b\x02\n\x12SetRegisteredModel\x12<\n\x02id\x18\x01 \x01(\x0b\x32\x30.ai.verta.registry.RegisteredModelIdentification\x12<\n\x10registered_model\x18\x02 \x01(\x0b\x32\".ai.verta.registry.RegisteredModel\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x1aH\n\x08Response\x12<\n\x10registered_model\x18\x01 \x01(\x0b\x32\".ai.verta.registry.RegisteredModel\"h\n\x1c\x44\x65leteRegisteredModelRequest\x12<\n\x02id\x18\x01 \x01(\x0b\x32\x30.ai.verta.registry.RegisteredModelIdentification\x1a\n\n\x08Response\"c\n\x19ModelVersionLockLevelEnum\"F\n\x15ModelVersionLockLevel\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\n\n\x06\x43LOSED\x10\x02\x12\n\n\x06REDACT\x10\x03\"\x8d\t\n\x0cModelVersion\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x1b\n\x13registered_model_id\x18\x02 \x01(\x04\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x14\n\x0ctime_updated\x18\x04 \x01(\x03\x12\x14\n\x0ctime_created\x18\x05 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x1b\n\x11\x65xperiment_run_id\x18\x07 \x01(\tH\x00\x12\x0e\n\x06labels\x18\x08 \x03(\t\x12(\n\x05model\x18\t \x01(\x0b\x32\x19.ai.verta.common.Artifact\x12\x41\n\x0b\x65nvironment\x18\n \x01(\x0b\x32,.ai.verta.modeldb.versioning.EnvironmentBlob\x12:\n\x0f\x64ocker_metadata\x18\x18 \x01(\x0b\x32!.ai.verta.registry.DockerMetadata\x12,\n\tartifacts\x18\x0b \x03(\x0b\x32\x19.ai.verta.common.Artifact\x12\x36\n\x08\x61rchived\x18\x0c \x01(\x0e\x32$.ai.verta.common.TernaryEnum.Ternary\x12\x13\n\x0breadme_text\x18\r \x01(\t\x12\x0c\n\x04\x61pis\x18\x0f \x03(\t\x12\r\n\x05owner\x18\x10 \x01(\t\x12-\n\nattributes\x18\x11 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x12\x31\n\x05stage\x18\x12 \x01(\x0e\x32\".ai.verta.registry.StageEnum.Stage\x12V\n\nlock_level\x18\x13 \x01(\x0e\x32\x42.ai.verta.registry.ModelVersionLockLevelEnum.ModelVersionLockLevel\x12+\n\x08\x64\x61tasets\x18\x14 \x03(\x0b\x32\x19.ai.verta.common.Artifact\x12G\n\rcode_blob_map\x18\x15 \x03(\x0b\x32\x30.ai.verta.registry.ModelVersion.CodeBlobMapEntry\x12\x1b\n\x13readme_text_updated\x18\x16 \x01(\x08\x12\x16\n\x0eversion_number\x18\x17 \x01(\x04\x12\x19\n\x11redirect_metadata\x18\x19 \x01(\t\x12\x19\n\x11input_description\x18\x1a \x01(\t\x12\x18\n\x10hide_input_label\x18\x1b \x01(\x08\x12\x1a\n\x12output_description\x18\x1c \x01(\t\x12\x19\n\x11hide_output_label\x18\x1d \x01(\x08\x12\x43\n\x14\x65xternal_deployments\x18\x1e \x03(\x0b\x32%.ai.verta.registry.ExternalDeployment\x1aY\n\x10\x43odeBlobMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.ai.verta.modeldb.versioning.CodeBlob:\x02\x38\x01\x42\x08\n\x06source\"Q\n\x0e\x44ockerMetadata\x12\x14\n\x0crequest_port\x18\x01 \x01(\r\x12\x14\n\x0crequest_path\x18\x02 \x01(\t\x12\x13\n\x0bhealth_path\x18\x03 \x01(\t\"\xbb\x01\n\x1aSetLockModelVersionRequest\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32-.ai.verta.registry.ModelVersionIdentification\x12V\n\nlock_level\x18\x02 \x01(\x0e\x32\x42.ai.verta.registry.ModelVersionLockLevelEnum.ModelVersionLockLevel\x1a\n\n\x08Response\"z\n\x1aModelVersionIdentification\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12\x42\n\x08model_id\x18\x02 \x01(\x0b\x32\x30.ai.verta.registry.RegisteredModelIdentification\"\x97\x01\n\x16GetModelVersionRequest\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32-.ai.verta.registry.ModelVersionIdentification\x1a\x42\n\x08Response\x12\x36\n\rmodel_version\x18\x01 \x01(\x0b\x32\x1f.ai.verta.registry.ModelVersion\"\xca\x02\n\x17\x46indModelVersionRequest\x12<\n\x02id\x18\x01 \x01(\x0b\x32\x30.ai.verta.registry.RegisteredModelIdentification\x12\x32\n\npredicates\x18\x02 \x03(\x0b\x32\x1e.ai.verta.common.KeyValueQuery\x12/\n\npagination\x18\x03 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x12\x11\n\tascending\x18\x04 \x01(\x08\x12\x10\n\x08sort_key\x18\x05 \x01(\t\x12\x0b\n\x03ids\x18\x06 \x03(\x04\x1aZ\n\x08Response\x12\x37\n\x0emodel_versions\x18\x01 \x03(\x0b\x32\x1f.ai.verta.registry.ModelVersion\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"\xf9\x01\n\x0fSetModelVersion\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32-.ai.verta.registry.ModelVersionIdentification\x12\x36\n\rmodel_version\x18\x02 \x01(\x0b\x32\x1f.ai.verta.registry.ModelVersion\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x1a\x42\n\x08Response\x12\x36\n\rmodel_version\x18\x01 \x01(\x0b\x32\x1f.ai.verta.registry.ModelVersion\"b\n\x19\x44\x65leteModelVersionRequest\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32-.ai.verta.registry.ModelVersionIdentification\x1a\n\n\x08Response\"\xd7\x02\n\x11GetUrlForArtifact\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x45\n\rartifact_type\x18\x04 \x01(\x0e\x32..ai.verta.common.ArtifactTypeEnum.ArtifactType\x12\x13\n\x0bpart_number\x18\x05 \x01(\x04\x1a\xae\x01\n\x08Response\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x1b\n\x13multipart_upload_ok\x18\x02 \x01(\x08\x12I\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x39.ai.verta.registry.GetUrlForArtifact.Response.FieldsEntry\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\x12\x43ommitArtifactPart\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x34\n\rartifact_part\x18\x03 \x01(\x0b\x32\x1d.ai.verta.common.ArtifactPart\x1a\n\n\x08Response\"\x85\x01\n\x19GetCommittedArtifactParts\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12\x0b\n\x03key\x18\x02 \x01(\t\x1a\x41\n\x08Response\x12\x35\n\x0e\x61rtifact_parts\x18\x01 \x03(\x0b\x32\x1d.ai.verta.common.ArtifactPart\"L\n\x17\x43ommitMultipartArtifact\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12\x0b\n\x03key\x18\x02 \x01(\t\x1a\n\n\x08Response\"n\n\x19LogDatasetsInModelVersion\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12+\n\x08\x64\x61tasets\x18\x02 \x03(\x0b\x32\x19.ai.verta.common.Artifact\x1a\n\n\x08Response\"\xf2\x01\n\x19LogCodeBlobInModelVersion\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12T\n\rcode_blob_map\x18\x02 \x03(\x0b\x32=.ai.verta.registry.LogCodeBlobInModelVersion.CodeBlobMapEntry\x1aY\n\x10\x43odeBlobMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.ai.verta.modeldb.versioning.CodeBlob:\x02\x38\x01\x1a\n\n\x08Response\"r\n\x1bLogAttributesInModelVersion\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12-\n\nattributes\x18\x02 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x1a\n\n\x08Response\"\x83\x01\n\x1fLogDockerMetadataInModelVersion\x12\x18\n\x10model_version_id\x18\x01 \x01(\x04\x12:\n\x0f\x64ocker_metadata\x18\x02 \x01(\x0b\x32!.ai.verta.registry.DockerMetadata\x1a\n\n\x08Response\"\xae\x01\n\x12\x45xternalDeployment\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x18\n\x10model_version_id\x18\x02 \x01(\x04\x12\x14\n\x0ctime_created\x18\x03 \x01(\x03\x12\x14\n\x0ctime_updated\x18\x04 \x01(\x03\x12\x19\n\x11location_deployed\x18\x05 \x01(\t\x12\x16\n\x0eurl_path_title\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\"\x8b\x01\n\x19\x45xternalDeploymentRequest\x12\x1e\n\x16\x65xternal_deployment_id\x18\x01 \x01(\x04\x1aN\n\x08Response\x12\x42\n\x13\x65xternal_deployment\x18\x01 \x01(\x0b\x32%.ai.verta.registry.ExternalDeployment\"\x07\n\x05\x45mpty2\xc0\x37\n\x0fRegistryService\x12\xf2\x01\n\x13\x46indRegisteredModel\x12-.ai.verta.registry.FindRegisteredModelRequest\x1a\x36.ai.verta.registry.FindRegisteredModelRequest.Response\"t\x82\xd3\xe4\x93\x02n\"?/v1/registry/workspaces/{workspace_name}/registered_models/find:\x01*Z(\"#/v1/registry/registered_models/find:\x01*\x12\x99\x02\n\x12GetRegisteredModel\x12,.ai.verta.registry.GetRegisteredModelRequest\x1a\x35.ai.verta.registry.GetRegisteredModelRequest.Response\"\x9d\x01\x82\xd3\xe4\x93\x02\x96\x01\x12Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}Z9\x12\x37/v1/registry/registered_models/{id.registered_model_id}\x12\xb6\x01\n\x17GetRegisteredModelCount\x12\x31.ai.verta.registry.GetRegisteredModelCountRequest\x1a:.ai.verta.registry.GetRegisteredModelCountRequest.Response\",\x82\xd3\xe4\x93\x02&\x12$/v1/registry/registered_models/count\x12\xd0\x01\n\x15\x43reateRegisteredModel\x12%.ai.verta.registry.SetRegisteredModel\x1a..ai.verta.registry.SetRegisteredModel.Response\"`\x82\xd3\xe4\x93\x02Z\"F/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models:\x10registered_model\x12\xa0\x05\n\x15UpdateRegisteredModel\x12%.ai.verta.registry.SetRegisteredModel\x1a..ai.verta.registry.SetRegisteredModel.Response\"\xaf\x04\x82\xd3\xe4\x93\x02\xa8\x04\x32Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}:\x10registered_modelZK27/v1/registry/registered_models/{id.registered_model_id}:\x10registered_modelZh2c/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}/full_body:\x01*ZF2A/v1/registry/registered_models/{id.registered_model_id}/full_body:\x01*Zm\x1aY/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}:\x10registered_modelZK\x1a\x37/v1/registry/registered_models/{id.registered_model_id}:\x10registered_model\x12\xa2\x02\n\x15\x44\x65leteRegisteredModel\x12/.ai.verta.registry.DeleteRegisteredModelRequest\x1a\x38.ai.verta.registry.DeleteRegisteredModelRequest.Response\"\x9d\x01\x82\xd3\xe4\x93\x02\x96\x01*Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}Z9*7/v1/registry/registered_models/{id.registered_model_id}\x12\xb7\x03\n\x10\x46indModelVersion\x12*.ai.verta.registry.FindModelVersionRequest\x1a\x33.ai.verta.registry.FindModelVersionRequest.Response\"\xc1\x02\x82\xd3\xe4\x93\x02\xba\x02\"m/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}/model_versions/find:\x01*ZP\"K/v1/registry/registered_models/{id.registered_model_id}/model_versions/find:\x01*ZM\"H/v1/registry/workspaces/{id.named_id.workspace_name}/model_versions/find:\x01*Z%\" /v1/registry/model_versions/find:\x01*\x12\xc2\x02\n\x0fGetModelVersion\x12).ai.verta.registry.GetModelVersionRequest\x1a\x32.ai.verta.registry.GetModelVersionRequest.Response\"\xcf\x01\x82\xd3\xe4\x93\x02\xc8\x01\x12\x90\x01/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}Z3\x12\x31/v1/registry/model_versions/{id.model_version_id}\x12\xdc\x02\n\x12\x43reateModelVersion\x12\".ai.verta.registry.SetModelVersion\x1a+.ai.verta.registry.SetModelVersion.Response\"\xf4\x01\x82\xd3\xe4\x93\x02\xed\x01\"z/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions:\rmodel_versionZ`\"O/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions:\rmodel_version\x12\xbf\x07\n\x12UpdateModelVersion\x12\".ai.verta.registry.SetModelVersion\x1a+.ai.verta.registry.SetModelVersion.Response\"\xd7\x06\x82\xd3\xe4\x93\x02\xd0\x06\x32\x90\x01/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}:\rmodel_versionZv2e/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}:\rmodel_versionZ\xa0\x01\x32\x9a\x01/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}/full_body:\x01*Zt2o/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}/full_body:\x01*Z\xa2\x01\x1a\x90\x01/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}:\rmodel_versionZv\x1a\x65/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}:\rmodel_version\x12\xbf\x01\n\x13SetLockModelVersion\x12-.ai.verta.registry.SetLockModelVersionRequest\x1a\x36.ai.verta.registry.SetLockModelVersionRequest.Response\"A\x82\xd3\xe4\x93\x02;\x1a\x36/v1/registry/model_versions/{id.model_version_id}/lock:\x01*\x12\xb4\x03\n\x12\x44\x65leteModelVersion\x12,.ai.verta.registry.DeleteModelVersionRequest\x1a\x35.ai.verta.registry.DeleteModelVersionRequest.Response\"\xb8\x02\x82\xd3\xe4\x93\x02\xb1\x02*\x90\x01/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}Zg*e/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}Z3*1/v1/registry/model_versions/{id.model_version_id}\x12\xb5\x01\n\x11getUrlForArtifact\x12$.ai.verta.registry.GetUrlForArtifact\x1a-.ai.verta.registry.GetUrlForArtifact.Response\"K\x82\xd3\xe4\x93\x02\x45\"@/v1/registry/model_versions/{model_version_id}/getUrlForArtifact:\x01*\x12\xb9\x01\n\x12\x63ommitArtifactPart\x12%.ai.verta.registry.CommitArtifactPart\x1a..ai.verta.registry.CommitArtifactPart.Response\"L\x82\xd3\xe4\x93\x02\x46\"A/v1/registry/model_versions/{model_version_id}/commitArtifactPart:\x01*\x12\xd2\x01\n\x19getCommittedArtifactParts\x12,.ai.verta.registry.GetCommittedArtifactParts\x1a\x35.ai.verta.registry.GetCommittedArtifactParts.Response\"P\x82\xd3\xe4\x93\x02J\x12H/v1/registry/model_versions/{model_version_id}/getCommittedArtifactParts\x12\xcd\x01\n\x17\x63ommitMultipartArtifact\x12*.ai.verta.registry.CommitMultipartArtifact\x1a\x33.ai.verta.registry.CommitMultipartArtifact.Response\"Q\x82\xd3\xe4\x93\x02K\"F/v1/registry/model_versions/{model_version_id}/commitMultipartArtifact:\x01*\x12\xc7\x01\n\x19logDatasetsInModelVersion\x12,.ai.verta.registry.LogDatasetsInModelVersion\x1a\x35.ai.verta.registry.LogDatasetsInModelVersion.Response\"E\x82\xd3\xe4\x93\x02?\":/v1/registry/model_versions/{model_version_id}/logDatasets:\x01*\x12\xd5\x01\n\x19logCodeBlobInModelVersion\x12,.ai.verta.registry.LogCodeBlobInModelVersion\x1a\x35.ai.verta.registry.LogCodeBlobInModelVersion.Response\"S\x82\xd3\xe4\x93\x02M\"H/v1/registry/model_versions/{model_version_id}/logCodeBlobInModelVersion:\x01*\x12\xcf\x01\n\x1blogAttributesInModelVersion\x12..ai.verta.registry.LogAttributesInModelVersion\x1a\x37.ai.verta.registry.LogAttributesInModelVersion.Response\"G\x82\xd3\xe4\x93\x02\x41\"</v1/registry/model_versions/{model_version_id}/logAttributes:\x01*\x12\xdf\x01\n\x1flogDockerMetadataInModelVersion\x12\x32.ai.verta.registry.LogDockerMetadataInModelVersion\x1a;.ai.verta.registry.LogDockerMetadataInModelVersion.Response\"K\x82\xd3\xe4\x93\x02\x45\"@/v1/registry/model_versions/{model_version_id}/logDockerMetadata:\x01*\x12\xe1\x01\n\x15GetExternalDeployment\x12,.ai.verta.registry.ExternalDeploymentRequest\x1a\x35.ai.verta.registry.ExternalDeploymentRequest.Response\"c\x82\xd3\xe4\x93\x02]\x12[/v1/registry/registered_models/model_versions/external_deployments/{external_deployment_id}\x12\xc7\x01\n\x18\x43reateExternalDeployment\x12%.ai.verta.registry.ExternalDeployment\x1a\x35.ai.verta.registry.ExternalDeploymentRequest.Response\"M\x82\xd3\xe4\x93\x02G\"B/v1/registry/registered_models/model_versions/external_deployments:\x01*\x12\xc7\x01\n\x18UpdateExternalDeployment\x12%.ai.verta.registry.ExternalDeployment\x1a\x35.ai.verta.registry.ExternalDeploymentRequest.Response\"M\x82\xd3\xe4\x93\x02G\x1a\x42/v1/registry/registered_models/model_versions/external_deployments:\x01*\x12\xc7\x01\n\x18\x44\x65leteExternalDeployment\x12,.ai.verta.registry.ExternalDeploymentRequest\x1a\x18.ai.verta.registry.Empty\"c\x82\xd3\xe4\x93\x02]*[/v1/registry/registered_models/model_versions/external_deployments/{external_deployment_id}BCP\x01Z?github.com/VertaAI/modeldb/protos/gen/go/protos/public/registryb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'registry.RegistryService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001Z?github.com/VertaAI/modeldb/protos/gen/go/protos/public/registry'
  _ACTIONTYPEENUM_ACTIONTYPE._options = None
  _ACTIONTYPEENUM_ACTIONTYPE._serialized_options = b'\030\001'
  _ACTIONTYPEENUM._options = None
  _ACTIONTYPEENUM._serialized_options = b'\030\001'
  _REGISTEREDMODEL.fields_by_name['action_type']._options = None
  _REGISTEREDMODEL.fields_by_name['action_type']._serialized_options = b'\030\001'
  _MODELVERSION_CODEBLOBMAPENTRY._options = None
  _MODELVERSION_CODEBLOBMAPENTRY._serialized_options = b'8\001'
  _GETURLFORARTIFACT_RESPONSE_FIELDSENTRY._options = None
  _GETURLFORARTIFACT_RESPONSE_FIELDSENTRY._serialized_options = b'8\001'
  _LOGCODEBLOBINMODELVERSION_CODEBLOBMAPENTRY._options = None
  _LOGCODEBLOBINMODELVERSION_CODEBLOBMAPENTRY._serialized_options = b'8\001'
  _REGISTRYSERVICE.methods_by_name['FindRegisteredModel']._options = None
  _REGISTRYSERVICE.methods_by_name['FindRegisteredModel']._serialized_options = b'\202\323\344\223\002n\"?/v1/registry/workspaces/{workspace_name}/registered_models/find:\001*Z(\"#/v1/registry/registered_models/find:\001*'
  _REGISTRYSERVICE.methods_by_name['GetRegisteredModel']._options = None
  _REGISTRYSERVICE.methods_by_name['GetRegisteredModel']._serialized_options = b'\202\323\344\223\002\226\001\022Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}Z9\0227/v1/registry/registered_models/{id.registered_model_id}'
  _REGISTRYSERVICE.methods_by_name['GetRegisteredModelCount']._options = None
  _REGISTRYSERVICE.methods_by_name['GetRegisteredModelCount']._serialized_options = b'\202\323\344\223\002&\022$/v1/registry/registered_models/count'
  _REGISTRYSERVICE.methods_by_name['CreateRegisteredModel']._options = None
  _REGISTRYSERVICE.methods_by_name['CreateRegisteredModel']._serialized_options = b'\202\323\344\223\002Z\"F/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models:\020registered_model'
  _REGISTRYSERVICE.methods_by_name['UpdateRegisteredModel']._options = None
  _REGISTRYSERVICE.methods_by_name['UpdateRegisteredModel']._serialized_options = b'\202\323\344\223\002\250\0042Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}:\020registered_modelZK27/v1/registry/registered_models/{id.registered_model_id}:\020registered_modelZh2c/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}/full_body:\001*ZF2A/v1/registry/registered_models/{id.registered_model_id}/full_body:\001*Zm\032Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}:\020registered_modelZK\0327/v1/registry/registered_models/{id.registered_model_id}:\020registered_model'
  _REGISTRYSERVICE.methods_by_name['DeleteRegisteredModel']._options = None
  _REGISTRYSERVICE.methods_by_name['DeleteRegisteredModel']._serialized_options = b'\202\323\344\223\002\226\001*Y/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}Z9*7/v1/registry/registered_models/{id.registered_model_id}'
  _REGISTRYSERVICE.methods_by_name['FindModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['FindModelVersion']._serialized_options = b'\202\323\344\223\002\272\002\"m/v1/registry/workspaces/{id.named_id.workspace_name}/registered_models/{id.named_id.name}/model_versions/find:\001*ZP\"K/v1/registry/registered_models/{id.registered_model_id}/model_versions/find:\001*ZM\"H/v1/registry/workspaces/{id.named_id.workspace_name}/model_versions/find:\001*Z%\" /v1/registry/model_versions/find:\001*'
  _REGISTRYSERVICE.methods_by_name['GetModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['GetModelVersion']._serialized_options = b'\202\323\344\223\002\310\001\022\220\001/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}Z3\0221/v1/registry/model_versions/{id.model_version_id}'
  _REGISTRYSERVICE.methods_by_name['CreateModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['CreateModelVersion']._serialized_options = b'\202\323\344\223\002\355\001\"z/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions:\rmodel_versionZ`\"O/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions:\rmodel_version'
  _REGISTRYSERVICE.methods_by_name['UpdateModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['UpdateModelVersion']._serialized_options = b'\202\323\344\223\002\320\0062\220\001/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}:\rmodel_versionZv2e/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}:\rmodel_versionZ\240\0012\232\001/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}/full_body:\001*Zt2o/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}/full_body:\001*Z\242\001\032\220\001/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}:\rmodel_versionZv\032e/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}:\rmodel_version'
  _REGISTRYSERVICE.methods_by_name['SetLockModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['SetLockModelVersion']._serialized_options = b'\202\323\344\223\002;\0326/v1/registry/model_versions/{id.model_version_id}/lock:\001*'
  _REGISTRYSERVICE.methods_by_name['DeleteModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['DeleteModelVersion']._serialized_options = b'\202\323\344\223\002\261\002*\220\001/v1/registry/workspaces/{id.model_id.named_id.workspace_name}/registered_models/{id.model_id.named_id.name}/model_versions/{id.model_version_id}Zg*e/v1/registry/registered_models/{id.model_id.registered_model_id}/model_versions/{id.model_version_id}Z3*1/v1/registry/model_versions/{id.model_version_id}'
  _REGISTRYSERVICE.methods_by_name['getUrlForArtifact']._options = None
  _REGISTRYSERVICE.methods_by_name['getUrlForArtifact']._serialized_options = b'\202\323\344\223\002E\"@/v1/registry/model_versions/{model_version_id}/getUrlForArtifact:\001*'
  _REGISTRYSERVICE.methods_by_name['commitArtifactPart']._options = None
  _REGISTRYSERVICE.methods_by_name['commitArtifactPart']._serialized_options = b'\202\323\344\223\002F\"A/v1/registry/model_versions/{model_version_id}/commitArtifactPart:\001*'
  _REGISTRYSERVICE.methods_by_name['getCommittedArtifactParts']._options = None
  _REGISTRYSERVICE.methods_by_name['getCommittedArtifactParts']._serialized_options = b'\202\323\344\223\002J\022H/v1/registry/model_versions/{model_version_id}/getCommittedArtifactParts'
  _REGISTRYSERVICE.methods_by_name['commitMultipartArtifact']._options = None
  _REGISTRYSERVICE.methods_by_name['commitMultipartArtifact']._serialized_options = b'\202\323\344\223\002K\"F/v1/registry/model_versions/{model_version_id}/commitMultipartArtifact:\001*'
  _REGISTRYSERVICE.methods_by_name['logDatasetsInModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['logDatasetsInModelVersion']._serialized_options = b'\202\323\344\223\002?\":/v1/registry/model_versions/{model_version_id}/logDatasets:\001*'
  _REGISTRYSERVICE.methods_by_name['logCodeBlobInModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['logCodeBlobInModelVersion']._serialized_options = b'\202\323\344\223\002M\"H/v1/registry/model_versions/{model_version_id}/logCodeBlobInModelVersion:\001*'
  _REGISTRYSERVICE.methods_by_name['logAttributesInModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['logAttributesInModelVersion']._serialized_options = b'\202\323\344\223\002A\"</v1/registry/model_versions/{model_version_id}/logAttributes:\001*'
  _REGISTRYSERVICE.methods_by_name['logDockerMetadataInModelVersion']._options = None
  _REGISTRYSERVICE.methods_by_name['logDockerMetadataInModelVersion']._serialized_options = b'\202\323\344\223\002E\"@/v1/registry/model_versions/{model_version_id}/logDockerMetadata:\001*'
  _REGISTRYSERVICE.methods_by_name['GetExternalDeployment']._options = None
  _REGISTRYSERVICE.methods_by_name['GetExternalDeployment']._serialized_options = b'\202\323\344\223\002]\022[/v1/registry/registered_models/model_versions/external_deployments/{external_deployment_id}'
  _REGISTRYSERVICE.methods_by_name['CreateExternalDeployment']._options = None
  _REGISTRYSERVICE.methods_by_name['CreateExternalDeployment']._serialized_options = b'\202\323\344\223\002G\"B/v1/registry/registered_models/model_versions/external_deployments:\001*'
  _REGISTRYSERVICE.methods_by_name['UpdateExternalDeployment']._options = None
  _REGISTRYSERVICE.methods_by_name['UpdateExternalDeployment']._serialized_options = b'\202\323\344\223\002G\032B/v1/registry/registered_models/model_versions/external_deployments:\001*'
  _REGISTRYSERVICE.methods_by_name['DeleteExternalDeployment']._options = None
  _REGISTRYSERVICE.methods_by_name['DeleteExternalDeployment']._serialized_options = b'\202\323\344\223\002]*[/v1/registry/registered_models/model_versions/external_deployments/{external_deployment_id}'
  _DATATYPEENUM._serialized_start=267
  _DATATYPEENUM._serialized_end=373
  _DATATYPEENUM_DATATYPE._serialized_start=283
  _DATATYPEENUM_DATATYPE._serialized_end=373
  _ACTIONTYPEENUM._serialized_start=376
  _ACTIONTYPEENUM._serialized_end=542
  _ACTIONTYPEENUM_ACTIONTYPE._serialized_start=395
  _ACTIONTYPEENUM_ACTIONTYPE._serialized_end=538
  _TASKTYPEENUM._serialized_start=545
  _TASKTYPEENUM._serialized_end=699
  _TASKTYPEENUM_TASKTYPE._serialized_start=562
  _TASKTYPEENUM_TASKTYPE._serialized_end=699
  _REGISTEREDMODEL._serialized_start=702
  _REGISTEREDMODEL._serialized_end=1446
  _FINDREGISTEREDMODELREQUEST._serialized_start=1449
  _FINDREGISTEREDMODELREQUEST._serialized_end=1750
  _FINDREGISTEREDMODELREQUEST_RESPONSE._serialized_start=1654
  _FINDREGISTEREDMODELREQUEST_RESPONSE._serialized_end=1750
  _GETREGISTEREDMODELREQUEST._serialized_start=1753
  _GETREGISTEREDMODELREQUEST._serialized_end=1916
  _GETREGISTEREDMODELREQUEST_RESPONSE._serialized_start=1844
  _GETREGISTEREDMODELREQUEST_RESPONSE._serialized_end=1916
  _GETREGISTEREDMODELCOUNTREQUEST._serialized_start=1918
  _GETREGISTEREDMODELCOUNTREQUEST._serialized_end=2014
  _GETREGISTEREDMODELCOUNTREQUEST_RESPONSE._serialized_start=1972
  _GETREGISTEREDMODELCOUNTREQUEST_RESPONSE._serialized_end=2014
  _REGISTEREDMODELNAMEDIDENTIFICATION._serialized_start=2016
  _REGISTEREDMODELNAMEDIDENTIFICATION._serialized_end=2090
  _REGISTEREDMODELIDENTIFICATION._serialized_start=2093
  _REGISTEREDMODELIDENTIFICATION._serialized_end=2226
  _SETREGISTEREDMODEL._serialized_start=2229
  _SETREGISTEREDMODEL._serialized_end=2496
  _SETREGISTEREDMODEL_RESPONSE._serialized_start=1844
  _SETREGISTEREDMODEL_RESPONSE._serialized_end=1916
  _DELETEREGISTEREDMODELREQUEST._serialized_start=2498
  _DELETEREGISTEREDMODELREQUEST._serialized_end=2602
  _DELETEREGISTEREDMODELREQUEST_RESPONSE._serialized_start=1654
  _DELETEREGISTEREDMODELREQUEST_RESPONSE._serialized_end=1664
  _MODELVERSIONLOCKLEVELENUM._serialized_start=2604
  _MODELVERSIONLOCKLEVELENUM._serialized_end=2703
  _MODELVERSIONLOCKLEVELENUM_MODELVERSIONLOCKLEVEL._serialized_start=2633
  _MODELVERSIONLOCKLEVELENUM_MODELVERSIONLOCKLEVEL._serialized_end=2703
  _MODELVERSION._serialized_start=2706
  _MODELVERSION._serialized_end=3871
  _MODELVERSION_CODEBLOBMAPENTRY._serialized_start=3772
  _MODELVERSION_CODEBLOBMAPENTRY._serialized_end=3861
  _DOCKERMETADATA._serialized_start=3873
  _DOCKERMETADATA._serialized_end=3954
  _SETLOCKMODELVERSIONREQUEST._serialized_start=3957
  _SETLOCKMODELVERSIONREQUEST._serialized_end=4144
  _SETLOCKMODELVERSIONREQUEST_RESPONSE._serialized_start=1654
  _SETLOCKMODELVERSIONREQUEST_RESPONSE._serialized_end=1664
  _MODELVERSIONIDENTIFICATION._serialized_start=4146
  _MODELVERSIONIDENTIFICATION._serialized_end=4268
  _GETMODELVERSIONREQUEST._serialized_start=4271
  _GETMODELVERSIONREQUEST._serialized_end=4422
  _GETMODELVERSIONREQUEST_RESPONSE._serialized_start=4356
  _GETMODELVERSIONREQUEST_RESPONSE._serialized_end=4422
  _FINDMODELVERSIONREQUEST._serialized_start=4425
  _FINDMODELVERSIONREQUEST._serialized_end=4755
  _FINDMODELVERSIONREQUEST_RESPONSE._serialized_start=4665
  _FINDMODELVERSIONREQUEST_RESPONSE._serialized_end=4755
  _SETMODELVERSION._serialized_start=4758
  _SETMODELVERSION._serialized_end=5007
  _SETMODELVERSION_RESPONSE._serialized_start=4356
  _SETMODELVERSION_RESPONSE._serialized_end=4422
  _DELETEMODELVERSIONREQUEST._serialized_start=5009
  _DELETEMODELVERSIONREQUEST._serialized_end=5107
  _DELETEMODELVERSIONREQUEST_RESPONSE._serialized_start=1654
  _DELETEMODELVERSIONREQUEST_RESPONSE._serialized_end=1664
  _GETURLFORARTIFACT._serialized_start=5110
  _GETURLFORARTIFACT._serialized_end=5453
  _GETURLFORARTIFACT_RESPONSE._serialized_start=5279
  _GETURLFORARTIFACT_RESPONSE._serialized_end=5453
  _GETURLFORARTIFACT_RESPONSE_FIELDSENTRY._serialized_start=5408
  _GETURLFORARTIFACT_RESPONSE_FIELDSENTRY._serialized_end=5453
  _COMMITARTIFACTPART._serialized_start=5455
  _COMMITARTIFACTPART._serialized_end=5580
  _COMMITARTIFACTPART_RESPONSE._serialized_start=1654
  _COMMITARTIFACTPART_RESPONSE._serialized_end=1664
  _GETCOMMITTEDARTIFACTPARTS._serialized_start=5583
  _GETCOMMITTEDARTIFACTPARTS._serialized_end=5716
  _GETCOMMITTEDARTIFACTPARTS_RESPONSE._serialized_start=5651
  _GETCOMMITTEDARTIFACTPARTS_RESPONSE._serialized_end=5716
  _COMMITMULTIPARTARTIFACT._serialized_start=5718
  _COMMITMULTIPARTARTIFACT._serialized_end=5794
  _COMMITMULTIPARTARTIFACT_RESPONSE._serialized_start=1654
  _COMMITMULTIPARTARTIFACT_RESPONSE._serialized_end=1664
  _LOGDATASETSINMODELVERSION._serialized_start=5796
  _LOGDATASETSINMODELVERSION._serialized_end=5906
  _LOGDATASETSINMODELVERSION_RESPONSE._serialized_start=1654
  _LOGDATASETSINMODELVERSION_RESPONSE._serialized_end=1664
  _LOGCODEBLOBINMODELVERSION._serialized_start=5909
  _LOGCODEBLOBINMODELVERSION._serialized_end=6151
  _LOGCODEBLOBINMODELVERSION_CODEBLOBMAPENTRY._serialized_start=3772
  _LOGCODEBLOBINMODELVERSION_CODEBLOBMAPENTRY._serialized_end=3861
  _LOGCODEBLOBINMODELVERSION_RESPONSE._serialized_start=1654
  _LOGCODEBLOBINMODELVERSION_RESPONSE._serialized_end=1664
  _LOGATTRIBUTESINMODELVERSION._serialized_start=6153
  _LOGATTRIBUTESINMODELVERSION._serialized_end=6267
  _LOGATTRIBUTESINMODELVERSION_RESPONSE._serialized_start=1654
  _LOGATTRIBUTESINMODELVERSION_RESPONSE._serialized_end=1664
  _LOGDOCKERMETADATAINMODELVERSION._serialized_start=6270
  _LOGDOCKERMETADATAINMODELVERSION._serialized_end=6401
  _LOGDOCKERMETADATAINMODELVERSION_RESPONSE._serialized_start=1654
  _LOGDOCKERMETADATAINMODELVERSION_RESPONSE._serialized_end=1664
  _EXTERNALDEPLOYMENT._serialized_start=6404
  _EXTERNALDEPLOYMENT._serialized_end=6578
  _EXTERNALDEPLOYMENTREQUEST._serialized_start=6581
  _EXTERNALDEPLOYMENTREQUEST._serialized_end=6720
  _EXTERNALDEPLOYMENTREQUEST_RESPONSE._serialized_start=6642
  _EXTERNALDEPLOYMENTREQUEST_RESPONSE._serialized_end=6720
  _EMPTY._serialized_start=6722
  _EMPTY._serialized_end=6729
  _REGISTRYSERVICE._serialized_start=6732
  _REGISTRYSERVICE._serialized_end=13836
# @@protoc_insertion_point(module_scope)
