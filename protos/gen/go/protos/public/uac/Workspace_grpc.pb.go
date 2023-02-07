// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.21.6
// source: uac/Workspace.proto

package uac

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// WorkspaceServiceClient is the client API for WorkspaceService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type WorkspaceServiceClient interface {
	GetWorkspaceById(ctx context.Context, in *GetWorkspaceById, opts ...grpc.CallOption) (*Workspace, error)
	GetWorkspaceByName(ctx context.Context, in *GetWorkspaceByName, opts ...grpc.CallOption) (*Workspace, error)
	GetWorkspaceByLegacyId(ctx context.Context, in *GetWorkspaceByLegacyId, opts ...grpc.CallOption) (*Workspace, error)
	GetVisibleWorkspaces(ctx context.Context, in *GetVisibleWorkspaces, opts ...grpc.CallOption) (*Workspaces, error)
	CreateOrUpdateContainerRegistryConfiguration(ctx context.Context, in *WorkspaceContainerRegistryConfiguration, opts ...grpc.CallOption) (*WorkspaceContainerRegistryConfiguration, error)
	DeleteContainerRegistryConfiguration(ctx context.Context, in *WorkspaceContainerRegistryConfiguration, opts ...grpc.CallOption) (*Empty, error)
}

type workspaceServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewWorkspaceServiceClient(cc grpc.ClientConnInterface) WorkspaceServiceClient {
	return &workspaceServiceClient{cc}
}

func (c *workspaceServiceClient) GetWorkspaceById(ctx context.Context, in *GetWorkspaceById, opts ...grpc.CallOption) (*Workspace, error) {
	out := new(Workspace)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.WorkspaceService/getWorkspaceById", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceServiceClient) GetWorkspaceByName(ctx context.Context, in *GetWorkspaceByName, opts ...grpc.CallOption) (*Workspace, error) {
	out := new(Workspace)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.WorkspaceService/getWorkspaceByName", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceServiceClient) GetWorkspaceByLegacyId(ctx context.Context, in *GetWorkspaceByLegacyId, opts ...grpc.CallOption) (*Workspace, error) {
	out := new(Workspace)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.WorkspaceService/getWorkspaceByLegacyId", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceServiceClient) GetVisibleWorkspaces(ctx context.Context, in *GetVisibleWorkspaces, opts ...grpc.CallOption) (*Workspaces, error) {
	out := new(Workspaces)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.WorkspaceService/getVisibleWorkspaces", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceServiceClient) CreateOrUpdateContainerRegistryConfiguration(ctx context.Context, in *WorkspaceContainerRegistryConfiguration, opts ...grpc.CallOption) (*WorkspaceContainerRegistryConfiguration, error) {
	out := new(WorkspaceContainerRegistryConfiguration)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.WorkspaceService/createOrUpdateContainerRegistryConfiguration", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceServiceClient) DeleteContainerRegistryConfiguration(ctx context.Context, in *WorkspaceContainerRegistryConfiguration, opts ...grpc.CallOption) (*Empty, error) {
	out := new(Empty)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.WorkspaceService/deleteContainerRegistryConfiguration", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// WorkspaceServiceServer is the server API for WorkspaceService service.
// All implementations must embed UnimplementedWorkspaceServiceServer
// for forward compatibility
type WorkspaceServiceServer interface {
	GetWorkspaceById(context.Context, *GetWorkspaceById) (*Workspace, error)
	GetWorkspaceByName(context.Context, *GetWorkspaceByName) (*Workspace, error)
	GetWorkspaceByLegacyId(context.Context, *GetWorkspaceByLegacyId) (*Workspace, error)
	GetVisibleWorkspaces(context.Context, *GetVisibleWorkspaces) (*Workspaces, error)
	CreateOrUpdateContainerRegistryConfiguration(context.Context, *WorkspaceContainerRegistryConfiguration) (*WorkspaceContainerRegistryConfiguration, error)
	DeleteContainerRegistryConfiguration(context.Context, *WorkspaceContainerRegistryConfiguration) (*Empty, error)
	mustEmbedUnimplementedWorkspaceServiceServer()
}

// UnimplementedWorkspaceServiceServer must be embedded to have forward compatible implementations.
type UnimplementedWorkspaceServiceServer struct {
}

func (UnimplementedWorkspaceServiceServer) GetWorkspaceById(context.Context, *GetWorkspaceById) (*Workspace, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetWorkspaceById not implemented")
}
func (UnimplementedWorkspaceServiceServer) GetWorkspaceByName(context.Context, *GetWorkspaceByName) (*Workspace, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetWorkspaceByName not implemented")
}
func (UnimplementedWorkspaceServiceServer) GetWorkspaceByLegacyId(context.Context, *GetWorkspaceByLegacyId) (*Workspace, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetWorkspaceByLegacyId not implemented")
}
func (UnimplementedWorkspaceServiceServer) GetVisibleWorkspaces(context.Context, *GetVisibleWorkspaces) (*Workspaces, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetVisibleWorkspaces not implemented")
}
func (UnimplementedWorkspaceServiceServer) CreateOrUpdateContainerRegistryConfiguration(context.Context, *WorkspaceContainerRegistryConfiguration) (*WorkspaceContainerRegistryConfiguration, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateOrUpdateContainerRegistryConfiguration not implemented")
}
func (UnimplementedWorkspaceServiceServer) DeleteContainerRegistryConfiguration(context.Context, *WorkspaceContainerRegistryConfiguration) (*Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteContainerRegistryConfiguration not implemented")
}
func (UnimplementedWorkspaceServiceServer) mustEmbedUnimplementedWorkspaceServiceServer() {}

// UnsafeWorkspaceServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to WorkspaceServiceServer will
// result in compilation errors.
type UnsafeWorkspaceServiceServer interface {
	mustEmbedUnimplementedWorkspaceServiceServer()
}

func RegisterWorkspaceServiceServer(s grpc.ServiceRegistrar, srv WorkspaceServiceServer) {
	s.RegisterService(&WorkspaceService_ServiceDesc, srv)
}

func _WorkspaceService_GetWorkspaceById_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetWorkspaceById)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceServiceServer).GetWorkspaceById(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.WorkspaceService/getWorkspaceById",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceServiceServer).GetWorkspaceById(ctx, req.(*GetWorkspaceById))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceService_GetWorkspaceByName_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetWorkspaceByName)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceServiceServer).GetWorkspaceByName(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.WorkspaceService/getWorkspaceByName",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceServiceServer).GetWorkspaceByName(ctx, req.(*GetWorkspaceByName))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceService_GetWorkspaceByLegacyId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetWorkspaceByLegacyId)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceServiceServer).GetWorkspaceByLegacyId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.WorkspaceService/getWorkspaceByLegacyId",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceServiceServer).GetWorkspaceByLegacyId(ctx, req.(*GetWorkspaceByLegacyId))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceService_GetVisibleWorkspaces_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetVisibleWorkspaces)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceServiceServer).GetVisibleWorkspaces(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.WorkspaceService/getVisibleWorkspaces",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceServiceServer).GetVisibleWorkspaces(ctx, req.(*GetVisibleWorkspaces))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceService_CreateOrUpdateContainerRegistryConfiguration_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceContainerRegistryConfiguration)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceServiceServer).CreateOrUpdateContainerRegistryConfiguration(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.WorkspaceService/createOrUpdateContainerRegistryConfiguration",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceServiceServer).CreateOrUpdateContainerRegistryConfiguration(ctx, req.(*WorkspaceContainerRegistryConfiguration))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceService_DeleteContainerRegistryConfiguration_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceContainerRegistryConfiguration)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceServiceServer).DeleteContainerRegistryConfiguration(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.WorkspaceService/deleteContainerRegistryConfiguration",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceServiceServer).DeleteContainerRegistryConfiguration(ctx, req.(*WorkspaceContainerRegistryConfiguration))
	}
	return interceptor(ctx, in, info, handler)
}

// WorkspaceService_ServiceDesc is the grpc.ServiceDesc for WorkspaceService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var WorkspaceService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "ai.verta.uac.WorkspaceService",
	HandlerType: (*WorkspaceServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "getWorkspaceById",
			Handler:    _WorkspaceService_GetWorkspaceById_Handler,
		},
		{
			MethodName: "getWorkspaceByName",
			Handler:    _WorkspaceService_GetWorkspaceByName_Handler,
		},
		{
			MethodName: "getWorkspaceByLegacyId",
			Handler:    _WorkspaceService_GetWorkspaceByLegacyId_Handler,
		},
		{
			MethodName: "getVisibleWorkspaces",
			Handler:    _WorkspaceService_GetVisibleWorkspaces_Handler,
		},
		{
			MethodName: "createOrUpdateContainerRegistryConfiguration",
			Handler:    _WorkspaceService_CreateOrUpdateContainerRegistryConfiguration_Handler,
		},
		{
			MethodName: "deleteContainerRegistryConfiguration",
			Handler:    _WorkspaceService_DeleteContainerRegistryConfiguration_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "uac/Workspace.proto",
}
