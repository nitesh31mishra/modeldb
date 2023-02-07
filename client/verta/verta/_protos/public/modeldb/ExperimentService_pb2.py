# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modeldb/ExperimentService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import CommonService_pb2 as common_dot_CommonService__pb2
from ..modeldb import CommonService_pb2 as modeldb_dot_CommonService__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmodeldb/ExperimentService.proto\x12\x10\x61i.verta.modeldb\x1a\x1a\x63ommon/CommonService.proto\x1a\x1bmodeldb/CommonService.proto\x1a\x1cgoogle/api/annotations.proto\"\xa4\x03\n\nExperiment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x61te_created\x18\x05 \x01(\x03\x12\x14\n\x0c\x64\x61te_updated\x18\x06 \x01(\x03\x12-\n\nattributes\x18\x14 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x12\x0c\n\x04tags\x18\x15 \x03(\t\x12\r\n\x05owner\x18\x16 \x01(\t\x12\x12\n\x08owner_id\x18\x1a \x01(\x04H\x00\x12\x32\n\x0egroup_owner_id\x18\x1b \x01(\x0b\x32\x18.ai.verta.common.GroupIdH\x00\x12;\n\x15\x63ode_version_snapshot\x18\x17 \x01(\x0b\x32\x1c.ai.verta.common.CodeVersion\x12,\n\tartifacts\x18\x18 \x03(\x0b\x32\x19.ai.verta.common.Artifact\x12\x16\n\x0eversion_number\x18\x19 \x01(\x04\x42\x10\n\x0eowner_tracking\"\xd1\x01\n\x17GetExperimentsInProject\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\x12\x12\n\npage_limit\x18\x03 \x01(\x05\x12\x11\n\tascending\x18\x04 \x01(\x08\x12\x10\n\x08sort_key\x18\x05 \x01(\t\x1aT\n\x08Response\x12\x31\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32\x1c.ai.verta.modeldb.Experiment\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"]\n\x11GetExperimentById\x12\n\n\x02id\x18\x01 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"u\n\x13GetExperimentByName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"\x9e\x02\n\x10\x43reateExperiment\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x61te_created\x18\x04 \x01(\x03\x12\x14\n\x0c\x64\x61te_updated\x18\x05 \x01(\x03\x12-\n\nattributes\x18\x14 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x12\x0c\n\x04tags\x18\x15 \x03(\t\x12,\n\tartifacts\x18\x16 \x03(\x0b\x32\x19.ai.verta.common.Artifact\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\":\n\x10\x44\x65leteExperiment\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x90\x01\n!UpdateExperimentNameOrDescription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"n\n\x14UpdateExperimentName\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"|\n\x1bUpdateExperimentDescription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"k\n\x11\x41\x64\x64\x45xperimentTags\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"\x82\x01\n\x14\x44\x65leteExperimentTags\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x12\n\ndelete_all\x18\x03 \x01(\x08\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"i\n\x10\x41\x64\x64\x45xperimentTag\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"l\n\x13\x44\x65leteExperimentTag\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"\x92\x01\n\x17\x41\x64\x64\x45xperimentAttributes\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\nattributes\x18\x02 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"\x92\x01\n\x1a\x44\x65leteExperimentAttributes\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0e\x61ttribute_keys\x18\x02 \x03(\t\x12\x12\n\ndelete_all\x18\x03 \x01(\x08\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"\x98\x01\n\x18LogExperimentCodeVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x0c\x63ode_version\x18\x02 \x01(\x0b\x32\x1c.ai.verta.common.CodeVersion\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"f\n\x18GetExperimentCodeVersion\x12\n\n\x02id\x18\x01 \x01(\t\x1a>\n\x08Response\x12\x32\n\x0c\x63ode_version\x18\x01 \x01(\x0b\x32\x1c.ai.verta.common.CodeVersion\"\xbf\x02\n\x0f\x46indExperiments\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xperiment_ids\x18\x02 \x03(\t\x12\x32\n\npredicates\x18\x04 \x03(\x0b\x32\x1e.ai.verta.common.KeyValueQuery\x12\x10\n\x08ids_only\x18\x05 \x01(\x08\x12\x13\n\x0bpage_number\x18\x06 \x01(\x05\x12\x12\n\npage_limit\x18\x07 \x01(\x05\x12\x11\n\tascending\x18\t \x01(\x08\x12\x10\n\x08sort_key\x18\n \x01(\t\x12\x16\n\x0eworkspace_name\x18\x0b \x01(\t\x1aT\n\x08Response\x12\x31\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32\x1c.ai.verta.modeldb.Experiment\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\"\x90\x01\n\x16LogExperimentArtifacts\x12\n\n\x02id\x18\x01 \x01(\t\x12,\n\tartifacts\x18\x02 \x03(\x0b\x32\x19.ai.verta.common.Artifact\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"q\n\x18\x44\x65leteExperimentArtifact\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x1a<\n\x08Response\x12\x30\n\nexperiment\x18\x01 \x01(\x0b\x32\x1c.ai.verta.modeldb.Experiment\"<\n\x11\x44\x65leteExperiments\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xf9\x1e\n\x11\x45xperimentService\x12\x8f\x01\n\x10\x63reateExperiment\x12\".ai.verta.modeldb.CreateExperiment\x1a+.ai.verta.modeldb.CreateExperiment.Response\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/experiment/createExperiment:\x01*\x12\xd3\x01\n!updateExperimentNameOrDescription\x12\x33.ai.verta.modeldb.UpdateExperimentNameOrDescription\x1a<.ai.verta.modeldb.UpdateExperimentNameOrDescription.Response\";\x82\xd3\xe4\x93\x02\x35\"0/v1/experiment/updateExperimentNameOrDescription:\x01*\x12\x9f\x01\n\x14updateExperimentName\x12&.ai.verta.modeldb.UpdateExperimentName\x1a/.ai.verta.modeldb.UpdateExperimentName.Response\".\x82\xd3\xe4\x93\x02(\"#/v1/experiment/updateExperimentName:\x01*\x12\xbb\x01\n\x1bupdateExperimentDescription\x12-.ai.verta.modeldb.UpdateExperimentDescription\x1a\x36.ai.verta.modeldb.UpdateExperimentDescription.Response\"5\x82\xd3\xe4\x93\x02/\"*/v1/experiment/updateExperimentDescription:\x01*\x12\x93\x01\n\x11\x61\x64\x64\x45xperimentTags\x12#.ai.verta.modeldb.AddExperimentTags\x1a,.ai.verta.modeldb.AddExperimentTags.Response\"+\x82\xd3\xe4\x93\x02%\" /v1/experiment/addExperimentTags:\x01*\x12|\n\x11getExperimentTags\x12\x19.ai.verta.modeldb.GetTags\x1a\".ai.verta.modeldb.GetTags.Response\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/experiment/getExperimentTags\x12\x9f\x01\n\x14\x64\x65leteExperimentTags\x12&.ai.verta.modeldb.DeleteExperimentTags\x1a/.ai.verta.modeldb.DeleteExperimentTags.Response\".\x82\xd3\xe4\x93\x02(*#/v1/experiment/deleteExperimentTags:\x01*\x12\x8f\x01\n\x10\x61\x64\x64\x45xperimentTag\x12\".ai.verta.modeldb.AddExperimentTag\x1a+.ai.verta.modeldb.AddExperimentTag.Response\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/experiment/addExperimentTag:\x01*\x12\x9b\x01\n\x13\x64\x65leteExperimentTag\x12%.ai.verta.modeldb.DeleteExperimentTag\x1a..ai.verta.modeldb.DeleteExperimentTag.Response\"-\x82\xd3\xe4\x93\x02\'*\"/v1/experiment/deleteExperimentTag:\x01*\x12\x81\x01\n\x0c\x61\x64\x64\x41ttribute\x12\x1f.ai.verta.modeldb.AddAttributes\x1a(.ai.verta.modeldb.AddAttributes.Response\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/experiment/addAttribute:\x01*\x12\xab\x01\n\x17\x61\x64\x64\x45xperimentAttributes\x12).ai.verta.modeldb.AddExperimentAttributes\x1a\x32.ai.verta.modeldb.AddExperimentAttributes.Response\"1\x82\xd3\xe4\x93\x02+\"&/v1/experiment/addExperimentAttributes:\x01*\x12\x94\x01\n\x17getExperimentAttributes\x12\x1f.ai.verta.modeldb.GetAttributes\x1a(.ai.verta.modeldb.GetAttributes.Response\".\x82\xd3\xe4\x93\x02(\x12&/v1/experiment/getExperimentAttributes\x12\xb4\x01\n\x1a\x64\x65leteExperimentAttributes\x12,.ai.verta.modeldb.DeleteExperimentAttributes\x1a\x35.ai.verta.modeldb.DeleteExperimentAttributes.Response\"1\x82\xd3\xe4\x93\x02+*)/v1/experiment/deleteExperimentAttributes\x12\xaf\x01\n\x18logExperimentCodeVersion\x12*.ai.verta.modeldb.LogExperimentCodeVersion\x1a\x33.ai.verta.modeldb.LogExperimentCodeVersion.Response\"2\x82\xd3\xe4\x93\x02,\"\'/v1/experiment/logExperimentCodeVersion:\x01*\x12\xac\x01\n\x18getExperimentCodeVersion\x12*.ai.verta.modeldb.GetExperimentCodeVersion\x1a\x33.ai.verta.modeldb.GetExperimentCodeVersion.Response\"/\x82\xd3\xe4\x93\x02)\x12\'/v1/experiment/getExperimentCodeVersion\x12\xa8\x01\n\x17getExperimentsInProject\x12).ai.verta.modeldb.GetExperimentsInProject\x1a\x32.ai.verta.modeldb.GetExperimentsInProject.Response\".\x82\xd3\xe4\x93\x02(\x12&/v1/experiment/getExperimentsInProject\x12\x90\x01\n\x11getExperimentById\x12#.ai.verta.modeldb.GetExperimentById\x1a,.ai.verta.modeldb.GetExperimentById.Response\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/experiment/getExperimentById\x12\x98\x01\n\x13getExperimentByName\x12%.ai.verta.modeldb.GetExperimentByName\x1a..ai.verta.modeldb.GetExperimentByName.Response\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/experiment/getExperimentByName\x12\x8f\x01\n\x10\x64\x65leteExperiment\x12\".ai.verta.modeldb.DeleteExperiment\x1a+.ai.verta.modeldb.DeleteExperiment.Response\"*\x82\xd3\xe4\x93\x02$*\x1f/v1/experiment/deleteExperiment:\x01*\x12\x93\x01\n\x11getUrlForArtifact\x12#.ai.verta.modeldb.GetUrlForArtifact\x1a,.ai.verta.modeldb.GetUrlForArtifact.Response\"+\x82\xd3\xe4\x93\x02%\" /v1/experiment/getUrlForArtifact:\x01*\x12\x8b\x01\n\x0f\x66indExperiments\x12!.ai.verta.modeldb.FindExperiments\x1a*.ai.verta.modeldb.FindExperiments.Response\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/experiment/findExperiments:\x01*\x12\x93\x01\n\x0clogArtifacts\x12(.ai.verta.modeldb.LogExperimentArtifacts\x1a\x31.ai.verta.modeldb.LogExperimentArtifacts.Response\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/experiment/logArtifacts:\x01*\x12|\n\x0cgetArtifacts\x12\x1e.ai.verta.modeldb.GetArtifacts\x1a\'.ai.verta.modeldb.GetArtifacts.Response\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/experiment/getArtifacts\x12\x9b\x01\n\x0e\x64\x65leteArtifact\x12*.ai.verta.modeldb.DeleteExperimentArtifact\x1a\x33.ai.verta.modeldb.DeleteExperimentArtifact.Response\"(\x82\xd3\xe4\x93\x02\"*\x1d/v1/experiment/deleteArtifact:\x01*\x12\x93\x01\n\x11\x64\x65leteExperiments\x12#.ai.verta.modeldb.DeleteExperiments\x1a,.ai.verta.modeldb.DeleteExperiments.Response\"+\x82\xd3\xe4\x93\x02%* /v1/experiment/deleteExperiments:\x01*BBP\x01Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'modeldb.ExperimentService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldb'
  _EXPERIMENTSERVICE.methods_by_name['createExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['createExperiment']._serialized_options = b'\202\323\344\223\002$\"\037/v1/experiment/createExperiment:\001*'
  _EXPERIMENTSERVICE.methods_by_name['updateExperimentNameOrDescription']._options = None
  _EXPERIMENTSERVICE.methods_by_name['updateExperimentNameOrDescription']._serialized_options = b'\202\323\344\223\0025\"0/v1/experiment/updateExperimentNameOrDescription:\001*'
  _EXPERIMENTSERVICE.methods_by_name['updateExperimentName']._options = None
  _EXPERIMENTSERVICE.methods_by_name['updateExperimentName']._serialized_options = b'\202\323\344\223\002(\"#/v1/experiment/updateExperimentName:\001*'
  _EXPERIMENTSERVICE.methods_by_name['updateExperimentDescription']._options = None
  _EXPERIMENTSERVICE.methods_by_name['updateExperimentDescription']._serialized_options = b'\202\323\344\223\002/\"*/v1/experiment/updateExperimentDescription:\001*'
  _EXPERIMENTSERVICE.methods_by_name['addExperimentTags']._options = None
  _EXPERIMENTSERVICE.methods_by_name['addExperimentTags']._serialized_options = b'\202\323\344\223\002%\" /v1/experiment/addExperimentTags:\001*'
  _EXPERIMENTSERVICE.methods_by_name['getExperimentTags']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getExperimentTags']._serialized_options = b'\202\323\344\223\002\"\022 /v1/experiment/getExperimentTags'
  _EXPERIMENTSERVICE.methods_by_name['deleteExperimentTags']._options = None
  _EXPERIMENTSERVICE.methods_by_name['deleteExperimentTags']._serialized_options = b'\202\323\344\223\002(*#/v1/experiment/deleteExperimentTags:\001*'
  _EXPERIMENTSERVICE.methods_by_name['addExperimentTag']._options = None
  _EXPERIMENTSERVICE.methods_by_name['addExperimentTag']._serialized_options = b'\202\323\344\223\002$\"\037/v1/experiment/addExperimentTag:\001*'
  _EXPERIMENTSERVICE.methods_by_name['deleteExperimentTag']._options = None
  _EXPERIMENTSERVICE.methods_by_name['deleteExperimentTag']._serialized_options = b'\202\323\344\223\002\'*\"/v1/experiment/deleteExperimentTag:\001*'
  _EXPERIMENTSERVICE.methods_by_name['addAttribute']._options = None
  _EXPERIMENTSERVICE.methods_by_name['addAttribute']._serialized_options = b'\202\323\344\223\002 \"\033/v1/experiment/addAttribute:\001*'
  _EXPERIMENTSERVICE.methods_by_name['addExperimentAttributes']._options = None
  _EXPERIMENTSERVICE.methods_by_name['addExperimentAttributes']._serialized_options = b'\202\323\344\223\002+\"&/v1/experiment/addExperimentAttributes:\001*'
  _EXPERIMENTSERVICE.methods_by_name['getExperimentAttributes']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getExperimentAttributes']._serialized_options = b'\202\323\344\223\002(\022&/v1/experiment/getExperimentAttributes'
  _EXPERIMENTSERVICE.methods_by_name['deleteExperimentAttributes']._options = None
  _EXPERIMENTSERVICE.methods_by_name['deleteExperimentAttributes']._serialized_options = b'\202\323\344\223\002+*)/v1/experiment/deleteExperimentAttributes'
  _EXPERIMENTSERVICE.methods_by_name['logExperimentCodeVersion']._options = None
  _EXPERIMENTSERVICE.methods_by_name['logExperimentCodeVersion']._serialized_options = b'\202\323\344\223\002,\"\'/v1/experiment/logExperimentCodeVersion:\001*'
  _EXPERIMENTSERVICE.methods_by_name['getExperimentCodeVersion']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getExperimentCodeVersion']._serialized_options = b'\202\323\344\223\002)\022\'/v1/experiment/getExperimentCodeVersion'
  _EXPERIMENTSERVICE.methods_by_name['getExperimentsInProject']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getExperimentsInProject']._serialized_options = b'\202\323\344\223\002(\022&/v1/experiment/getExperimentsInProject'
  _EXPERIMENTSERVICE.methods_by_name['getExperimentById']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getExperimentById']._serialized_options = b'\202\323\344\223\002\"\022 /v1/experiment/getExperimentById'
  _EXPERIMENTSERVICE.methods_by_name['getExperimentByName']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getExperimentByName']._serialized_options = b'\202\323\344\223\002$\022\"/v1/experiment/getExperimentByName'
  _EXPERIMENTSERVICE.methods_by_name['deleteExperiment']._options = None
  _EXPERIMENTSERVICE.methods_by_name['deleteExperiment']._serialized_options = b'\202\323\344\223\002$*\037/v1/experiment/deleteExperiment:\001*'
  _EXPERIMENTSERVICE.methods_by_name['getUrlForArtifact']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getUrlForArtifact']._serialized_options = b'\202\323\344\223\002%\" /v1/experiment/getUrlForArtifact:\001*'
  _EXPERIMENTSERVICE.methods_by_name['findExperiments']._options = None
  _EXPERIMENTSERVICE.methods_by_name['findExperiments']._serialized_options = b'\202\323\344\223\002#\"\036/v1/experiment/findExperiments:\001*'
  _EXPERIMENTSERVICE.methods_by_name['logArtifacts']._options = None
  _EXPERIMENTSERVICE.methods_by_name['logArtifacts']._serialized_options = b'\202\323\344\223\002 \"\033/v1/experiment/logArtifacts:\001*'
  _EXPERIMENTSERVICE.methods_by_name['getArtifacts']._options = None
  _EXPERIMENTSERVICE.methods_by_name['getArtifacts']._serialized_options = b'\202\323\344\223\002\035\022\033/v1/experiment/getArtifacts'
  _EXPERIMENTSERVICE.methods_by_name['deleteArtifact']._options = None
  _EXPERIMENTSERVICE.methods_by_name['deleteArtifact']._serialized_options = b'\202\323\344\223\002\"*\035/v1/experiment/deleteArtifact:\001*'
  _EXPERIMENTSERVICE.methods_by_name['deleteExperiments']._options = None
  _EXPERIMENTSERVICE.methods_by_name['deleteExperiments']._serialized_options = b'\202\323\344\223\002%* /v1/experiment/deleteExperiments:\001*'
  _EXPERIMENT._serialized_start=141
  _EXPERIMENT._serialized_end=561
  _GETEXPERIMENTSINPROJECT._serialized_start=564
  _GETEXPERIMENTSINPROJECT._serialized_end=773
  _GETEXPERIMENTSINPROJECT_RESPONSE._serialized_start=689
  _GETEXPERIMENTSINPROJECT_RESPONSE._serialized_end=773
  _GETEXPERIMENTBYID._serialized_start=775
  _GETEXPERIMENTBYID._serialized_end=868
  _GETEXPERIMENTBYID_RESPONSE._serialized_start=808
  _GETEXPERIMENTBYID_RESPONSE._serialized_end=868
  _GETEXPERIMENTBYNAME._serialized_start=870
  _GETEXPERIMENTBYNAME._serialized_end=987
  _GETEXPERIMENTBYNAME_RESPONSE._serialized_start=808
  _GETEXPERIMENTBYNAME_RESPONSE._serialized_end=868
  _CREATEEXPERIMENT._serialized_start=990
  _CREATEEXPERIMENT._serialized_end=1276
  _CREATEEXPERIMENT_RESPONSE._serialized_start=808
  _CREATEEXPERIMENT_RESPONSE._serialized_end=868
  _DELETEEXPERIMENT._serialized_start=1278
  _DELETEEXPERIMENT._serialized_end=1336
  _DELETEEXPERIMENT_RESPONSE._serialized_start=1310
  _DELETEEXPERIMENT_RESPONSE._serialized_end=1336
  _UPDATEEXPERIMENTNAMEORDESCRIPTION._serialized_start=1339
  _UPDATEEXPERIMENTNAMEORDESCRIPTION._serialized_end=1483
  _UPDATEEXPERIMENTNAMEORDESCRIPTION_RESPONSE._serialized_start=808
  _UPDATEEXPERIMENTNAMEORDESCRIPTION_RESPONSE._serialized_end=868
  _UPDATEEXPERIMENTNAME._serialized_start=1485
  _UPDATEEXPERIMENTNAME._serialized_end=1595
  _UPDATEEXPERIMENTNAME_RESPONSE._serialized_start=808
  _UPDATEEXPERIMENTNAME_RESPONSE._serialized_end=868
  _UPDATEEXPERIMENTDESCRIPTION._serialized_start=1597
  _UPDATEEXPERIMENTDESCRIPTION._serialized_end=1721
  _UPDATEEXPERIMENTDESCRIPTION_RESPONSE._serialized_start=808
  _UPDATEEXPERIMENTDESCRIPTION_RESPONSE._serialized_end=868
  _ADDEXPERIMENTTAGS._serialized_start=1723
  _ADDEXPERIMENTTAGS._serialized_end=1830
  _ADDEXPERIMENTTAGS_RESPONSE._serialized_start=808
  _ADDEXPERIMENTTAGS_RESPONSE._serialized_end=868
  _DELETEEXPERIMENTTAGS._serialized_start=1833
  _DELETEEXPERIMENTTAGS._serialized_end=1963
  _DELETEEXPERIMENTTAGS_RESPONSE._serialized_start=808
  _DELETEEXPERIMENTTAGS_RESPONSE._serialized_end=868
  _ADDEXPERIMENTTAG._serialized_start=1965
  _ADDEXPERIMENTTAG._serialized_end=2070
  _ADDEXPERIMENTTAG_RESPONSE._serialized_start=808
  _ADDEXPERIMENTTAG_RESPONSE._serialized_end=868
  _DELETEEXPERIMENTTAG._serialized_start=2072
  _DELETEEXPERIMENTTAG._serialized_end=2180
  _DELETEEXPERIMENTTAG_RESPONSE._serialized_start=808
  _DELETEEXPERIMENTTAG_RESPONSE._serialized_end=868
  _ADDEXPERIMENTATTRIBUTES._serialized_start=2183
  _ADDEXPERIMENTATTRIBUTES._serialized_end=2329
  _ADDEXPERIMENTATTRIBUTES_RESPONSE._serialized_start=808
  _ADDEXPERIMENTATTRIBUTES_RESPONSE._serialized_end=868
  _DELETEEXPERIMENTATTRIBUTES._serialized_start=2332
  _DELETEEXPERIMENTATTRIBUTES._serialized_end=2478
  _DELETEEXPERIMENTATTRIBUTES_RESPONSE._serialized_start=808
  _DELETEEXPERIMENTATTRIBUTES_RESPONSE._serialized_end=868
  _LOGEXPERIMENTCODEVERSION._serialized_start=2481
  _LOGEXPERIMENTCODEVERSION._serialized_end=2633
  _LOGEXPERIMENTCODEVERSION_RESPONSE._serialized_start=808
  _LOGEXPERIMENTCODEVERSION_RESPONSE._serialized_end=868
  _GETEXPERIMENTCODEVERSION._serialized_start=2635
  _GETEXPERIMENTCODEVERSION._serialized_end=2737
  _GETEXPERIMENTCODEVERSION_RESPONSE._serialized_start=2675
  _GETEXPERIMENTCODEVERSION_RESPONSE._serialized_end=2737
  _FINDEXPERIMENTS._serialized_start=2740
  _FINDEXPERIMENTS._serialized_end=3059
  _FINDEXPERIMENTS_RESPONSE._serialized_start=689
  _FINDEXPERIMENTS_RESPONSE._serialized_end=773
  _LOGEXPERIMENTARTIFACTS._serialized_start=3062
  _LOGEXPERIMENTARTIFACTS._serialized_end=3206
  _LOGEXPERIMENTARTIFACTS_RESPONSE._serialized_start=808
  _LOGEXPERIMENTARTIFACTS_RESPONSE._serialized_end=868
  _DELETEEXPERIMENTARTIFACT._serialized_start=3208
  _DELETEEXPERIMENTARTIFACT._serialized_end=3321
  _DELETEEXPERIMENTARTIFACT_RESPONSE._serialized_start=808
  _DELETEEXPERIMENTARTIFACT_RESPONSE._serialized_end=868
  _DELETEEXPERIMENTS._serialized_start=3323
  _DELETEEXPERIMENTS._serialized_end=3383
  _DELETEEXPERIMENTS_RESPONSE._serialized_start=1310
  _DELETEEXPERIMENTS_RESPONSE._serialized_end=1336
  _EXPERIMENTSERVICE._serialized_start=3386
  _EXPERIMENTSERVICE._serialized_end=7347
# @@protoc_insertion_point(module_scope)
