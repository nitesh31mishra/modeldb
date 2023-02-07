# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/Workspace.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import CommonService_pb2 as common_dot_CommonService__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13uac/Workspace.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x1a\x63ommon/CommonService.proto\x1a\x14uac/UACService.proto\"\x1e\n\x10GetWorkspaceById\x12\n\n\x02id\x18\x01 \x01(\x04\"\"\n\x12GetWorkspaceByName\x12\x0c\n\x04name\x18\x01 \x01(\t\"n\n\x16GetWorkspaceByLegacyId\x12\n\n\x02id\x18\x01 \x01(\t\x12H\n\x0eworkspace_type\x18\x02 \x01(\x0e\x32\x30.ai.verta.common.WorkspaceTypeEnum.WorkspaceType\"\xe3\x01\n\tWorkspace\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\x07user_id\x18\x02 \x01(\tH\x00\x12\x10\n\x06org_id\x18\x03 \x01(\tH\x00\x12\x12\n\x08username\x18\x04 \x01(\tH\x01\x12\x12\n\x08org_name\x18\x05 \x01(\tH\x01\x12S\n\x14\x63ontainer_registries\x18\x06 \x03(\x0b\x32\x35.ai.verta.uac.WorkspaceContainerRegistryConfiguration\x12\x11\n\tnamespace\x18\x07 \x01(\tB\r\n\x0binternal_idB\x06\n\x04name\"\x7f\n\'WorkspaceContainerRegistryConfiguration\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x12\n\nsecret_key\x18\x04 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x05 \x01(\x04\"G\n\x14GetVisibleWorkspaces\x12/\n\npagination\x18\x01 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\"O\n\nWorkspaces\x12*\n\tworkspace\x18\x01 \x03(\x0b\x32\x17.ai.verta.uac.Workspace\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\x32\xa7\x07\n\x10WorkspaceService\x12s\n\x10getWorkspaceById\x12\x1e.ai.verta.uac.GetWorkspaceById\x1a\x17.ai.verta.uac.Workspace\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/workspace/getWorkspaceById\x12y\n\x12getWorkspaceByName\x12 .ai.verta.uac.GetWorkspaceByName\x1a\x17.ai.verta.uac.Workspace\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/workspace/getWorkspaceByName\x12\x85\x01\n\x16getWorkspaceByLegacyId\x12$.ai.verta.uac.GetWorkspaceByLegacyId\x1a\x17.ai.verta.uac.Workspace\",\x82\xd3\xe4\x93\x02&\x12$/v1/workspace/getWorkspaceByLegacyId\x12\x80\x01\n\x14getVisibleWorkspaces\x12\".ai.verta.uac.GetVisibleWorkspaces\x1a\x18.ai.verta.uac.Workspaces\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/workspace/getVisibleWorkspaces\x12\xe3\x01\n,createOrUpdateContainerRegistryConfiguration\x12\x35.ai.verta.uac.WorkspaceContainerRegistryConfiguration\x1a\x35.ai.verta.uac.WorkspaceContainerRegistryConfiguration\"E\x82\xd3\xe4\x93\x02?\":/v1/workspace/createOrUpdateContainerRegistryConfiguration:\x01*\x12\xb1\x01\n$deleteContainerRegistryConfiguration\x12\x35.ai.verta.uac.WorkspaceContainerRegistryConfiguration\x1a\x13.ai.verta.uac.Empty\"=\x82\xd3\xe4\x93\x02\x37\"2/v1/workspace/deleteContainerRegistryConfiguration:\x01*B>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uac.Workspace_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac'
  _WORKSPACESERVICE.methods_by_name['getWorkspaceById']._options = None
  _WORKSPACESERVICE.methods_by_name['getWorkspaceById']._serialized_options = b'\202\323\344\223\002 \022\036/v1/workspace/getWorkspaceById'
  _WORKSPACESERVICE.methods_by_name['getWorkspaceByName']._options = None
  _WORKSPACESERVICE.methods_by_name['getWorkspaceByName']._serialized_options = b'\202\323\344\223\002\"\022 /v1/workspace/getWorkspaceByName'
  _WORKSPACESERVICE.methods_by_name['getWorkspaceByLegacyId']._options = None
  _WORKSPACESERVICE.methods_by_name['getWorkspaceByLegacyId']._serialized_options = b'\202\323\344\223\002&\022$/v1/workspace/getWorkspaceByLegacyId'
  _WORKSPACESERVICE.methods_by_name['getVisibleWorkspaces']._options = None
  _WORKSPACESERVICE.methods_by_name['getVisibleWorkspaces']._serialized_options = b'\202\323\344\223\002$\022\"/v1/workspace/getVisibleWorkspaces'
  _WORKSPACESERVICE.methods_by_name['createOrUpdateContainerRegistryConfiguration']._options = None
  _WORKSPACESERVICE.methods_by_name['createOrUpdateContainerRegistryConfiguration']._serialized_options = b'\202\323\344\223\002?\":/v1/workspace/createOrUpdateContainerRegistryConfiguration:\001*'
  _WORKSPACESERVICE.methods_by_name['deleteContainerRegistryConfiguration']._options = None
  _WORKSPACESERVICE.methods_by_name['deleteContainerRegistryConfiguration']._serialized_options = b'\202\323\344\223\0027\"2/v1/workspace/deleteContainerRegistryConfiguration:\001*'
  _GETWORKSPACEBYID._serialized_start=117
  _GETWORKSPACEBYID._serialized_end=147
  _GETWORKSPACEBYNAME._serialized_start=149
  _GETWORKSPACEBYNAME._serialized_end=183
  _GETWORKSPACEBYLEGACYID._serialized_start=185
  _GETWORKSPACEBYLEGACYID._serialized_end=295
  _WORKSPACE._serialized_start=298
  _WORKSPACE._serialized_end=525
  _WORKSPACECONTAINERREGISTRYCONFIGURATION._serialized_start=527
  _WORKSPACECONTAINERREGISTRYCONFIGURATION._serialized_end=654
  _GETVISIBLEWORKSPACES._serialized_start=656
  _GETVISIBLEWORKSPACES._serialized_end=727
  _WORKSPACES._serialized_start=729
  _WORKSPACES._serialized_end=808
  _WORKSPACESERVICE._serialized_start=811
  _WORKSPACESERVICE._serialized_end=1746
# @@protoc_insertion_point(module_scope)
