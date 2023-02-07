// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.26.0
// 	protoc        v3.21.6
// source: modeldb/versioning/Code.proto

package versioning

import (
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

type CodeBlob struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Content:
	//	*CodeBlob_Git
	//	*CodeBlob_Notebook
	Content isCodeBlob_Content `protobuf_oneof:"content"`
}

func (x *CodeBlob) Reset() {
	*x = CodeBlob{}
	if protoimpl.UnsafeEnabled {
		mi := &file_modeldb_versioning_Code_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CodeBlob) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CodeBlob) ProtoMessage() {}

func (x *CodeBlob) ProtoReflect() protoreflect.Message {
	mi := &file_modeldb_versioning_Code_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CodeBlob.ProtoReflect.Descriptor instead.
func (*CodeBlob) Descriptor() ([]byte, []int) {
	return file_modeldb_versioning_Code_proto_rawDescGZIP(), []int{0}
}

func (m *CodeBlob) GetContent() isCodeBlob_Content {
	if m != nil {
		return m.Content
	}
	return nil
}

func (x *CodeBlob) GetGit() *GitCodeBlob {
	if x, ok := x.GetContent().(*CodeBlob_Git); ok {
		return x.Git
	}
	return nil
}

func (x *CodeBlob) GetNotebook() *NotebookCodeBlob {
	if x, ok := x.GetContent().(*CodeBlob_Notebook); ok {
		return x.Notebook
	}
	return nil
}

type isCodeBlob_Content interface {
	isCodeBlob_Content()
}

type CodeBlob_Git struct {
	Git *GitCodeBlob `protobuf:"bytes,1,opt,name=git,proto3,oneof"`
}

type CodeBlob_Notebook struct {
	Notebook *NotebookCodeBlob `protobuf:"bytes,2,opt,name=notebook,proto3,oneof"`
}

func (*CodeBlob_Git) isCodeBlob_Content() {}

func (*CodeBlob_Notebook) isCodeBlob_Content() {}

type GitCodeBlob struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Repo    string `protobuf:"bytes,1,opt,name=repo,proto3" json:"repo,omitempty"`
	Hash    string `protobuf:"bytes,2,opt,name=hash,proto3" json:"hash,omitempty"`
	Branch  string `protobuf:"bytes,3,opt,name=branch,proto3" json:"branch,omitempty"`
	Tag     string `protobuf:"bytes,4,opt,name=tag,proto3" json:"tag,omitempty"`
	IsDirty bool   `protobuf:"varint,5,opt,name=is_dirty,json=isDirty,proto3" json:"is_dirty,omitempty"`
}

func (x *GitCodeBlob) Reset() {
	*x = GitCodeBlob{}
	if protoimpl.UnsafeEnabled {
		mi := &file_modeldb_versioning_Code_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GitCodeBlob) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GitCodeBlob) ProtoMessage() {}

func (x *GitCodeBlob) ProtoReflect() protoreflect.Message {
	mi := &file_modeldb_versioning_Code_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GitCodeBlob.ProtoReflect.Descriptor instead.
func (*GitCodeBlob) Descriptor() ([]byte, []int) {
	return file_modeldb_versioning_Code_proto_rawDescGZIP(), []int{1}
}

func (x *GitCodeBlob) GetRepo() string {
	if x != nil {
		return x.Repo
	}
	return ""
}

func (x *GitCodeBlob) GetHash() string {
	if x != nil {
		return x.Hash
	}
	return ""
}

func (x *GitCodeBlob) GetBranch() string {
	if x != nil {
		return x.Branch
	}
	return ""
}

func (x *GitCodeBlob) GetTag() string {
	if x != nil {
		return x.Tag
	}
	return ""
}

func (x *GitCodeBlob) GetIsDirty() bool {
	if x != nil {
		return x.IsDirty
	}
	return false
}

type NotebookCodeBlob struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Path    *PathDatasetComponentBlob `protobuf:"bytes,1,opt,name=path,proto3" json:"path,omitempty"`
	GitRepo *GitCodeBlob              `protobuf:"bytes,2,opt,name=git_repo,json=gitRepo,proto3" json:"git_repo,omitempty"`
}

func (x *NotebookCodeBlob) Reset() {
	*x = NotebookCodeBlob{}
	if protoimpl.UnsafeEnabled {
		mi := &file_modeldb_versioning_Code_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NotebookCodeBlob) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NotebookCodeBlob) ProtoMessage() {}

func (x *NotebookCodeBlob) ProtoReflect() protoreflect.Message {
	mi := &file_modeldb_versioning_Code_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NotebookCodeBlob.ProtoReflect.Descriptor instead.
func (*NotebookCodeBlob) Descriptor() ([]byte, []int) {
	return file_modeldb_versioning_Code_proto_rawDescGZIP(), []int{2}
}

func (x *NotebookCodeBlob) GetPath() *PathDatasetComponentBlob {
	if x != nil {
		return x.Path
	}
	return nil
}

func (x *NotebookCodeBlob) GetGitRepo() *GitCodeBlob {
	if x != nil {
		return x.GitRepo
	}
	return nil
}

type CodeDiff struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Content:
	//	*CodeDiff_Git
	//	*CodeDiff_Notebook
	Content isCodeDiff_Content `protobuf_oneof:"content"`
}

func (x *CodeDiff) Reset() {
	*x = CodeDiff{}
	if protoimpl.UnsafeEnabled {
		mi := &file_modeldb_versioning_Code_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CodeDiff) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CodeDiff) ProtoMessage() {}

func (x *CodeDiff) ProtoReflect() protoreflect.Message {
	mi := &file_modeldb_versioning_Code_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CodeDiff.ProtoReflect.Descriptor instead.
func (*CodeDiff) Descriptor() ([]byte, []int) {
	return file_modeldb_versioning_Code_proto_rawDescGZIP(), []int{3}
}

func (m *CodeDiff) GetContent() isCodeDiff_Content {
	if m != nil {
		return m.Content
	}
	return nil
}

func (x *CodeDiff) GetGit() *GitCodeDiff {
	if x, ok := x.GetContent().(*CodeDiff_Git); ok {
		return x.Git
	}
	return nil
}

func (x *CodeDiff) GetNotebook() *NotebookCodeDiff {
	if x, ok := x.GetContent().(*CodeDiff_Notebook); ok {
		return x.Notebook
	}
	return nil
}

type isCodeDiff_Content interface {
	isCodeDiff_Content()
}

type CodeDiff_Git struct {
	Git *GitCodeDiff `protobuf:"bytes,1,opt,name=git,proto3,oneof"`
}

type CodeDiff_Notebook struct {
	Notebook *NotebookCodeDiff `protobuf:"bytes,2,opt,name=notebook,proto3,oneof"`
}

func (*CodeDiff_Git) isCodeDiff_Content() {}

func (*CodeDiff_Notebook) isCodeDiff_Content() {}

type GitCodeDiff struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Status DiffStatusEnum_DiffStatus `protobuf:"varint,1,opt,name=status,proto3,enum=ai.verta.modeldb.versioning.DiffStatusEnum_DiffStatus" json:"status,omitempty"`
	A      *GitCodeBlob              `protobuf:"bytes,2,opt,name=A,proto3" json:"A,omitempty"`
	B      *GitCodeBlob              `protobuf:"bytes,3,opt,name=B,proto3" json:"B,omitempty"`
	C      *GitCodeBlob              `protobuf:"bytes,4,opt,name=C,proto3" json:"C,omitempty"`
}

func (x *GitCodeDiff) Reset() {
	*x = GitCodeDiff{}
	if protoimpl.UnsafeEnabled {
		mi := &file_modeldb_versioning_Code_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GitCodeDiff) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GitCodeDiff) ProtoMessage() {}

func (x *GitCodeDiff) ProtoReflect() protoreflect.Message {
	mi := &file_modeldb_versioning_Code_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GitCodeDiff.ProtoReflect.Descriptor instead.
func (*GitCodeDiff) Descriptor() ([]byte, []int) {
	return file_modeldb_versioning_Code_proto_rawDescGZIP(), []int{4}
}

func (x *GitCodeDiff) GetStatus() DiffStatusEnum_DiffStatus {
	if x != nil {
		return x.Status
	}
	return DiffStatusEnum_UNKNOWN
}

func (x *GitCodeDiff) GetA() *GitCodeBlob {
	if x != nil {
		return x.A
	}
	return nil
}

func (x *GitCodeDiff) GetB() *GitCodeBlob {
	if x != nil {
		return x.B
	}
	return nil
}

func (x *GitCodeDiff) GetC() *GitCodeBlob {
	if x != nil {
		return x.C
	}
	return nil
}

type NotebookCodeDiff struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Path    *PathDatasetComponentDiff `protobuf:"bytes,1,opt,name=path,proto3" json:"path,omitempty"`
	GitRepo *GitCodeDiff              `protobuf:"bytes,2,opt,name=git_repo,json=gitRepo,proto3" json:"git_repo,omitempty"`
}

func (x *NotebookCodeDiff) Reset() {
	*x = NotebookCodeDiff{}
	if protoimpl.UnsafeEnabled {
		mi := &file_modeldb_versioning_Code_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NotebookCodeDiff) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NotebookCodeDiff) ProtoMessage() {}

func (x *NotebookCodeDiff) ProtoReflect() protoreflect.Message {
	mi := &file_modeldb_versioning_Code_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NotebookCodeDiff.ProtoReflect.Descriptor instead.
func (*NotebookCodeDiff) Descriptor() ([]byte, []int) {
	return file_modeldb_versioning_Code_proto_rawDescGZIP(), []int{5}
}

func (x *NotebookCodeDiff) GetPath() *PathDatasetComponentDiff {
	if x != nil {
		return x.Path
	}
	return nil
}

func (x *NotebookCodeDiff) GetGitRepo() *GitCodeDiff {
	if x != nil {
		return x.GitRepo
	}
	return nil
}

var File_modeldb_versioning_Code_proto protoreflect.FileDescriptor

var file_modeldb_versioning_Code_proto_rawDesc = []byte{
	0x0a, 0x1d, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f,
	0x6e, 0x69, 0x6e, 0x67, 0x2f, 0x43, 0x6f, 0x64, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x1b, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64,
	0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x1a, 0x20, 0x6d, 0x6f,
	0x64, 0x65, 0x6c, 0x64, 0x62, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67,
	0x2f, 0x44, 0x61, 0x74, 0x61, 0x73, 0x65, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1e,
	0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69,
	0x6e, 0x67, 0x2f, 0x45, 0x6e, 0x75, 0x6d, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xa0,
	0x01, 0x0a, 0x08, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c, 0x6f, 0x62, 0x12, 0x3c, 0x0a, 0x03, 0x67,
	0x69, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x28, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65,
	0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73,
	0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47, 0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c,
	0x6f, 0x62, 0x48, 0x00, 0x52, 0x03, 0x67, 0x69, 0x74, 0x12, 0x4b, 0x0a, 0x08, 0x6e, 0x6f, 0x74,
	0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2d, 0x2e, 0x61, 0x69,
	0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2e, 0x76,
	0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x4e, 0x6f, 0x74, 0x65, 0x62, 0x6f,
	0x6f, 0x6b, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c, 0x6f, 0x62, 0x48, 0x00, 0x52, 0x08, 0x6e, 0x6f,
	0x74, 0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x42, 0x09, 0x0a, 0x07, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x6e,
	0x74, 0x22, 0x7a, 0x0a, 0x0b, 0x47, 0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c, 0x6f, 0x62,
	0x12, 0x12, 0x0a, 0x04, 0x72, 0x65, 0x70, 0x6f, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x72, 0x65, 0x70, 0x6f, 0x12, 0x12, 0x0a, 0x04, 0x68, 0x61, 0x73, 0x68, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x04, 0x68, 0x61, 0x73, 0x68, 0x12, 0x16, 0x0a, 0x06, 0x62, 0x72, 0x61, 0x6e,
	0x63, 0x68, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x62, 0x72, 0x61, 0x6e, 0x63, 0x68,
	0x12, 0x10, 0x0a, 0x03, 0x74, 0x61, 0x67, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x74,
	0x61, 0x67, 0x12, 0x19, 0x0a, 0x08, 0x69, 0x73, 0x5f, 0x64, 0x69, 0x72, 0x74, 0x79, 0x18, 0x05,
	0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x69, 0x73, 0x44, 0x69, 0x72, 0x74, 0x79, 0x22, 0xa2, 0x01,
	0x0a, 0x10, 0x4e, 0x6f, 0x74, 0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c,
	0x6f, 0x62, 0x12, 0x49, 0x0a, 0x04, 0x70, 0x61, 0x74, 0x68, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x35, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65,
	0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x50,
	0x61, 0x74, 0x68, 0x44, 0x61, 0x74, 0x61, 0x73, 0x65, 0x74, 0x43, 0x6f, 0x6d, 0x70, 0x6f, 0x6e,
	0x65, 0x6e, 0x74, 0x42, 0x6c, 0x6f, 0x62, 0x52, 0x04, 0x70, 0x61, 0x74, 0x68, 0x12, 0x43, 0x0a,
	0x08, 0x67, 0x69, 0x74, 0x5f, 0x72, 0x65, 0x70, 0x6f, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x28, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c,
	0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47, 0x69,
	0x74, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c, 0x6f, 0x62, 0x52, 0x07, 0x67, 0x69, 0x74, 0x52, 0x65,
	0x70, 0x6f, 0x22, 0xa0, 0x01, 0x0a, 0x08, 0x43, 0x6f, 0x64, 0x65, 0x44, 0x69, 0x66, 0x66, 0x12,
	0x3c, 0x0a, 0x03, 0x67, 0x69, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x28, 0x2e, 0x61,
	0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2e,
	0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47, 0x69, 0x74, 0x43, 0x6f,
	0x64, 0x65, 0x44, 0x69, 0x66, 0x66, 0x48, 0x00, 0x52, 0x03, 0x67, 0x69, 0x74, 0x12, 0x4b, 0x0a,
	0x08, 0x6e, 0x6f, 0x74, 0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x2d, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c,
	0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x4e, 0x6f,
	0x74, 0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x43, 0x6f, 0x64, 0x65, 0x44, 0x69, 0x66, 0x66, 0x48, 0x00,
	0x52, 0x08, 0x6e, 0x6f, 0x74, 0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x42, 0x09, 0x0a, 0x07, 0x63, 0x6f,
	0x6e, 0x74, 0x65, 0x6e, 0x74, 0x22, 0x85, 0x02, 0x0a, 0x0b, 0x47, 0x69, 0x74, 0x43, 0x6f, 0x64,
	0x65, 0x44, 0x69, 0x66, 0x66, 0x12, 0x4e, 0x0a, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x36, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61,
	0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e,
	0x69, 0x6e, 0x67, 0x2e, 0x44, 0x69, 0x66, 0x66, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x45, 0x6e,
	0x75, 0x6d, 0x2e, 0x44, 0x69, 0x66, 0x66, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x73,
	0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x36, 0x0a, 0x01, 0x41, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x28, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65,
	0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47,
	0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c, 0x6f, 0x62, 0x52, 0x01, 0x41, 0x12, 0x36, 0x0a,
	0x01, 0x42, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x28, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65,
	0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73,
	0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47, 0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c,
	0x6f, 0x62, 0x52, 0x01, 0x42, 0x12, 0x36, 0x0a, 0x01, 0x43, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x28, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65,
	0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47,
	0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x42, 0x6c, 0x6f, 0x62, 0x52, 0x01, 0x43, 0x22, 0xa2, 0x01,
	0x0a, 0x10, 0x4e, 0x6f, 0x74, 0x65, 0x62, 0x6f, 0x6f, 0x6b, 0x43, 0x6f, 0x64, 0x65, 0x44, 0x69,
	0x66, 0x66, 0x12, 0x49, 0x0a, 0x04, 0x70, 0x61, 0x74, 0x68, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x35, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65,
	0x6c, 0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x50,
	0x61, 0x74, 0x68, 0x44, 0x61, 0x74, 0x61, 0x73, 0x65, 0x74, 0x43, 0x6f, 0x6d, 0x70, 0x6f, 0x6e,
	0x65, 0x6e, 0x74, 0x44, 0x69, 0x66, 0x66, 0x52, 0x04, 0x70, 0x61, 0x74, 0x68, 0x12, 0x43, 0x0a,
	0x08, 0x67, 0x69, 0x74, 0x5f, 0x72, 0x65, 0x70, 0x6f, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x28, 0x2e, 0x61, 0x69, 0x2e, 0x76, 0x65, 0x72, 0x74, 0x61, 0x2e, 0x6d, 0x6f, 0x64, 0x65, 0x6c,
	0x64, 0x62, 0x2e, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x47, 0x69,
	0x74, 0x43, 0x6f, 0x64, 0x65, 0x44, 0x69, 0x66, 0x66, 0x52, 0x07, 0x67, 0x69, 0x74, 0x52, 0x65,
	0x70, 0x6f, 0x42, 0x4d, 0x50, 0x01, 0x5a, 0x49, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x56, 0x65, 0x72, 0x74, 0x61, 0x41, 0x49, 0x2f, 0x6d, 0x6f, 0x64, 0x65, 0x6c,
	0x64, 0x62, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x2f, 0x6d,
	0x6f, 0x64, 0x65, 0x6c, 0x64, 0x62, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x69, 0x6e,
	0x67, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_modeldb_versioning_Code_proto_rawDescOnce sync.Once
	file_modeldb_versioning_Code_proto_rawDescData = file_modeldb_versioning_Code_proto_rawDesc
)

func file_modeldb_versioning_Code_proto_rawDescGZIP() []byte {
	file_modeldb_versioning_Code_proto_rawDescOnce.Do(func() {
		file_modeldb_versioning_Code_proto_rawDescData = protoimpl.X.CompressGZIP(file_modeldb_versioning_Code_proto_rawDescData)
	})
	return file_modeldb_versioning_Code_proto_rawDescData
}

var file_modeldb_versioning_Code_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_modeldb_versioning_Code_proto_goTypes = []interface{}{
	(*CodeBlob)(nil),                 // 0: ai.verta.modeldb.versioning.CodeBlob
	(*GitCodeBlob)(nil),              // 1: ai.verta.modeldb.versioning.GitCodeBlob
	(*NotebookCodeBlob)(nil),         // 2: ai.verta.modeldb.versioning.NotebookCodeBlob
	(*CodeDiff)(nil),                 // 3: ai.verta.modeldb.versioning.CodeDiff
	(*GitCodeDiff)(nil),              // 4: ai.verta.modeldb.versioning.GitCodeDiff
	(*NotebookCodeDiff)(nil),         // 5: ai.verta.modeldb.versioning.NotebookCodeDiff
	(*PathDatasetComponentBlob)(nil), // 6: ai.verta.modeldb.versioning.PathDatasetComponentBlob
	(DiffStatusEnum_DiffStatus)(0),   // 7: ai.verta.modeldb.versioning.DiffStatusEnum.DiffStatus
	(*PathDatasetComponentDiff)(nil), // 8: ai.verta.modeldb.versioning.PathDatasetComponentDiff
}
var file_modeldb_versioning_Code_proto_depIdxs = []int32{
	1,  // 0: ai.verta.modeldb.versioning.CodeBlob.git:type_name -> ai.verta.modeldb.versioning.GitCodeBlob
	2,  // 1: ai.verta.modeldb.versioning.CodeBlob.notebook:type_name -> ai.verta.modeldb.versioning.NotebookCodeBlob
	6,  // 2: ai.verta.modeldb.versioning.NotebookCodeBlob.path:type_name -> ai.verta.modeldb.versioning.PathDatasetComponentBlob
	1,  // 3: ai.verta.modeldb.versioning.NotebookCodeBlob.git_repo:type_name -> ai.verta.modeldb.versioning.GitCodeBlob
	4,  // 4: ai.verta.modeldb.versioning.CodeDiff.git:type_name -> ai.verta.modeldb.versioning.GitCodeDiff
	5,  // 5: ai.verta.modeldb.versioning.CodeDiff.notebook:type_name -> ai.verta.modeldb.versioning.NotebookCodeDiff
	7,  // 6: ai.verta.modeldb.versioning.GitCodeDiff.status:type_name -> ai.verta.modeldb.versioning.DiffStatusEnum.DiffStatus
	1,  // 7: ai.verta.modeldb.versioning.GitCodeDiff.A:type_name -> ai.verta.modeldb.versioning.GitCodeBlob
	1,  // 8: ai.verta.modeldb.versioning.GitCodeDiff.B:type_name -> ai.verta.modeldb.versioning.GitCodeBlob
	1,  // 9: ai.verta.modeldb.versioning.GitCodeDiff.C:type_name -> ai.verta.modeldb.versioning.GitCodeBlob
	8,  // 10: ai.verta.modeldb.versioning.NotebookCodeDiff.path:type_name -> ai.verta.modeldb.versioning.PathDatasetComponentDiff
	4,  // 11: ai.verta.modeldb.versioning.NotebookCodeDiff.git_repo:type_name -> ai.verta.modeldb.versioning.GitCodeDiff
	12, // [12:12] is the sub-list for method output_type
	12, // [12:12] is the sub-list for method input_type
	12, // [12:12] is the sub-list for extension type_name
	12, // [12:12] is the sub-list for extension extendee
	0,  // [0:12] is the sub-list for field type_name
}

func init() { file_modeldb_versioning_Code_proto_init() }
func file_modeldb_versioning_Code_proto_init() {
	if File_modeldb_versioning_Code_proto != nil {
		return
	}
	file_modeldb_versioning_Dataset_proto_init()
	file_modeldb_versioning_Enums_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_modeldb_versioning_Code_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CodeBlob); i {
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
		file_modeldb_versioning_Code_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GitCodeBlob); i {
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
		file_modeldb_versioning_Code_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NotebookCodeBlob); i {
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
		file_modeldb_versioning_Code_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CodeDiff); i {
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
		file_modeldb_versioning_Code_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GitCodeDiff); i {
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
		file_modeldb_versioning_Code_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NotebookCodeDiff); i {
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
	file_modeldb_versioning_Code_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*CodeBlob_Git)(nil),
		(*CodeBlob_Notebook)(nil),
	}
	file_modeldb_versioning_Code_proto_msgTypes[3].OneofWrappers = []interface{}{
		(*CodeDiff_Git)(nil),
		(*CodeDiff_Notebook)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_modeldb_versioning_Code_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_modeldb_versioning_Code_proto_goTypes,
		DependencyIndexes: file_modeldb_versioning_Code_proto_depIdxs,
		MessageInfos:      file_modeldb_versioning_Code_proto_msgTypes,
	}.Build()
	File_modeldb_versioning_Code_proto = out.File
	file_modeldb_versioning_Code_proto_rawDesc = nil
	file_modeldb_versioning_Code_proto_goTypes = nil
	file_modeldb_versioning_Code_proto_depIdxs = nil
}
