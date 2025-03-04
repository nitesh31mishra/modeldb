# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..uac import OrganizationV2_pb2 as uac_dot_OrganizationV2__pb2


class OrganizationServiceV2Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getOrganizationById = channel.unary_unary(
        '/ai.verta.uac.OrganizationServiceV2/getOrganizationById',
        request_serializer=uac_dot_OrganizationV2__pb2.GetOrganizationByIdV2.SerializeToString,
        response_deserializer=uac_dot_OrganizationV2__pb2.GetOrganizationByIdV2.Response.FromString,
        )
    self.getOrganizationByName = channel.unary_unary(
        '/ai.verta.uac.OrganizationServiceV2/getOrganizationByName',
        request_serializer=uac_dot_OrganizationV2__pb2.GetOrganizationByNameV2.SerializeToString,
        response_deserializer=uac_dot_OrganizationV2__pb2.GetOrganizationByNameV2.Response.FromString,
        )
    self.listOrganizations = channel.unary_unary(
        '/ai.verta.uac.OrganizationServiceV2/listOrganizations',
        request_serializer=uac_dot_OrganizationV2__pb2.ListOrganizationsV2.SerializeToString,
        response_deserializer=uac_dot_OrganizationV2__pb2.ListOrganizationsV2.Response.FromString,
        )
    self.setOrganization = channel.unary_unary(
        '/ai.verta.uac.OrganizationServiceV2/setOrganization',
        request_serializer=uac_dot_OrganizationV2__pb2.SetOrganizationV2.SerializeToString,
        response_deserializer=uac_dot_OrganizationV2__pb2.SetOrganizationV2.Response.FromString,
        )
    self.deleteOrganization = channel.unary_unary(
        '/ai.verta.uac.OrganizationServiceV2/deleteOrganization',
        request_serializer=uac_dot_OrganizationV2__pb2.DeleteOrganizationV2.SerializeToString,
        response_deserializer=uac_dot_OrganizationV2__pb2.DeleteOrganizationV2.Response.FromString,
        )


class OrganizationServiceV2Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getOrganizationById(self, request, context):
    """Gets information from a given organization
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getOrganizationByName(self, request, context):
    """Gets information from a given organization
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listOrganizations(self, request, context):
    """Lists the organizations that the current user can access
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setOrganization(self, request, context):
    """Create or update an organization
    Automatically sets the user making the call as owner and adds to the organization
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteOrganization(self, request, context):
    """Delete an existing organization
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OrganizationServiceV2Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getOrganizationById': grpc.unary_unary_rpc_method_handler(
          servicer.getOrganizationById,
          request_deserializer=uac_dot_OrganizationV2__pb2.GetOrganizationByIdV2.FromString,
          response_serializer=uac_dot_OrganizationV2__pb2.GetOrganizationByIdV2.Response.SerializeToString,
      ),
      'getOrganizationByName': grpc.unary_unary_rpc_method_handler(
          servicer.getOrganizationByName,
          request_deserializer=uac_dot_OrganizationV2__pb2.GetOrganizationByNameV2.FromString,
          response_serializer=uac_dot_OrganizationV2__pb2.GetOrganizationByNameV2.Response.SerializeToString,
      ),
      'listOrganizations': grpc.unary_unary_rpc_method_handler(
          servicer.listOrganizations,
          request_deserializer=uac_dot_OrganizationV2__pb2.ListOrganizationsV2.FromString,
          response_serializer=uac_dot_OrganizationV2__pb2.ListOrganizationsV2.Response.SerializeToString,
      ),
      'setOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.setOrganization,
          request_deserializer=uac_dot_OrganizationV2__pb2.SetOrganizationV2.FromString,
          response_serializer=uac_dot_OrganizationV2__pb2.SetOrganizationV2.Response.SerializeToString,
      ),
      'deleteOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.deleteOrganization,
          request_deserializer=uac_dot_OrganizationV2__pb2.DeleteOrganizationV2.FromString,
          response_serializer=uac_dot_OrganizationV2__pb2.DeleteOrganizationV2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.OrganizationServiceV2', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
