# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x05users\"=\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\"\x11\n\x0fGetUsersRequest\"-\n\x10GetUsersResponse\x12\x19\n\x04user\x18\x01 \x03(\x0b\x32\x0b.users.User\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"0\n\x13GetUserByIdResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\".\n\x11\x43reateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12\x43reateUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\".\n\x11UpdateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12UpdateUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"/\n\x12\x44\x65leteUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User2\xdd\x02\n\x05Users\x12=\n\x08GetUsers\x12\x16.users.GetUsersRequest\x1a\x17.users.GetUsersResponse\"\x00\x12\x46\n\x0bGetuserById\x12\x19.users.GetUserByIdRequest\x1a\x1a.users.GetUserByIdResponse\"\x00\x12\x43\n\nCreateUser\x12\x18.users.CreateUserRequest\x1a\x19.users.CreateUserResponse\"\x00\x12\x43\n\nUpdateUser\x12\x18.users.UpdateUserRequest\x1a\x19.users.UpdateUserResponse\"\x00\x12\x43\n\nDeleteUser\x12\x18.users.DeleteUserRequest\x1a\x19.users.DeleteUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=22
  _globals['_USER']._serialized_end=83
  _globals['_GETUSERSREQUEST']._serialized_start=85
  _globals['_GETUSERSREQUEST']._serialized_end=102
  _globals['_GETUSERSRESPONSE']._serialized_start=104
  _globals['_GETUSERSRESPONSE']._serialized_end=149
  _globals['_GETUSERBYIDREQUEST']._serialized_start=151
  _globals['_GETUSERBYIDREQUEST']._serialized_end=183
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=185
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=233
  _globals['_CREATEUSERREQUEST']._serialized_start=235
  _globals['_CREATEUSERREQUEST']._serialized_end=281
  _globals['_CREATEUSERRESPONSE']._serialized_start=283
  _globals['_CREATEUSERRESPONSE']._serialized_end=330
  _globals['_UPDATEUSERREQUEST']._serialized_start=332
  _globals['_UPDATEUSERREQUEST']._serialized_end=378
  _globals['_UPDATEUSERRESPONSE']._serialized_start=380
  _globals['_UPDATEUSERRESPONSE']._serialized_end=427
  _globals['_DELETEUSERREQUEST']._serialized_start=429
  _globals['_DELETEUSERREQUEST']._serialized_end=460
  _globals['_DELETEUSERRESPONSE']._serialized_start=462
  _globals['_DELETEUSERRESPONSE']._serialized_end=509
  _globals['_USERS']._serialized_start=512
  _globals['_USERS']._serialized_end=861
# @@protoc_insertion_point(module_scope)