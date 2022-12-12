// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.11.2
// source: registry/ChecklistService.proto

package registry

import (
	context "context"
	proto "github.com/golang/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	_ "google.golang.org/genproto/protobuf/field_mask"
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

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type ChecklistItemValue struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// internal id
	Id uint64 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	// value corresponds to if the item was marked as completed
	Completed bool `protobuf:"varint,2,opt,name=completed,proto3" json:"completed,omitempty"`
	// value corresponds to user given evidence
	Evidence string `protobuf:"bytes,3,opt,name=evidence,proto3" json:"evidence,omitempty"`
	// id of the model version this belongs to
	ModelVersionId uint64 `protobuf:"varint,4,opt,name=model_version_id,json=modelVersionId,proto3" json:"model_version_id,omitempty"`
	// id of the template(UAC) this is related to
	ChecklistTemplateId uint64 `protobuf:"varint,5,opt,name=checklist_template_id,json=checklistTemplateId,proto3" json:"checklist_template_id,omitempty"`
	// id of the template item (UAC) this is related to
	ChecklistTemplateItemId uint64 `protobuf:"varint,6,opt,name=checklist_template_item_id,json=checklistTemplateItemId,proto3" json:"checklist_template_item_id,omitempty"`
	// Timestamp recorded when this entity was created
	TimeCreated int64 `protobuf:"varint,7,opt,name=time_created,json=timeCreated,proto3" json:"time_created,omitempty"`
	// Timestamp recorded when metadata for this entity was last updated
	TimeUpdated int64 `protobuf:"varint,8,opt,name=time_updated,json=timeUpdated,proto3" json:"time_updated,omitempty"`
	// id of user(UAC) that created this entity
	CreatedById uint64 `protobuf:"varint,9,opt,name=created_by_id,json=createdById,proto3" json:"created_by_id,omitempty"`
	// id of user(UAC) that updated this entity
	UpdatedById uint64 `protobuf:"varint,10,opt,name=updated_by_id,json=updatedById,proto3" json:"updated_by_id,omitempty"`
}

func (x *ChecklistItemValue) Reset() {
	*x = ChecklistItemValue{}
	if protoimpl.UnsafeEnabled {
		mi := &file_registry_ChecklistService_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ChecklistItemValue) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ChecklistItemValue) ProtoMessage() {}

func (x *ChecklistItemValue) ProtoReflect() protoreflect.Message {
	mi := &file_registry_ChecklistService_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ChecklistItemValue.ProtoReflect.Descriptor instead.
func (*ChecklistItemValue) Descriptor() ([]byte, []int) {
	return file_registry_ChecklistService_proto_rawDescGZIP(), []int{0}
}

func (x *ChecklistItemValue) GetId() uint64 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *ChecklistItemValue) GetCompleted() bool {
	if x != nil {
		return x.Completed
	}
	return false
}

func (x *ChecklistItemValue) GetEvidence() string {
	if x != nil {
		return x.Evidence
	}
	return ""
}

func (x *ChecklistItemValue) GetModelVersionId() uint64 {
	if x != nil {
		return x.ModelVersionId
	}
	return 0
}

func (x *ChecklistItemValue) GetChecklistTemplateId() uint64 {
	if x != nil {
		return x.ChecklistTemplateId
	}
	return 0
}

func (x *ChecklistItemValue) GetChecklistTemplateItemId() uint64 {
	if x != nil {
		return x.ChecklistTemplateItemId
	}
	return 0
}

func (x *ChecklistItemValue) GetTimeCreated() int64 {
	if x != nil {
		return x.TimeCreated
	}
	return 0
}

func (x *ChecklistItemValue) GetTimeUpdated() int64 {
	if x != nil {
		return x.TimeUpdated
	}
	return 0
}

func (x *ChecklistItemValue) GetCreatedById() uint64 {
	if x != nil {
		return x.CreatedById
	}
	return 0
}

func (x *ChecklistItemValue) GetUpdatedById() uint64 {
	if x != nil {
		return x.UpdatedById
	}
	return 0
}

type SearchChecklistItemValues struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// identity of parent registered model version
	ModelVersionId string `protobuf:"bytes,1,opt,name=model_version_id,json=modelVersionId,proto3" json:"model_version_id,omitempty"`
}

func (x *SearchChecklistItemValues) Reset() {
	*x = SearchChecklistItemValues{}
	if protoimpl.UnsafeEnabled {
		mi := &file_registry_ChecklistService_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SearchChecklistItemValues) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SearchChecklistItemValues) ProtoMessage() {}

func (x *SearchChecklistItemValues) ProtoReflect() protoreflect.Message {
	mi := &file_registry_ChecklistService_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SearchChecklistItemValues.ProtoReflect.Descriptor instead.
func (*SearchChecklistItemValues) Descriptor() ([]byte, []int) {
	return file_registry_ChecklistService_proto_rawDescGZIP(), []int{1}
}

func (x *SearchChecklistItemValues) GetModelVersionId() string {
	if x != nil {
		return x.ModelVersionId
	}
	return ""
}

type SearchChecklistItemValues_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ChecklistItemValues []*ChecklistItemValue `protobuf:"bytes,1,rep,name=checklist_item_values,json=checklistItemValues,proto3" json:"checklist_item_values,omitempty"`
}

func (x *SearchChecklistItemValues_Response) Reset() {
	*x = SearchChecklistItemValues_Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_registry_ChecklistService_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SearchChecklistItemValues_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SearchChecklistItemValues_Response) ProtoMessage() {}

func (x *SearchChecklistItemValues_Response) ProtoReflect() protoreflect.Message {
	mi := &file_registry_ChecklistService_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SearchChecklistItemValues_Response.ProtoReflect.Descriptor instead.
func (*SearchChecklistItemValues_Response) Descriptor() ([]byte, []int) {
	return file_registry_ChecklistService_proto_rawDescGZIP(), []int{1, 0}
}

func (x *SearchChecklistItemValues_Response) GetChecklistItemValues() []*ChecklistItemValue {
	if x != nil {
		return x.ChecklistItemValues
	}
	return nil
}

var File_registry_ChecklistService_proto protoreflect.FileDescriptor

var file_registry_ChecklistService_proto_rawDesc = []byte{
	0x0a, 0x1f, 0x72, 0x65, 0x67, 0x69, 0x73, 0x74, 0x72, 0x79, 0x2f, 0x43, 0x68, 0x65, 0x63, 0x6b,
	0x6c, 0x69, 0x73, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x11, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x72, 0x65, 0x67, 0x69,
	0x73, 0x74, 0x72, 0x79, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x20, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x5f, 0x6d, 0x61, 0x73, 0x6b, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0x87, 0x03, 0x0a, 0x12, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69,
	0x73, 0x74, 0x49, 0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x12, 0x0e, 0x0a, 0x02, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x04, 0x52, 0x02, 0x69, 0x64, 0x12, 0x1c, 0x0a, 0x09, 0x63,
	0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x65, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09,
	0x63, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x65, 0x64, 0x12, 0x1a, 0x0a, 0x08, 0x65, 0x76, 0x69,
	0x64, 0x65, 0x6e, 0x63, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x65, 0x76, 0x69,
	0x64, 0x65, 0x6e, 0x63, 0x65, 0x12, 0x28, 0x0a, 0x10, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x5f, 0x76,
	0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x04, 0x20, 0x01, 0x28, 0x04, 0x52,
	0x0e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x12,
	0x32, 0x0a, 0x15, 0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x5f, 0x74, 0x65, 0x6d,
	0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x05, 0x20, 0x01, 0x28, 0x04, 0x52, 0x13,
	0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x54, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74,
	0x65, 0x49, 0x64, 0x12, 0x3b, 0x0a, 0x1a, 0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74,
	0x5f, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x74, 0x65, 0x6d, 0x5f, 0x69,
	0x64, 0x18, 0x06, 0x20, 0x01, 0x28, 0x04, 0x52, 0x17, 0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69,
	0x73, 0x74, 0x54, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x74, 0x65, 0x6d, 0x49, 0x64,
	0x12, 0x21, 0x0a, 0x0c, 0x74, 0x69, 0x6d, 0x65, 0x5f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64,
	0x18, 0x07, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0b, 0x74, 0x69, 0x6d, 0x65, 0x43, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x64, 0x12, 0x21, 0x0a, 0x0c, 0x74, 0x69, 0x6d, 0x65, 0x5f, 0x75, 0x70, 0x64, 0x61,
	0x74, 0x65, 0x64, 0x18, 0x08, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0b, 0x74, 0x69, 0x6d, 0x65, 0x55,
	0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x12, 0x22, 0x0a, 0x0d, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x64, 0x5f, 0x62, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x09, 0x20, 0x01, 0x28, 0x04, 0x52, 0x0b, 0x63,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x42, 0x79, 0x49, 0x64, 0x12, 0x22, 0x0a, 0x0d, 0x75, 0x70,
	0x64, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x62, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x0a, 0x20, 0x01, 0x28,
	0x04, 0x52, 0x0b, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x42, 0x79, 0x49, 0x64, 0x22, 0xac,
	0x01, 0x0a, 0x19, 0x53, 0x65, 0x61, 0x72, 0x63, 0x68, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69,
	0x73, 0x74, 0x49, 0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x12, 0x28, 0x0a, 0x10,
	0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x5f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x56, 0x65, 0x72,
	0x73, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x1a, 0x65, 0x0a, 0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x12, 0x59, 0x0a, 0x15, 0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x5f,
	0x69, 0x74, 0x65, 0x6d, 0x5f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x25, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x72, 0x65, 0x67,
	0x69, 0x73, 0x74, 0x72, 0x79, 0x2e, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x49,
	0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x13, 0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c,
	0x69, 0x73, 0x74, 0x49, 0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x32, 0x9f, 0x02,
	0x0a, 0x10, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69,
	0x63, 0x65, 0x12, 0x8a, 0x02, 0x0a, 0x19, 0x73, 0x65, 0x61, 0x72, 0x63, 0x68, 0x43, 0x68, 0x65,
	0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x49, 0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73,
	0x12, 0x2c, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x72, 0x65, 0x67, 0x69,
	0x73, 0x74, 0x72, 0x79, 0x2e, 0x53, 0x65, 0x61, 0x72, 0x63, 0x68, 0x43, 0x68, 0x65, 0x63, 0x6b,
	0x6c, 0x69, 0x73, 0x74, 0x49, 0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x1a, 0x35,
	0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x72, 0x65, 0x67, 0x69, 0x73, 0x74,
	0x72, 0x79, 0x2e, 0x53, 0x65, 0x61, 0x72, 0x63, 0x68, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69,
	0x73, 0x74, 0x49, 0x74, 0x65, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2e, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x87, 0x01, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x80, 0x01, 0x22,
	0x29, 0x2f, 0x76, 0x31, 0x2f, 0x72, 0x65, 0x67, 0x69, 0x73, 0x74, 0x72, 0x79, 0x2f, 0x63, 0x68,
	0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x5f, 0x69, 0x74, 0x65, 0x6d, 0x5f, 0x76, 0x61, 0x6c,
	0x75, 0x65, 0x73, 0x2f, 0x73, 0x65, 0x61, 0x72, 0x63, 0x68, 0x3a, 0x01, 0x2a, 0x5a, 0x50, 0x22,
	0x4b, 0x2f, 0x76, 0x31, 0x2f, 0x72, 0x65, 0x67, 0x69, 0x73, 0x74, 0x72, 0x79, 0x2f, 0x6d, 0x6f,
	0x64, 0x65, 0x6c, 0x5f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x73, 0x2f, 0x7b, 0x6d, 0x6f,
	0x64, 0x65, 0x6c, 0x5f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x7d, 0x2f,
	0x63, 0x68, 0x65, 0x63, 0x6b, 0x6c, 0x69, 0x73, 0x74, 0x5f, 0x69, 0x74, 0x65, 0x6d, 0x5f, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x73, 0x2f, 0x73, 0x65, 0x61, 0x72, 0x63, 0x68, 0x3a, 0x01, 0x2a, 0x42,
	0x43, 0x50, 0x01, 0x5a, 0x3f, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x56, 0x65, 0x72, 0x74, 0x61, 0x41, 0x49, 0x2f, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x2f, 0x72, 0x65, 0x67, 0x69,
	0x73, 0x74, 0x72, 0x79, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_registry_ChecklistService_proto_rawDescOnce sync.Once
	file_registry_ChecklistService_proto_rawDescData = file_registry_ChecklistService_proto_rawDesc
)

func file_registry_ChecklistService_proto_rawDescGZIP() []byte {
	file_registry_ChecklistService_proto_rawDescOnce.Do(func() {
		file_registry_ChecklistService_proto_rawDescData = protoimpl.X.CompressGZIP(file_registry_ChecklistService_proto_rawDescData)
	})
	return file_registry_ChecklistService_proto_rawDescData
}

var file_registry_ChecklistService_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_registry_ChecklistService_proto_goTypes = []interface{}{
	(*ChecklistItemValue)(nil),                 // 0: ai.verta.registry.ChecklistItemValue
	(*SearchChecklistItemValues)(nil),          // 1: ai.verta.registry.SearchChecklistItemValues
	(*SearchChecklistItemValues_Response)(nil), // 2: ai.verta.registry.SearchChecklistItemValues.Response
}
var file_registry_ChecklistService_proto_depIdxs = []int32{
	0, // 0: ai.verta.registry.SearchChecklistItemValues.Response.checklist_item_values:type_name -> ai.verta.registry.ChecklistItemValue
	1, // 1: ai.verta.registry.ChecklistService.searchChecklistItemValues:input_type -> ai.verta.registry.SearchChecklistItemValues
	2, // 2: ai.verta.registry.ChecklistService.searchChecklistItemValues:output_type -> ai.verta.registry.SearchChecklistItemValues.Response
	2, // [2:3] is the sub-list for method output_type
	1, // [1:2] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_registry_ChecklistService_proto_init() }
func file_registry_ChecklistService_proto_init() {
	if File_registry_ChecklistService_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_registry_ChecklistService_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ChecklistItemValue); i {
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
		file_registry_ChecklistService_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SearchChecklistItemValues); i {
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
		file_registry_ChecklistService_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SearchChecklistItemValues_Response); i {
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
			RawDescriptor: file_registry_ChecklistService_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_registry_ChecklistService_proto_goTypes,
		DependencyIndexes: file_registry_ChecklistService_proto_depIdxs,
		MessageInfos:      file_registry_ChecklistService_proto_msgTypes,
	}.Build()
	File_registry_ChecklistService_proto = out.File
	file_registry_ChecklistService_proto_rawDesc = nil
	file_registry_ChecklistService_proto_goTypes = nil
	file_registry_ChecklistService_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// ChecklistServiceClient is the client API for ChecklistService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type ChecklistServiceClient interface {
	// Initial functions to list all, create, update
	// checklist_item_values
	SearchChecklistItemValues(ctx context.Context, in *SearchChecklistItemValues, opts ...grpc.CallOption) (*SearchChecklistItemValues_Response, error)
}

type checklistServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewChecklistServiceClient(cc grpc.ClientConnInterface) ChecklistServiceClient {
	return &checklistServiceClient{cc}
}

func (c *checklistServiceClient) SearchChecklistItemValues(ctx context.Context, in *SearchChecklistItemValues, opts ...grpc.CallOption) (*SearchChecklistItemValues_Response, error) {
	out := new(SearchChecklistItemValues_Response)
	err := c.cc.Invoke(ctx, "/ai.verta.registry.ChecklistService/searchChecklistItemValues", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ChecklistServiceServer is the server API for ChecklistService service.
type ChecklistServiceServer interface {
	// Initial functions to list all, create, update
	// checklist_item_values
	SearchChecklistItemValues(context.Context, *SearchChecklistItemValues) (*SearchChecklistItemValues_Response, error)
}

// UnimplementedChecklistServiceServer can be embedded to have forward compatible implementations.
type UnimplementedChecklistServiceServer struct {
}

func (*UnimplementedChecklistServiceServer) SearchChecklistItemValues(context.Context, *SearchChecklistItemValues) (*SearchChecklistItemValues_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SearchChecklistItemValues not implemented")
}

func RegisterChecklistServiceServer(s *grpc.Server, srv ChecklistServiceServer) {
	s.RegisterService(&_ChecklistService_serviceDesc, srv)
}

func _ChecklistService_SearchChecklistItemValues_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SearchChecklistItemValues)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ChecklistServiceServer).SearchChecklistItemValues(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/ai.verta.registry.ChecklistService/SearchChecklistItemValues",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ChecklistServiceServer).SearchChecklistItemValues(ctx, req.(*SearchChecklistItemValues))
	}
	return interceptor(ctx, in, info, handler)
}

var _ChecklistService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "ai.verta.registry.ChecklistService",
	HandlerType: (*ChecklistServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "searchChecklistItemValues",
			Handler:    _ChecklistService_SearchChecklistItemValues_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "registry/ChecklistService.proto",
}
