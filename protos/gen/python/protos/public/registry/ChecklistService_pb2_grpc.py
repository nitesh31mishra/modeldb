# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..registry import ChecklistService_pb2 as registry_dot_ChecklistService__pb2
from ..registry import RegistryService_pb2 as registry_dot_RegistryService__pb2


class ChecklistServiceStub(object):
  """Initial functions to list all, create, retreive, update and delete checklist_item_values
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FindChecklistItemValues = channel.unary_unary(
        '/ai.verta.registry.ChecklistService/FindChecklistItemValues',
        request_serializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.Response.FromString,
        )
    self.GetChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.ChecklistService/GetChecklistItemValue',
        request_serializer=registry_dot_ChecklistService__pb2.GetChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_ChecklistService__pb2.GetChecklistItemValueRequest.Response.FromString,
        )
    self.CreateChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.ChecklistService/CreateChecklistItemValue',
        request_serializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.Response.FromString,
        )
    self.UpdateChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.ChecklistService/UpdateChecklistItemValue',
        request_serializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.Response.FromString,
        )
    self.DeleteChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.ChecklistService/DeleteChecklistItemValue',
        request_serializer=registry_dot_ChecklistService__pb2.DeleteChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_ChecklistService__pb2.DeleteChecklistItemValueRequest.Response.FromString,
        )


class ChecklistServiceServicer(object):
  """Initial functions to list all, create, retreive, update and delete checklist_item_values
  """

  def FindChecklistItemValues(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChecklistServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FindChecklistItemValues': grpc.unary_unary_rpc_method_handler(
          servicer.FindChecklistItemValues,
          request_deserializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.Response.SerializeToString,
      ),
      'GetChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.GetChecklistItemValue,
          request_deserializer=registry_dot_ChecklistService__pb2.GetChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_ChecklistService__pb2.GetChecklistItemValueRequest.Response.SerializeToString,
      ),
      'CreateChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.CreateChecklistItemValue,
          request_deserializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.Response.SerializeToString,
      ),
      'UpdateChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateChecklistItemValue,
          request_deserializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_ChecklistService__pb2.SetChecklistItemValueRequest.Response.SerializeToString,
      ),
      'DeleteChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteChecklistItemValue,
          request_deserializer=registry_dot_ChecklistService__pb2.DeleteChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_ChecklistService__pb2.DeleteChecklistItemValueRequest.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.registry.ChecklistService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
