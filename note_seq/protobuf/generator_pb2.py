# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: generator.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'generator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgenerator.proto\x12\x07magenta\"3\n\x10GeneratorDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\xdd\x03\n\x10GeneratorOptions\x12\x41\n\x0einput_sections\x18\x01 \x03(\x0b\x32).magenta.GeneratorOptions.SequenceSection\x12\x44\n\x11generate_sections\x18\x02 \x03(\x0b\x32).magenta.GeneratorOptions.SequenceSection\x12\x31\n\x04\x61rgs\x18\x03 \x03(\x0b\x32#.magenta.GeneratorOptions.ArgsEntry\x1a\x37\n\x0fSequenceSection\x12\x12\n\nstart_time\x18\x01 \x01(\x01\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x01\x1a\x82\x01\n\x08\x41rgValue\x12\x14\n\nbyte_value\x18\x01 \x01(\x0cH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x05 \x01(\tH\x00\x42\x06\n\x04kind\x1aO\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".magenta.GeneratorOptions.ArgValue:\x02\x38\x01\"\xde\x01\n\x0fGeneratorBundle\x12\x34\n\x11generator_details\x18\x01 \x01(\x0b\x32\x19.magenta.GeneratorDetails\x12>\n\x0e\x62undle_details\x18\x04 \x01(\x0b\x32&.magenta.GeneratorBundle.BundleDetails\x12\x17\n\x0f\x63heckpoint_file\x18\x02 \x03(\x0c\x12\x16\n\x0emetagraph_file\x18\x03 \x01(\x0c\x1a$\n\rBundleDetails\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GENERATOROPTIONS_ARGSENTRY']._loaded_options = None
  _globals['_GENERATOROPTIONS_ARGSENTRY']._serialized_options = b'8\001'
  _globals['_GENERATORDETAILS']._serialized_start=28
  _globals['_GENERATORDETAILS']._serialized_end=79
  _globals['_GENERATOROPTIONS']._serialized_start=82
  _globals['_GENERATOROPTIONS']._serialized_end=559
  _globals['_GENERATOROPTIONS_SEQUENCESECTION']._serialized_start=290
  _globals['_GENERATOROPTIONS_SEQUENCESECTION']._serialized_end=345
  _globals['_GENERATOROPTIONS_ARGVALUE']._serialized_start=348
  _globals['_GENERATOROPTIONS_ARGVALUE']._serialized_end=478
  _globals['_GENERATOROPTIONS_ARGSENTRY']._serialized_start=480
  _globals['_GENERATOROPTIONS_ARGSENTRY']._serialized_end=559
  _globals['_GENERATORBUNDLE']._serialized_start=562
  _globals['_GENERATORBUNDLE']._serialized_end=784
  _globals['_GENERATORBUNDLE_BUNDLEDETAILS']._serialized_start=748
  _globals['_GENERATORBUNDLE_BUNDLEDETAILS']._serialized_end=784
# @@protoc_insertion_point(module_scope)