# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..uac import UserV2_pb2 as uac_dot_UserV2__pb2


class UserServiceV2Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.searchUsers = channel.unary_unary(
                '/ai.verta.uac.UserServiceV2/searchUsers',
                request_serializer=uac_dot_UserV2__pb2.SearchUsers.SerializeToString,
                response_deserializer=uac_dot_UserV2__pb2.SearchUsers.Response.FromString,
                )
        self.addUser = channel.unary_unary(
                '/ai.verta.uac.UserServiceV2/addUser',
                request_serializer=uac_dot_UserV2__pb2.AddUserV2.SerializeToString,
                response_deserializer=uac_dot_UserV2__pb2.AddUserV2.Response.FromString,
                )
        self.removeUser = channel.unary_unary(
                '/ai.verta.uac.UserServiceV2/removeUser',
                request_serializer=uac_dot_UserV2__pb2.RemoveUserV2.SerializeToString,
                response_deserializer=uac_dot_UserV2__pb2.RemoveUserV2.Response.FromString,
                )
        self.addServiceAccount = channel.unary_unary(
                '/ai.verta.uac.UserServiceV2/addServiceAccount',
                request_serializer=uac_dot_UserV2__pb2.AddServiceAccount.SerializeToString,
                response_deserializer=uac_dot_UserV2__pb2.AddServiceAccount.Response.FromString,
                )
        self.removeServiceAccount = channel.unary_unary(
                '/ai.verta.uac.UserServiceV2/removeServiceAccount',
                request_serializer=uac_dot_UserV2__pb2.RemoveServiceAccount.SerializeToString,
                response_deserializer=uac_dot_UserV2__pb2.RemoveServiceAccount.Response.FromString,
                )
        self.getUser = channel.unary_unary(
                '/ai.verta.uac.UserServiceV2/getUser',
                request_serializer=uac_dot_UserV2__pb2.GetUserV2.SerializeToString,
                response_deserializer=uac_dot_UserV2__pb2.GetUserV2.Response.FromString,
                )


class UserServiceV2Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def searchUsers(self, request, context):
        """List for users inside an organization, returning details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addUser(self, request, context):
        """Adds the given user to the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removeUser(self, request, context):
        """Removes the given user to the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addServiceAccount(self, request, context):
        """Adds a service account to the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removeServiceAccount(self, request, context):
        """Removes a service account from the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUser(self, request, context):
        """Get a user inside an organization, returning details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceV2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'searchUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.searchUsers,
                    request_deserializer=uac_dot_UserV2__pb2.SearchUsers.FromString,
                    response_serializer=uac_dot_UserV2__pb2.SearchUsers.Response.SerializeToString,
            ),
            'addUser': grpc.unary_unary_rpc_method_handler(
                    servicer.addUser,
                    request_deserializer=uac_dot_UserV2__pb2.AddUserV2.FromString,
                    response_serializer=uac_dot_UserV2__pb2.AddUserV2.Response.SerializeToString,
            ),
            'removeUser': grpc.unary_unary_rpc_method_handler(
                    servicer.removeUser,
                    request_deserializer=uac_dot_UserV2__pb2.RemoveUserV2.FromString,
                    response_serializer=uac_dot_UserV2__pb2.RemoveUserV2.Response.SerializeToString,
            ),
            'addServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.addServiceAccount,
                    request_deserializer=uac_dot_UserV2__pb2.AddServiceAccount.FromString,
                    response_serializer=uac_dot_UserV2__pb2.AddServiceAccount.Response.SerializeToString,
            ),
            'removeServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.removeServiceAccount,
                    request_deserializer=uac_dot_UserV2__pb2.RemoveServiceAccount.FromString,
                    response_serializer=uac_dot_UserV2__pb2.RemoveServiceAccount.Response.SerializeToString,
            ),
            'getUser': grpc.unary_unary_rpc_method_handler(
                    servicer.getUser,
                    request_deserializer=uac_dot_UserV2__pb2.GetUserV2.FromString,
                    response_serializer=uac_dot_UserV2__pb2.GetUserV2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ai.verta.uac.UserServiceV2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserServiceV2(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def searchUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.verta.uac.UserServiceV2/searchUsers',
            uac_dot_UserV2__pb2.SearchUsers.SerializeToString,
            uac_dot_UserV2__pb2.SearchUsers.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.verta.uac.UserServiceV2/addUser',
            uac_dot_UserV2__pb2.AddUserV2.SerializeToString,
            uac_dot_UserV2__pb2.AddUserV2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removeUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.verta.uac.UserServiceV2/removeUser',
            uac_dot_UserV2__pb2.RemoveUserV2.SerializeToString,
            uac_dot_UserV2__pb2.RemoveUserV2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addServiceAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.verta.uac.UserServiceV2/addServiceAccount',
            uac_dot_UserV2__pb2.AddServiceAccount.SerializeToString,
            uac_dot_UserV2__pb2.AddServiceAccount.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removeServiceAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.verta.uac.UserServiceV2/removeServiceAccount',
            uac_dot_UserV2__pb2.RemoveServiceAccount.SerializeToString,
            uac_dot_UserV2__pb2.RemoveServiceAccount.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ai.verta.uac.UserServiceV2/getUser',
            uac_dot_UserV2__pb2.GetUserV2.SerializeToString,
            uac_dot_UserV2__pb2.GetUserV2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
