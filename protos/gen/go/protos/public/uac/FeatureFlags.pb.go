// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.26.0
// 	protoc        v3.21.6
// source: uac/FeatureFlags.proto

package uac

import (
	context "context"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type FeatureFlagsRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *FeatureFlagsRequest) Reset() {
	*x = FeatureFlagsRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_uac_FeatureFlags_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureFlagsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureFlagsRequest) ProtoMessage() {}

func (x *FeatureFlagsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_uac_FeatureFlags_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureFlagsRequest.ProtoReflect.Descriptor instead.
func (*FeatureFlagsRequest) Descriptor() ([]byte, []int) {
	return file_uac_FeatureFlags_proto_rawDescGZIP(), []int{0}
}

type FeatureFlagItem struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Enabled bool   `protobuf:"varint,1,opt,name=enabled,proto3" json:"enabled,omitempty"`
	Content string `protobuf:"bytes,2,opt,name=content,proto3" json:"content,omitempty"`
}

func (x *FeatureFlagItem) Reset() {
	*x = FeatureFlagItem{}
	if protoimpl.UnsafeEnabled {
		mi := &file_uac_FeatureFlags_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureFlagItem) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureFlagItem) ProtoMessage() {}

func (x *FeatureFlagItem) ProtoReflect() protoreflect.Message {
	mi := &file_uac_FeatureFlags_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureFlagItem.ProtoReflect.Descriptor instead.
func (*FeatureFlagItem) Descriptor() ([]byte, []int) {
	return file_uac_FeatureFlags_proto_rawDescGZIP(), []int{1}
}

func (x *FeatureFlagItem) GetEnabled() bool {
	if x != nil {
		return x.Enabled
	}
	return false
}

func (x *FeatureFlagItem) GetContent() string {
	if x != nil {
		return x.Content
	}
	return ""
}

type FeatureFlagsRequest_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	FeatureFlags map[string]*FeatureFlagItem `protobuf:"bytes,1,rep,name=feature_flags,json=featureFlags,proto3" json:"feature_flags,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *FeatureFlagsRequest_Response) Reset() {
	*x = FeatureFlagsRequest_Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_uac_FeatureFlags_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureFlagsRequest_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureFlagsRequest_Response) ProtoMessage() {}

func (x *FeatureFlagsRequest_Response) ProtoReflect() protoreflect.Message {
	mi := &file_uac_FeatureFlags_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureFlagsRequest_Response.ProtoReflect.Descriptor instead.
func (*FeatureFlagsRequest_Response) Descriptor() ([]byte, []int) {
	return file_uac_FeatureFlags_proto_rawDescGZIP(), []int{0, 0}
}

func (x *FeatureFlagsRequest_Response) GetFeatureFlags() map[string]*FeatureFlagItem {
	if x != nil {
		return x.FeatureFlags
	}
	return nil
}

var File_uac_FeatureFlags_proto protoreflect.FileDescriptor

var file_uac_FeatureFlags_proto_rawDesc = []byte{
	0x0a, 0x16, 0x75, 0x61, 0x63, 0x2f, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61,
	0x67, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0c, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72,
	0x74, 0x61, 0x2e, 0x75, 0x61, 0x63, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0xe5, 0x01, 0x0a, 0x13, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65,
	0x46, 0x6c, 0x61, 0x67, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0xcd, 0x01, 0x0a,
	0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x61, 0x0a, 0x0d, 0x66, 0x65, 0x61,
	0x74, 0x75, 0x72, 0x65, 0x5f, 0x66, 0x6c, 0x61, 0x67, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x3c, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x75, 0x61, 0x63, 0x2e,
	0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x46, 0x65, 0x61,
	0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0c,
	0x66, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x1a, 0x5e, 0x0a, 0x11,
	0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x45, 0x6e, 0x74, 0x72,
	0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03,
	0x6b, 0x65, 0x79, 0x12, 0x33, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x75, 0x61,
	0x63, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x49, 0x74, 0x65,
	0x6d, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0x45, 0x0a, 0x0f,
	0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x49, 0x74, 0x65, 0x6d, 0x12,
	0x18, 0x0a, 0x07, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x08,
	0x52, 0x07, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x64, 0x12, 0x18, 0x0a, 0x07, 0x63, 0x6f, 0x6e,
	0x74, 0x65, 0x6e, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x63, 0x6f, 0x6e, 0x74,
	0x65, 0x6e, 0x74, 0x32, 0x92, 0x01, 0x0a, 0x13, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46,
	0x6c, 0x61, 0x67, 0x73, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x7b, 0x0a, 0x0f, 0x67,
	0x65, 0x74, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x12, 0x21,
	0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x75, 0x61, 0x63, 0x2e, 0x46, 0x65,
	0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x2a, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x75, 0x61, 0x63,
	0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x46, 0x6c, 0x61, 0x67, 0x73, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x19, 0x82,
	0xd3, 0xe4, 0x93, 0x02, 0x13, 0x12, 0x11, 0x2f, 0x76, 0x31, 0x2f, 0x66, 0x65, 0x61, 0x74, 0x75,
	0x72, 0x65, 0x2d, 0x66, 0x6c, 0x61, 0x67, 0x73, 0x42, 0x3e, 0x50, 0x01, 0x5a, 0x3a, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x56, 0x65, 0x72, 0x74, 0x61, 0x41, 0x49,
	0x2f, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f,
	0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x70, 0x75,
	0x62, 0x6c, 0x69, 0x63, 0x2f, 0x75, 0x61, 0x63, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_uac_FeatureFlags_proto_rawDescOnce sync.Once
	file_uac_FeatureFlags_proto_rawDescData = file_uac_FeatureFlags_proto_rawDesc
)

func file_uac_FeatureFlags_proto_rawDescGZIP() []byte {
	file_uac_FeatureFlags_proto_rawDescOnce.Do(func() {
		file_uac_FeatureFlags_proto_rawDescData = protoimpl.X.CompressGZIP(file_uac_FeatureFlags_proto_rawDescData)
	})
	return file_uac_FeatureFlags_proto_rawDescData
}

var file_uac_FeatureFlags_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_uac_FeatureFlags_proto_goTypes = []interface{}{
	(*FeatureFlagsRequest)(nil),          // 0: ai.verta.uac.FeatureFlagsRequest
	(*FeatureFlagItem)(nil),              // 1: ai.verta.uac.FeatureFlagItem
	(*FeatureFlagsRequest_Response)(nil), // 2: ai.verta.uac.FeatureFlagsRequest.Response
	nil,                                  // 3: ai.verta.uac.FeatureFlagsRequest.Response.FeatureFlagsEntry
}
var file_uac_FeatureFlags_proto_depIdxs = []int32{
	3, // 0: ai.verta.uac.FeatureFlagsRequest.Response.feature_flags:type_name -> ai.verta.uac.FeatureFlagsRequest.Response.FeatureFlagsEntry
	1, // 1: ai.verta.uac.FeatureFlagsRequest.Response.FeatureFlagsEntry.value:type_name -> ai.verta.uac.FeatureFlagItem
	0, // 2: ai.verta.uac.FeatureFlagsService.getFeatureFlags:input_type -> ai.verta.uac.FeatureFlagsRequest
	2, // 3: ai.verta.uac.FeatureFlagsService.getFeatureFlags:output_type -> ai.verta.uac.FeatureFlagsRequest.Response
	3, // [3:4] is the sub-list for method output_type
	2, // [2:3] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_uac_FeatureFlags_proto_init() }
func file_uac_FeatureFlags_proto_init() {
	if File_uac_FeatureFlags_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_uac_FeatureFlags_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureFlagsRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_uac_FeatureFlags_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureFlagItem); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_uac_FeatureFlags_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureFlagsRequest_Response); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_uac_FeatureFlags_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_uac_FeatureFlags_proto_goTypes,
		DependencyIndexes: file_uac_FeatureFlags_proto_depIdxs,
		MessageInfos:      file_uac_FeatureFlags_proto_msgTypes,
	}.Build()
	File_uac_FeatureFlags_proto = out.File
	file_uac_FeatureFlags_proto_rawDesc = nil
	file_uac_FeatureFlags_proto_goTypes = nil
	file_uac_FeatureFlags_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// FeatureFlagsServiceClient is the client API for FeatureFlagsService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type FeatureFlagsServiceClient interface {
	GetFeatureFlags(ctx context.Context, in *FeatureFlagsRequest, opts ...grpc.CallOption) (*FeatureFlagsRequest_Response, error)
}

type featureFlagsServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewFeatureFlagsServiceClient(cc grpc.ClientConnInterface) FeatureFlagsServiceClient {
	return &featureFlagsServiceClient{cc}
}

func (c *featureFlagsServiceClient) GetFeatureFlags(ctx context.Context, in *FeatureFlagsRequest, opts ...grpc.CallOption) (*FeatureFlagsRequest_Response, error) {
	out := new(FeatureFlagsRequest_Response)
	err := c.cc.Invoke(ctx, "/ai.verta.uac.FeatureFlagsService/getFeatureFlags", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// FeatureFlagsServiceServer is the server API for FeatureFlagsService service.
type FeatureFlagsServiceServer interface {
	GetFeatureFlags(context.Context, *FeatureFlagsRequest) (*FeatureFlagsRequest_Response, error)
}

// UnimplementedFeatureFlagsServiceServer can be embedded to have forward compatible implementations.
type UnimplementedFeatureFlagsServiceServer struct {
}

func (*UnimplementedFeatureFlagsServiceServer) GetFeatureFlags(context.Context, *FeatureFlagsRequest) (*FeatureFlagsRequest_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFeatureFlags not implemented")
}

func RegisterFeatureFlagsServiceServer(s *grpc.Server, srv FeatureFlagsServiceServer) {
	s.RegisterService(&_FeatureFlagsService_serviceDesc, srv)
}

func _FeatureFlagsService_GetFeatureFlags_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FeatureFlagsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(FeatureFlagsServiceServer).GetFeatureFlags(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.uac.FeatureFlagsService/GetFeatureFlags",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(FeatureFlagsServiceServer).GetFeatureFlags(ctx, req.(*FeatureFlagsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _FeatureFlagsService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "ai.verta.uac.FeatureFlagsService",
	HandlerType: (*FeatureFlagsServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "getFeatureFlags",
			Handler:    _FeatureFlagsService_GetFeatureFlags_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "uac/FeatureFlags.proto",
}
