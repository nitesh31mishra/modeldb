// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v3.21.6
// source: monitoring/Schema.proto

package monitoring

import (
	_ "github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	_ "google.golang.org/protobuf/types/known/structpb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type FeatureSchema_Type int32

const (
	FeatureSchema_UNDEFINED FeatureSchema_Type = 0
	FeatureSchema_STRING    FeatureSchema_Type = 1
	FeatureSchema_LONG      FeatureSchema_Type = 2
	FeatureSchema_DOUBLE    FeatureSchema_Type = 3
	FeatureSchema_BOOLEAN   FeatureSchema_Type = 4
)

// Enum value maps for FeatureSchema_Type.
var (
	FeatureSchema_Type_name = map[int32]string{
		0: "UNDEFINED",
		1: "STRING",
		2: "LONG",
		3: "DOUBLE",
		4: "BOOLEAN",
	}
	FeatureSchema_Type_value = map[string]int32{
		"UNDEFINED": 0,
		"STRING":    1,
		"LONG":      2,
		"DOUBLE":    3,
		"BOOLEAN":   4,
	}
)

func (x FeatureSchema_Type) Enum() *FeatureSchema_Type {
	p := new(FeatureSchema_Type)
	*p = x
	return p
}

func (x FeatureSchema_Type) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (FeatureSchema_Type) Descriptor() protoreflect.EnumDescriptor {
	return file_monitoring_Schema_proto_enumTypes[0].Descriptor()
}

func (FeatureSchema_Type) Type() protoreflect.EnumType {
	return &file_monitoring_Schema_proto_enumTypes[0]
}

func (x FeatureSchema_Type) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use FeatureSchema_Type.Descriptor instead.
func (FeatureSchema_Type) EnumDescriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{1, 0}
}

type Schema struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	MonitoredEntityId uint64                    `protobuf:"varint,1,opt,name=monitored_entity_id,json=monitoredEntityId,proto3" json:"monitored_entity_id,omitempty"`
	Version           uint64                    `protobuf:"varint,2,opt,name=version,proto3" json:"version,omitempty"`
	CreatedAtMillis   uint64                    `protobuf:"varint,3,opt,name=created_at_millis,json=createdAtMillis,proto3" json:"created_at_millis,omitempty"`
	Features          map[string]*FeatureSchema `protobuf:"bytes,4,rep,name=features,proto3" json:"features,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *Schema) Reset() {
	*x = Schema{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Schema) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Schema) ProtoMessage() {}

func (x *Schema) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Schema.ProtoReflect.Descriptor instead.
func (*Schema) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{0}
}

func (x *Schema) GetMonitoredEntityId() uint64 {
	if x != nil {
		return x.MonitoredEntityId
	}
	return 0
}

func (x *Schema) GetVersion() uint64 {
	if x != nil {
		return x.Version
	}
	return 0
}

func (x *Schema) GetCreatedAtMillis() uint64 {
	if x != nil {
		return x.CreatedAtMillis
	}
	return 0
}

func (x *Schema) GetFeatures() map[string]*FeatureSchema {
	if x != nil {
		return x.Features
	}
	return nil
}

type FeatureSchema struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type FeatureSchema_Type `protobuf:"varint,1,opt,name=type,proto3,enum=ai.verta.monitoring.FeatureSchema_Type" json:"type,omitempty"`
}

func (x *FeatureSchema) Reset() {
	*x = FeatureSchema{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FeatureSchema) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeatureSchema) ProtoMessage() {}

func (x *FeatureSchema) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeatureSchema.ProtoReflect.Descriptor instead.
func (*FeatureSchema) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{1}
}

func (x *FeatureSchema) GetType() FeatureSchema_Type {
	if x != nil {
		return x.Type
	}
	return FeatureSchema_UNDEFINED
}

type CreateSchema struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	MonitoredEntityId uint64                    `protobuf:"varint,1,opt,name=monitored_entity_id,json=monitoredEntityId,proto3" json:"monitored_entity_id,omitempty"`
	Features          map[string]*FeatureSchema `protobuf:"bytes,2,rep,name=features,proto3" json:"features,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *CreateSchema) Reset() {
	*x = CreateSchema{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CreateSchema) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateSchema) ProtoMessage() {}

func (x *CreateSchema) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateSchema.ProtoReflect.Descriptor instead.
func (*CreateSchema) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{2}
}

func (x *CreateSchema) GetMonitoredEntityId() uint64 {
	if x != nil {
		return x.MonitoredEntityId
	}
	return 0
}

func (x *CreateSchema) GetFeatures() map[string]*FeatureSchema {
	if x != nil {
		return x.Features
	}
	return nil
}

type UpdateSchema struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Schema *Schema `protobuf:"bytes,1,opt,name=schema,proto3" json:"schema,omitempty"`
}

func (x *UpdateSchema) Reset() {
	*x = UpdateSchema{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdateSchema) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateSchema) ProtoMessage() {}

func (x *UpdateSchema) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateSchema.ProtoReflect.Descriptor instead.
func (*UpdateSchema) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{3}
}

func (x *UpdateSchema) GetSchema() *Schema {
	if x != nil {
		return x.Schema
	}
	return nil
}

type FindSchemas struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	FindEntities *FindMonitoredEntityRequest `protobuf:"bytes,1,opt,name=find_entities,json=findEntities,proto3" json:"find_entities,omitempty"`
	Versions     []uint64                    `protobuf:"varint,2,rep,packed,name=versions,proto3" json:"versions,omitempty"`
}

func (x *FindSchemas) Reset() {
	*x = FindSchemas{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FindSchemas) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FindSchemas) ProtoMessage() {}

func (x *FindSchemas) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FindSchemas.ProtoReflect.Descriptor instead.
func (*FindSchemas) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{4}
}

func (x *FindSchemas) GetFindEntities() *FindMonitoredEntityRequest {
	if x != nil {
		return x.FindEntities
	}
	return nil
}

func (x *FindSchemas) GetVersions() []uint64 {
	if x != nil {
		return x.Versions
	}
	return nil
}

type DeleteSchema struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	MonitoredEntityId uint64 `protobuf:"varint,1,opt,name=monitored_entity_id,json=monitoredEntityId,proto3" json:"monitored_entity_id,omitempty"`
}

func (x *DeleteSchema) Reset() {
	*x = DeleteSchema{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DeleteSchema) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DeleteSchema) ProtoMessage() {}

func (x *DeleteSchema) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DeleteSchema.ProtoReflect.Descriptor instead.
func (*DeleteSchema) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{5}
}

func (x *DeleteSchema) GetMonitoredEntityId() uint64 {
	if x != nil {
		return x.MonitoredEntityId
	}
	return 0
}

type CreateSchema_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Schema *Schema `protobuf:"bytes,1,opt,name=schema,proto3" json:"schema,omitempty"`
}

func (x *CreateSchema_Response) Reset() {
	*x = CreateSchema_Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[8]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CreateSchema_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateSchema_Response) ProtoMessage() {}

func (x *CreateSchema_Response) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[8]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateSchema_Response.ProtoReflect.Descriptor instead.
func (*CreateSchema_Response) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{2, 1}
}

func (x *CreateSchema_Response) GetSchema() *Schema {
	if x != nil {
		return x.Schema
	}
	return nil
}

type UpdateSchema_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Schema *Schema `protobuf:"bytes,1,opt,name=schema,proto3" json:"schema,omitempty"`
}

func (x *UpdateSchema_Response) Reset() {
	*x = UpdateSchema_Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[9]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdateSchema_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateSchema_Response) ProtoMessage() {}

func (x *UpdateSchema_Response) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[9]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateSchema_Response.ProtoReflect.Descriptor instead.
func (*UpdateSchema_Response) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{3, 0}
}

func (x *UpdateSchema_Response) GetSchema() *Schema {
	if x != nil {
		return x.Schema
	}
	return nil
}

type FindSchemas_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Schemas []*Schema `protobuf:"bytes,1,rep,name=schemas,proto3" json:"schemas,omitempty"`
}

func (x *FindSchemas_Response) Reset() {
	*x = FindSchemas_Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[10]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FindSchemas_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FindSchemas_Response) ProtoMessage() {}

func (x *FindSchemas_Response) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[10]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FindSchemas_Response.ProtoReflect.Descriptor instead.
func (*FindSchemas_Response) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{4, 0}
}

func (x *FindSchemas_Response) GetSchemas() []*Schema {
	if x != nil {
		return x.Schemas
	}
	return nil
}

type DeleteSchema_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *DeleteSchema_Response) Reset() {
	*x = DeleteSchema_Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_monitoring_Schema_proto_msgTypes[11]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DeleteSchema_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DeleteSchema_Response) ProtoMessage() {}

func (x *DeleteSchema_Response) ProtoReflect() protoreflect.Message {
	mi := &file_monitoring_Schema_proto_msgTypes[11]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DeleteSchema_Response.ProtoReflect.Descriptor instead.
func (*DeleteSchema_Response) Descriptor() ([]byte, []int) {
	return file_monitoring_Schema_proto_rawDescGZIP(), []int{5, 0}
}

var File_monitoring_Schema_proto protoreflect.FileDescriptor

var file_monitoring_Schema_proto_rawDesc = []byte{
	0x0a, 0x17, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2f, 0x53, 0x63, 0x68,
	0x65, 0x6d, 0x61, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x13, 0x61, 0x69, 0x2e, 0x76, 0x65,
	0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x1a, 0x16,
	0x75, 0x61, 0x63, 0x2f, 0x43, 0x6f, 0x6c, 0x6c, 0x61, 0x62, 0x6f, 0x72, 0x61, 0x74, 0x6f, 0x72,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x20, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2f, 0x4d,
	0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0xa6, 0x02, 0x0a, 0x06, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x12,
	0x2e, 0x0a, 0x13, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x5f, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x04, 0x52, 0x11, 0x6d, 0x6f,
	0x6e, 0x69, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x49, 0x64, 0x12,
	0x18, 0x0a, 0x07, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x04,
	0x52, 0x07, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x12, 0x2a, 0x0a, 0x11, 0x63, 0x72, 0x65,
	0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x5f, 0x6d, 0x69, 0x6c, 0x6c, 0x69, 0x73, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x04, 0x52, 0x0f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x4d,
	0x69, 0x6c, 0x6c, 0x69, 0x73, 0x12, 0x45, 0x0a, 0x08, 0x66, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65,
	0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x29, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72,
	0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63,
	0x68, 0x65, 0x6d, 0x61, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x45, 0x6e, 0x74,
	0x72, 0x79, 0x52, 0x08, 0x66, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x1a, 0x5f, 0x0a, 0x0d,
	0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a,
	0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12,
	0x38, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22,
	0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f,
	0x72, 0x69, 0x6e, 0x67, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x63, 0x68, 0x65,
	0x6d, 0x61, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0x92, 0x01,
	0x0a, 0x0d, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x12,
	0x3b, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x27, 0x2e,
	0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72,
	0x69, 0x6e, 0x67, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x2e, 0x54, 0x79, 0x70, 0x65, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x22, 0x44, 0x0a, 0x04,
	0x54, 0x79, 0x70, 0x65, 0x12, 0x0d, 0x0a, 0x09, 0x55, 0x4e, 0x44, 0x45, 0x46, 0x49, 0x4e, 0x45,
	0x44, 0x10, 0x00, 0x12, 0x0a, 0x0a, 0x06, 0x53, 0x54, 0x52, 0x49, 0x4e, 0x47, 0x10, 0x01, 0x12,
	0x08, 0x0a, 0x04, 0x4c, 0x4f, 0x4e, 0x47, 0x10, 0x02, 0x12, 0x0a, 0x0a, 0x06, 0x44, 0x4f, 0x55,
	0x42, 0x4c, 0x45, 0x10, 0x03, 0x12, 0x0b, 0x0a, 0x07, 0x42, 0x4f, 0x4f, 0x4c, 0x45, 0x41, 0x4e,
	0x10, 0x04, 0x22, 0xad, 0x02, 0x0a, 0x0c, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68,
	0x65, 0x6d, 0x61, 0x12, 0x2e, 0x0a, 0x13, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x65, 0x64,
	0x5f, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x04,
	0x52, 0x11, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x45, 0x6e, 0x74, 0x69, 0x74,
	0x79, 0x49, 0x64, 0x12, 0x4b, 0x0a, 0x08, 0x66, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x18,
	0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2f, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61,
	0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x43, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65,
	0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x08, 0x66, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73,
	0x1a, 0x5f, 0x0a, 0x0d, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x45, 0x6e, 0x74, 0x72,
	0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03,
	0x6b, 0x65, 0x79, 0x12, 0x38, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x22, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f,
	0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x46, 0x65, 0x61, 0x74, 0x75, 0x72, 0x65,
	0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38,
	0x01, 0x1a, 0x3f, 0x0a, 0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x33, 0x0a,
	0x06, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1b, 0x2e,
	0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72,
	0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x52, 0x06, 0x73, 0x63, 0x68, 0x65,
	0x6d, 0x61, 0x22, 0x84, 0x01, 0x0a, 0x0c, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68,
	0x65, 0x6d, 0x61, 0x12, 0x33, 0x0a, 0x06, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d,
	0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61,
	0x52, 0x06, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x1a, 0x3f, 0x0a, 0x08, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x33, 0x0a, 0x06, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e,
	0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x52, 0x06, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x22, 0xc2, 0x01, 0x0a, 0x0b, 0x46, 0x69,
	0x6e, 0x64, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x73, 0x12, 0x54, 0x0a, 0x0d, 0x66, 0x69, 0x6e,
	0x64, 0x5f, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x2f, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69,
	0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x46, 0x69, 0x6e, 0x64, 0x4d, 0x6f, 0x6e, 0x69, 0x74,
	0x6f, 0x72, 0x65, 0x64, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x52, 0x0c, 0x66, 0x69, 0x6e, 0x64, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x69, 0x65, 0x73, 0x12,
	0x1a, 0x0a, 0x08, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28,
	0x04, 0x52, 0x08, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x73, 0x1a, 0x41, 0x0a, 0x08, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x35, 0x0a, 0x07, 0x73, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65,
	0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x53,
	0x63, 0x68, 0x65, 0x6d, 0x61, 0x52, 0x07, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x73, 0x22, 0x4a,
	0x0a, 0x0c, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x12, 0x2e,
	0x0a, 0x13, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x5f, 0x65, 0x6e, 0x74, 0x69,
	0x74, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x04, 0x52, 0x11, 0x6d, 0x6f, 0x6e,
	0x69, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x49, 0x64, 0x1a, 0x0a,
	0x0a, 0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x32, 0xa7, 0x04, 0x0a, 0x0d, 0x53,
	0x63, 0x68, 0x65, 0x6d, 0x61, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x81, 0x01, 0x0a,
	0x0c, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x12, 0x21, 0x2e,
	0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72,
	0x69, 0x6e, 0x67, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61,
	0x1a, 0x1b, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e, 0x69,
	0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x22, 0x31, 0x82,
	0xd3, 0xe4, 0x93, 0x02, 0x2b, 0x22, 0x26, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x6d,
	0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2f, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61,
	0x2f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x3a, 0x01, 0x2a,
	0x12, 0x81, 0x01, 0x0a, 0x0c, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x12, 0x21, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x6e,
	0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x53, 0x63,
	0x68, 0x65, 0x6d, 0x61, 0x1a, 0x1b, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e,
	0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x22, 0x31, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x2b, 0x22, 0x26, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x76, 0x31, 0x2f, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2f, 0x73, 0x63,
	0x68, 0x65, 0x6d, 0x61, 0x2f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x3a, 0x01, 0x2a, 0x12, 0x8a, 0x01, 0x0a, 0x0a, 0x66, 0x69, 0x6e, 0x64, 0x53, 0x63, 0x68,
	0x65, 0x6d, 0x61, 0x12, 0x20, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d,
	0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x46, 0x69, 0x6e, 0x64, 0x53, 0x63,
	0x68, 0x65, 0x6d, 0x61, 0x73, 0x1a, 0x29, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61,
	0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x46, 0x69, 0x6e, 0x64,
	0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x73, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x22, 0x2f, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x29, 0x22, 0x24, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76,
	0x31, 0x2f, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2f, 0x73, 0x63, 0x68,
	0x65, 0x6d, 0x61, 0x2f, 0x66, 0x69, 0x6e, 0x64, 0x53, 0x63, 0x68, 0x65, 0x6d, 0x61, 0x3a, 0x01,
	0x2a, 0x12, 0x80, 0x01, 0x0a, 0x0c, 0x64, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65,
	0x6d, 0x61, 0x12, 0x21, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f,
	0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x53,
	0x63, 0x68, 0x65, 0x6d, 0x61, 0x1a, 0x1a, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61,
	0x2e, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2e, 0x45, 0x6d, 0x70, 0x74,
	0x79, 0x22, 0x31, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x2b, 0x2a, 0x26, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x76, 0x31, 0x2f, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x2f, 0x73, 0x63,
	0x68, 0x65, 0x6d, 0x61, 0x2f, 0x64, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x53, 0x63, 0x68, 0x65, 0x6d,
	0x61, 0x3a, 0x01, 0x2a, 0x42, 0x45, 0x50, 0x01, 0x5a, 0x41, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x56, 0x65, 0x72, 0x74, 0x61, 0x41, 0x49, 0x2f, 0x6d, 0x6f, 0x64,
	0x65, 0x6c, 0x64, 0x62, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x67, 0x65, 0x6e, 0x2f,
	0x67, 0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63,
	0x2f, 0x6d, 0x6f, 0x6e, 0x69, 0x74, 0x6f, 0x72, 0x69, 0x6e, 0x67, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_monitoring_Schema_proto_rawDescOnce sync.Once
	file_monitoring_Schema_proto_rawDescData = file_monitoring_Schema_proto_rawDesc
)

func file_monitoring_Schema_proto_rawDescGZIP() []byte {
	file_monitoring_Schema_proto_rawDescOnce.Do(func() {
		file_monitoring_Schema_proto_rawDescData = protoimpl.X.CompressGZIP(file_monitoring_Schema_proto_rawDescData)
	})
	return file_monitoring_Schema_proto_rawDescData
}

var file_monitoring_Schema_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_monitoring_Schema_proto_msgTypes = make([]protoimpl.MessageInfo, 12)
var file_monitoring_Schema_proto_goTypes = []interface{}{
	(FeatureSchema_Type)(0),            // 0: ai.verta.monitoring.FeatureSchema.Type
	(*Schema)(nil),                     // 1: ai.verta.monitoring.Schema
	(*FeatureSchema)(nil),              // 2: ai.verta.monitoring.FeatureSchema
	(*CreateSchema)(nil),               // 3: ai.verta.monitoring.CreateSchema
	(*UpdateSchema)(nil),               // 4: ai.verta.monitoring.UpdateSchema
	(*FindSchemas)(nil),                // 5: ai.verta.monitoring.FindSchemas
	(*DeleteSchema)(nil),               // 6: ai.verta.monitoring.DeleteSchema
	nil,                                // 7: ai.verta.monitoring.Schema.FeaturesEntry
	nil,                                // 8: ai.verta.monitoring.CreateSchema.FeaturesEntry
	(*CreateSchema_Response)(nil),      // 9: ai.verta.monitoring.CreateSchema.Response
	(*UpdateSchema_Response)(nil),      // 10: ai.verta.monitoring.UpdateSchema.Response
	(*FindSchemas_Response)(nil),       // 11: ai.verta.monitoring.FindSchemas.Response
	(*DeleteSchema_Response)(nil),      // 12: ai.verta.monitoring.DeleteSchema.Response
	(*FindMonitoredEntityRequest)(nil), // 13: ai.verta.monitoring.FindMonitoredEntityRequest
	(*Empty)(nil),                      // 14: ai.verta.monitoring.Empty
}
var file_monitoring_Schema_proto_depIdxs = []int32{
	7,  // 0: ai.verta.monitoring.Schema.features:type_name -> ai.verta.monitoring.Schema.FeaturesEntry
	0,  // 1: ai.verta.monitoring.FeatureSchema.type:type_name -> ai.verta.monitoring.FeatureSchema.Type
	8,  // 2: ai.verta.monitoring.CreateSchema.features:type_name -> ai.verta.monitoring.CreateSchema.FeaturesEntry
	1,  // 3: ai.verta.monitoring.UpdateSchema.schema:type_name -> ai.verta.monitoring.Schema
	13, // 4: ai.verta.monitoring.FindSchemas.find_entities:type_name -> ai.verta.monitoring.FindMonitoredEntityRequest
	2,  // 5: ai.verta.monitoring.Schema.FeaturesEntry.value:type_name -> ai.verta.monitoring.FeatureSchema
	2,  // 6: ai.verta.monitoring.CreateSchema.FeaturesEntry.value:type_name -> ai.verta.monitoring.FeatureSchema
	1,  // 7: ai.verta.monitoring.CreateSchema.Response.schema:type_name -> ai.verta.monitoring.Schema
	1,  // 8: ai.verta.monitoring.UpdateSchema.Response.schema:type_name -> ai.verta.monitoring.Schema
	1,  // 9: ai.verta.monitoring.FindSchemas.Response.schemas:type_name -> ai.verta.monitoring.Schema
	3,  // 10: ai.verta.monitoring.SchemaService.createSchema:input_type -> ai.verta.monitoring.CreateSchema
	4,  // 11: ai.verta.monitoring.SchemaService.updateSchema:input_type -> ai.verta.monitoring.UpdateSchema
	5,  // 12: ai.verta.monitoring.SchemaService.findSchema:input_type -> ai.verta.monitoring.FindSchemas
	6,  // 13: ai.verta.monitoring.SchemaService.deleteSchema:input_type -> ai.verta.monitoring.DeleteSchema
	1,  // 14: ai.verta.monitoring.SchemaService.createSchema:output_type -> ai.verta.monitoring.Schema
	1,  // 15: ai.verta.monitoring.SchemaService.updateSchema:output_type -> ai.verta.monitoring.Schema
	11, // 16: ai.verta.monitoring.SchemaService.findSchema:output_type -> ai.verta.monitoring.FindSchemas.Response
	14, // 17: ai.verta.monitoring.SchemaService.deleteSchema:output_type -> ai.verta.monitoring.Empty
	14, // [14:18] is the sub-list for method output_type
	10, // [10:14] is the sub-list for method input_type
	10, // [10:10] is the sub-list for extension type_name
	10, // [10:10] is the sub-list for extension extendee
	0,  // [0:10] is the sub-list for field type_name
}

func init() { file_monitoring_Schema_proto_init() }
func file_monitoring_Schema_proto_init() {
	if File_monitoring_Schema_proto != nil {
		return
	}
	file_monitoring_MonitoredEntity_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_monitoring_Schema_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Schema); i {
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
		file_monitoring_Schema_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FeatureSchema); i {
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
		file_monitoring_Schema_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CreateSchema); i {
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
		file_monitoring_Schema_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdateSchema); i {
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
		file_monitoring_Schema_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FindSchemas); i {
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
		file_monitoring_Schema_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DeleteSchema); i {
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
		file_monitoring_Schema_proto_msgTypes[8].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CreateSchema_Response); i {
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
		file_monitoring_Schema_proto_msgTypes[9].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdateSchema_Response); i {
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
		file_monitoring_Schema_proto_msgTypes[10].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FindSchemas_Response); i {
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
		file_monitoring_Schema_proto_msgTypes[11].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DeleteSchema_Response); i {
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
			RawDescriptor: file_monitoring_Schema_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   12,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_monitoring_Schema_proto_goTypes,
		DependencyIndexes: file_monitoring_Schema_proto_depIdxs,
		EnumInfos:         file_monitoring_Schema_proto_enumTypes,
		MessageInfos:      file_monitoring_Schema_proto_msgTypes,
	}.Build()
	File_monitoring_Schema_proto = out.File
	file_monitoring_Schema_proto_rawDesc = nil
	file_monitoring_Schema_proto_goTypes = nil
	file_monitoring_Schema_proto_depIdxs = nil
}
