# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/RoleService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import CommonService_pb2 as common_dot_CommonService__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15uac/RoleService.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x1a\x63ommon/CommonService.proto\"\xaf\x01\n\x0bServiceEnum\"\x9f\x01\n\x07Service\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x10\n\x0cROLE_SERVICE\x10\x02\x12\x11\n\rAUTHZ_SERVICE\x10\x03\x12\x13\n\x0fMODELDB_SERVICE\x10\x04\x12\x16\n\x12\x44\x45PLOYMENT_SERVICE\x10\x05\x12\x14\n\x10REGISTRY_SERVICE\x10\x06\x12\x16\n\x12MONITORING_SERVICE\x10\x07\"\x8a\x01\n\x0eRoleActionEnum\"x\n\x12RoleServiceActions\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\r\n\tGET_BY_ID\x10\x02\x12\x0f\n\x0bGET_BY_NAME\x10\x03\x12\n\n\x06\x43REATE\x10\x04\x12\n\n\x06UPDATE\x10\x05\x12\x08\n\x04LIST\x10\x06\x12\n\n\x06\x44\x45LETE\x10\x07\"\xf9\x01\n\x0f\x41uthzActionEnum\"\xe5\x01\n\x13\x41uthzServiceActions\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x0e\n\nIS_ALLOWED\x10\x02\x12\x07\n\x03GET\x10\x03\x12\n\n\x06\x43REATE\x10\x04\x12\x08\n\x04READ\x10\x05\x12\n\n\x06UPDATE\x10\x06\x12\n\n\x06\x44\x45LETE\x10\x07\x12\x10\n\x0cREAD_SECRETS\x10\x08\x12\x1a\n\x16\x43REATE_SERVICE_ACCOUNT\x10\t\x12\x1d\n\x19\x43REATE_CONTAINER_REGISTRY\x10\n\x12\x12\n\x0e\x43REATE_WEBHOOK\x10\x0b\x12\x10\n\x0c\x43REATE_GROUP\x10\x0c\"\xe9\x02\n\x11ModelDBActionEnum\"\xd3\x02\n\x15ModelDBServiceActions\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\x08\n\x04READ\x10\x03\x12\n\n\x06UPDATE\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\n\n\x06\x44\x45PLOY\x10\x06\x12\x0f\n\x0bPUBLIC_READ\x10\x07\x12\x16\n\x12UPDATE_PERMISSIONS\x10\x08\x12\x08\n\x04LOCK\x10\t\x12\n\n\x06UNLOCK\x10\n\x12\x11\n\rUPDATE_REDACT\x10\x0b\x12\x0b\n\x07\x41LERTER\x10\x0c\x12\x0b\n\x07PREDICT\x10\r\x12\x0b\n\x07\x43ONTROL\x10\x0e\x12\x0e\n\nIS_ALLOWED\x10\x0f\x12\x07\n\x03GET\x10\x10\x12\x10\n\x0cREAD_SECRETS\x10\x11\x12\x1a\n\x16\x43REATE_SERVICE_ACCOUNT\x10\x12\x12\x1d\n\x19\x43REATE_CONTAINER_REGISTRY\x10\x13\x12\x0b\n\x07PROMOTE\x10\x14\"\xa9\x01\n\x14\x44\x65ploymentActionEnum\"\x90\x01\n\x18\x44\x65ploymentServiceActions\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\x08\n\x04READ\x10\x03\x12\n\n\x06UPDATE\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\x16\n\x12UPDATE_PERMISSIONS\x10\x08\x12\x0b\n\x07PREDICT\x10\t\x12\x0b\n\x07\x43ONTROL\x10\n\"\xa4\x03\n\x06\x41\x63tion\x12\x32\n\x07service\x18\x01 \x01(\x0e\x32!.ai.verta.uac.ServiceEnum.Service\x12N\n\x13role_service_action\x18\x02 \x01(\x0e\x32/.ai.verta.uac.RoleActionEnum.RoleServiceActionsH\x00\x12Q\n\x14\x61uthz_service_action\x18\x03 \x01(\x0e\x32\x31.ai.verta.uac.AuthzActionEnum.AuthzServiceActionsH\x00\x12W\n\x16modeldb_service_action\x18\x04 \x01(\x0e\x32\x35.ai.verta.uac.ModelDBActionEnum.ModelDBServiceActionsH\x00\x12`\n\x19\x64\x65ployment_service_action\x18\x05 \x01(\x0e\x32;.ai.verta.uac.DeploymentActionEnum.DeploymentServiceActionsH\x00\x42\x08\n\x06\x61\x63tion\"`\n\x10RoleResourceEnum\"L\n\x18RoleServiceResourceTypes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x08\n\x04ROLE\x10\x02\x12\x10\n\x0cROLE_BINDING\x10\x03\"\xb5\x02\n\x11\x41uthzResourceEnum\"\x9f\x02\n\x19\x41uthzServiceResourceTypes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x10\n\x0cORGANIZATION\x10\x02\x12\x08\n\x04TEAM\x10\x03\x12\r\n\tWORKSPACE\x10\x04\x12\x08\n\x04USER\x10\x05\x12\x13\n\x0fSERVICE_ACCOUNT\x10\x06\x12$\n CONTAINER_REGISTRY_CONFIGURATION\x10\x07\x12\t\n\x05\x45VENT\x10\x08\x12\x0b\n\x07WEBHOOK\x10\t\x12\x10\n\x0cSYSTEM_ADMIN\x10\n\x12\x16\n\x12PYPI_CONFIGURATION\x10\x0b\x12\x17\n\x13KAFKA_CONFIGURATION\x10\x0c\x12\x16\n\x12SCIM_CONFIGURATION\x10\r\x12\t\n\x05GROUP\x10\x0e\"i\n\x16\x44\x65ploymentResourceEnum\"O\n\x1e\x44\x65ploymentServiceResourceTypes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x0c\n\x08\x45NDPOINT\x10\x02\x12\t\n\x05\x42UILD\x10\x03\"\xb7\x03\n\x0cResourceType\x12]\n\x1arole_service_resource_type\x18\x01 \x01(\x0e\x32\x37.ai.verta.uac.RoleResourceEnum.RoleServiceResourceTypesH\x00\x12`\n\x1b\x61uthz_service_resource_type\x18\x02 \x01(\x0e\x32\x39.ai.verta.uac.AuthzResourceEnum.AuthzServiceResourceTypesH\x00\x12i\n\x1dmodeldb_service_resource_type\x18\x03 \x01(\x0e\x32@.ai.verta.common.ModelDBResourceEnum.ModelDBServiceResourceTypesH\x00\x12o\n deployment_service_resource_type\x18\x04 \x01(\x0e\x32\x43.ai.verta.uac.DeploymentResourceEnum.DeploymentServiceResourceTypesH\x00\x42\n\n\x08resource\"\xa2\x01\n\tResources\x12\x32\n\x07service\x18\x01 \x01(\x0e\x32!.ai.verta.uac.ServiceEnum.Service\x12\x14\n\x0cresource_ids\x18\x02 \x03(\t\x12\x18\n\x10\x61ll_resource_ids\x18\x03 \x01(\x08\x12\x31\n\rresource_type\x18\x06 \x01(\x0b\x32\x1a.ai.verta.uac.ResourceType\",\n\tRoleScope\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x0f\n\x07team_id\x18\x02 \x01(\t\"h\n\x13ResourceActionGroup\x12*\n\tresources\x18\x01 \x03(\x0b\x32\x17.ai.verta.uac.Resources\x12%\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x14.ai.verta.uac.Action\"\x8b\x01\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x05scope\x18\x03 \x01(\x0b\x32\x17.ai.verta.uac.RoleScope\x12\x41\n\x16resource_action_groups\x18\x04 \x03(\x0b\x32!.ai.verta.uac.ResourceActionGroup\"?\n\x08\x45ntities\x12\x10\n\x08user_ids\x18\x01 \x03(\t\x12\x0f\n\x07org_ids\x18\x02 \x03(\t\x12\x10\n\x08team_ids\x18\x03 \x03(\t\"\xd9\x01\n\x0bRoleBinding\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x05scope\x18\x03 \x01(\x0b\x32\x17.ai.verta.uac.RoleScope\x12(\n\x08\x65ntities\x18\x05 \x03(\x0b\x32\x16.ai.verta.uac.Entities\x12*\n\tresources\x18\x06 \x03(\x0b\x32\x17.ai.verta.uac.Resources\x12\x0f\n\x07role_id\x18\x07 \x01(\t\x12\x11\n\trole_name\x18\t \x01(\t\x12\x0e\n\x06public\x18\x08 \x01(\x08\"G\n\x0bGetRoleById\x12\n\n\x02id\x18\x01 \x01(\t\x1a,\n\x08Response\x12 \n\x04role\x18\x01 \x01(\x0b\x32\x12.ai.verta.uac.Role\"s\n\rGetRoleByName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05scope\x18\x02 \x01(\x0b\x32\x17.ai.verta.uac.RoleScope\x1a,\n\x08Response\x12 \n\x04role\x18\x01 \x01(\x0b\x32\x12.ai.verta.uac.Role\"\xaa\x01\n\tListRoles\x12/\n\npagination\x18\x01 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x12&\n\x05scope\x18\x02 \x01(\x0b\x32\x17.ai.verta.uac.RoleScope\x1a\x44\n\x08Response\x12!\n\x05roles\x18\x01 \x03(\x0b\x32\x12.ai.verta.uac.Role\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"Y\n\x07SetRole\x12 \n\x04role\x18\x01 \x01(\x0b\x32\x12.ai.verta.uac.Role\x1a,\n\x08Response\x12 \n\x04role\x18\x01 \x01(\x0b\x32\x12.ai.verta.uac.Role\"4\n\nDeleteRole\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"]\n\x12GetRoleBindingById\x12\n\n\x02id\x18\x01 \x01(\t\x1a;\n\x08Response\x12/\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x19.ai.verta.uac.RoleBinding\"\x89\x01\n\x14GetRoleBindingByName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05scope\x18\x02 \x01(\x0b\x32\x17.ai.verta.uac.RoleScope\x1a;\n\x08Response\x12/\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x19.ai.verta.uac.RoleBinding\"\xd3\x01\n\x10ListRoleBindings\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12&\n\x05scope\x18\x02 \x01(\x0b\x32\x17.ai.verta.uac.RoleScope\x12/\n\npagination\x18\x03 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x1aS\n\x08Response\x12\x30\n\rrole_bindings\x18\x01 \x03(\x0b\x32\x19.ai.verta.uac.RoleBinding\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"~\n\x0eSetRoleBinding\x12/\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x19.ai.verta.uac.RoleBinding\x1a;\n\x08Response\x12/\n\x0crole_binding\x18\x01 \x01(\x0b\x32\x19.ai.verta.uac.RoleBinding\";\n\x11\x44\x65leteRoleBinding\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"J\n\x12\x44\x65leteRoleBindings\x12\x18\n\x10roleBindingNames\x18\x01 \x03(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"v\n\x0fRemoveResources\x12\x14\n\x0cresource_ids\x18\x01 \x03(\t\x12\x31\n\rresource_type\x18\x02 \x01(\x0b\x32\x1a.ai.verta.uac.ResourceType\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xc9\x0b\n\x0bRoleService\x12j\n\x0bgetRoleById\x12\x19.ai.verta.uac.GetRoleById\x1a\".ai.verta.uac.GetRoleById.Response\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/role/getRoleById\x12r\n\rgetRoleByName\x12\x1b.ai.verta.uac.GetRoleByName\x1a$.ai.verta.uac.GetRoleByName.Response\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/role/getRoleByName\x12\x62\n\tlistRoles\x12\x17.ai.verta.uac.ListRoles\x1a .ai.verta.uac.ListRoles.Response\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/role/listRoles\x12]\n\x07setRole\x12\x15.ai.verta.uac.SetRole\x1a\x1e.ai.verta.uac.SetRole.Response\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/role/setRole:\x01*\x12i\n\ndeleteRole\x12\x18.ai.verta.uac.DeleteRole\x1a!.ai.verta.uac.DeleteRole.Response\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/role/deleteRole:\x01*\x12\x86\x01\n\x12getBindingRoleById\x12 .ai.verta.uac.GetRoleBindingById\x1a).ai.verta.uac.GetRoleBindingById.Response\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/role/getRoleBindingById\x12\x8e\x01\n\x14getRoleBindingByName\x12\".ai.verta.uac.GetRoleBindingByName\x1a+.ai.verta.uac.GetRoleBindingByName.Response\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/role/getRoleBindingByName\x12~\n\x10listRoleBindings\x12\x1e.ai.verta.uac.ListRoleBindings\x1a\'.ai.verta.uac.ListRoleBindings.Response\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/role/listRoleBindings\x12y\n\x0esetRoleBinding\x12\x1c.ai.verta.uac.SetRoleBinding\x1a%.ai.verta.uac.SetRoleBinding.Response\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/role/setRoleBinding:\x01*\x12\x85\x01\n\x11\x64\x65leteRoleBinding\x12\x1f.ai.verta.uac.DeleteRoleBinding\x1a(.ai.verta.uac.DeleteRoleBinding.Response\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/role/deleteRoleBinding:\x01*\x12\x89\x01\n\x12\x64\x65leteRoleBindings\x12 .ai.verta.uac.DeleteRoleBindings\x1a).ai.verta.uac.DeleteRoleBindings.Response\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/role/deleteRoleBindings:\x01*\x12\x82\x01\n\x0fremoveResources\x12\x1d.ai.verta.uac.RemoveResources\x1a&.ai.verta.uac.RemoveResources.Response\"(\x82\xd3\xe4\x93\x02\"* /v1/collaborator/removeResourcesB>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uac.RoleService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac'
  _ROLESERVICE.methods_by_name['getRoleById']._options = None
  _ROLESERVICE.methods_by_name['getRoleById']._serialized_options = b'\202\323\344\223\002\026\022\024/v1/role/getRoleById'
  _ROLESERVICE.methods_by_name['getRoleByName']._options = None
  _ROLESERVICE.methods_by_name['getRoleByName']._serialized_options = b'\202\323\344\223\002\030\022\026/v1/role/getRoleByName'
  _ROLESERVICE.methods_by_name['listRoles']._options = None
  _ROLESERVICE.methods_by_name['listRoles']._serialized_options = b'\202\323\344\223\002\024\022\022/v1/role/listRoles'
  _ROLESERVICE.methods_by_name['setRole']._options = None
  _ROLESERVICE.methods_by_name['setRole']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/role/setRole:\001*'
  _ROLESERVICE.methods_by_name['deleteRole']._options = None
  _ROLESERVICE.methods_by_name['deleteRole']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/role/deleteRole:\001*'
  _ROLESERVICE.methods_by_name['getBindingRoleById']._options = None
  _ROLESERVICE.methods_by_name['getBindingRoleById']._serialized_options = b'\202\323\344\223\002\035\022\033/v1/role/getRoleBindingById'
  _ROLESERVICE.methods_by_name['getRoleBindingByName']._options = None
  _ROLESERVICE.methods_by_name['getRoleBindingByName']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/role/getRoleBindingByName'
  _ROLESERVICE.methods_by_name['listRoleBindings']._options = None
  _ROLESERVICE.methods_by_name['listRoleBindings']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/role/listRoleBindings'
  _ROLESERVICE.methods_by_name['setRoleBinding']._options = None
  _ROLESERVICE.methods_by_name['setRoleBinding']._serialized_options = b'\202\323\344\223\002\034\"\027/v1/role/setRoleBinding:\001*'
  _ROLESERVICE.methods_by_name['deleteRoleBinding']._options = None
  _ROLESERVICE.methods_by_name['deleteRoleBinding']._serialized_options = b'\202\323\344\223\002\037\"\032/v1/role/deleteRoleBinding:\001*'
  _ROLESERVICE.methods_by_name['deleteRoleBindings']._options = None
  _ROLESERVICE.methods_by_name['deleteRoleBindings']._serialized_options = b'\202\323\344\223\002 \"\033/v1/role/deleteRoleBindings:\001*'
  _ROLESERVICE.methods_by_name['removeResources']._options = None
  _ROLESERVICE.methods_by_name['removeResources']._serialized_options = b'\202\323\344\223\002\"* /v1/collaborator/removeResources'
  _SERVICEENUM._serialized_start=98
  _SERVICEENUM._serialized_end=273
  _SERVICEENUM_SERVICE._serialized_start=114
  _SERVICEENUM_SERVICE._serialized_end=273
  _ROLEACTIONENUM._serialized_start=276
  _ROLEACTIONENUM._serialized_end=414
  _ROLEACTIONENUM_ROLESERVICEACTIONS._serialized_start=294
  _ROLEACTIONENUM_ROLESERVICEACTIONS._serialized_end=414
  _AUTHZACTIONENUM._serialized_start=417
  _AUTHZACTIONENUM._serialized_end=666
  _AUTHZACTIONENUM_AUTHZSERVICEACTIONS._serialized_start=437
  _AUTHZACTIONENUM_AUTHZSERVICEACTIONS._serialized_end=666
  _MODELDBACTIONENUM._serialized_start=669
  _MODELDBACTIONENUM._serialized_end=1030
  _MODELDBACTIONENUM_MODELDBSERVICEACTIONS._serialized_start=691
  _MODELDBACTIONENUM_MODELDBSERVICEACTIONS._serialized_end=1030
  _DEPLOYMENTACTIONENUM._serialized_start=1033
  _DEPLOYMENTACTIONENUM._serialized_end=1202
  _DEPLOYMENTACTIONENUM_DEPLOYMENTSERVICEACTIONS._serialized_start=1058
  _DEPLOYMENTACTIONENUM_DEPLOYMENTSERVICEACTIONS._serialized_end=1202
  _ACTION._serialized_start=1205
  _ACTION._serialized_end=1625
  _ROLERESOURCEENUM._serialized_start=1627
  _ROLERESOURCEENUM._serialized_end=1723
  _ROLERESOURCEENUM_ROLESERVICERESOURCETYPES._serialized_start=1647
  _ROLERESOURCEENUM_ROLESERVICERESOURCETYPES._serialized_end=1723
  _AUTHZRESOURCEENUM._serialized_start=1726
  _AUTHZRESOURCEENUM._serialized_end=2035
  _AUTHZRESOURCEENUM_AUTHZSERVICERESOURCETYPES._serialized_start=1748
  _AUTHZRESOURCEENUM_AUTHZSERVICERESOURCETYPES._serialized_end=2035
  _DEPLOYMENTRESOURCEENUM._serialized_start=2037
  _DEPLOYMENTRESOURCEENUM._serialized_end=2142
  _DEPLOYMENTRESOURCEENUM_DEPLOYMENTSERVICERESOURCETYPES._serialized_start=2063
  _DEPLOYMENTRESOURCEENUM_DEPLOYMENTSERVICERESOURCETYPES._serialized_end=2142
  _RESOURCETYPE._serialized_start=2145
  _RESOURCETYPE._serialized_end=2584
  _RESOURCES._serialized_start=2587
  _RESOURCES._serialized_end=2749
  _ROLESCOPE._serialized_start=2751
  _ROLESCOPE._serialized_end=2795
  _RESOURCEACTIONGROUP._serialized_start=2797
  _RESOURCEACTIONGROUP._serialized_end=2901
  _ROLE._serialized_start=2904
  _ROLE._serialized_end=3043
  _ENTITIES._serialized_start=3045
  _ENTITIES._serialized_end=3108
  _ROLEBINDING._serialized_start=3111
  _ROLEBINDING._serialized_end=3328
  _GETROLEBYID._serialized_start=3330
  _GETROLEBYID._serialized_end=3401
  _GETROLEBYID_RESPONSE._serialized_start=3357
  _GETROLEBYID_RESPONSE._serialized_end=3401
  _GETROLEBYNAME._serialized_start=3403
  _GETROLEBYNAME._serialized_end=3518
  _GETROLEBYNAME_RESPONSE._serialized_start=3357
  _GETROLEBYNAME_RESPONSE._serialized_end=3401
  _LISTROLES._serialized_start=3521
  _LISTROLES._serialized_end=3691
  _LISTROLES_RESPONSE._serialized_start=3623
  _LISTROLES_RESPONSE._serialized_end=3691
  _SETROLE._serialized_start=3693
  _SETROLE._serialized_end=3782
  _SETROLE_RESPONSE._serialized_start=3357
  _SETROLE_RESPONSE._serialized_end=3401
  _DELETEROLE._serialized_start=3784
  _DELETEROLE._serialized_end=3836
  _DELETEROLE_RESPONSE._serialized_start=3810
  _DELETEROLE_RESPONSE._serialized_end=3836
  _GETROLEBINDINGBYID._serialized_start=3838
  _GETROLEBINDINGBYID._serialized_end=3931
  _GETROLEBINDINGBYID_RESPONSE._serialized_start=3872
  _GETROLEBINDINGBYID_RESPONSE._serialized_end=3931
  _GETROLEBINDINGBYNAME._serialized_start=3934
  _GETROLEBINDINGBYNAME._serialized_end=4071
  _GETROLEBINDINGBYNAME_RESPONSE._serialized_start=3872
  _GETROLEBINDINGBYNAME_RESPONSE._serialized_end=3931
  _LISTROLEBINDINGS._serialized_start=4074
  _LISTROLEBINDINGS._serialized_end=4285
  _LISTROLEBINDINGS_RESPONSE._serialized_start=4202
  _LISTROLEBINDINGS_RESPONSE._serialized_end=4285
  _SETROLEBINDING._serialized_start=4287
  _SETROLEBINDING._serialized_end=4413
  _SETROLEBINDING_RESPONSE._serialized_start=3872
  _SETROLEBINDING_RESPONSE._serialized_end=3931
  _DELETEROLEBINDING._serialized_start=4415
  _DELETEROLEBINDING._serialized_end=4474
  _DELETEROLEBINDING_RESPONSE._serialized_start=3810
  _DELETEROLEBINDING_RESPONSE._serialized_end=3836
  _DELETEROLEBINDINGS._serialized_start=4476
  _DELETEROLEBINDINGS._serialized_end=4550
  _DELETEROLEBINDINGS_RESPONSE._serialized_start=3810
  _DELETEROLEBINDINGS_RESPONSE._serialized_end=3836
  _REMOVERESOURCES._serialized_start=4552
  _REMOVERESOURCES._serialized_end=4670
  _REMOVERESOURCES_RESPONSE._serialized_start=3810
  _REMOVERESOURCES_RESPONSE._serialized_end=3836
  _ROLESERVICE._serialized_start=4673
  _ROLESERVICE._serialized_end=6154
# @@protoc_insertion_point(module_scope)
