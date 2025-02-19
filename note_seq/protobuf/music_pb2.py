# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: music.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmusic.proto\x12\x07magenta\"\xd3\x1e\n\x0cNoteSequence\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x18\n\x10reference_number\x18\x12 \x01(\x03\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12\x19\n\x11ticks_per_quarter\x18\x04 \x01(\x05\x12<\n\x0ftime_signatures\x18\x05 \x03(\x0b\x32#.magenta.NoteSequence.TimeSignature\x12:\n\x0ekey_signatures\x18\x06 \x03(\x0b\x32\".magenta.NoteSequence.KeySignature\x12+\n\x06tempos\x18\x07 \x03(\x0b\x32\x1b.magenta.NoteSequence.Tempo\x12)\n\x05notes\x18\x08 \x03(\x0b\x32\x1a.magenta.NoteSequence.Note\x12\x12\n\ntotal_time\x18\t \x01(\x01\x12\x1d\n\x15total_quantized_steps\x18\x10 \x01(\x03\x12\x34\n\x0bpitch_bends\x18\n \x03(\x0b\x32\x1f.magenta.NoteSequence.PitchBend\x12<\n\x0f\x63ontrol_changes\x18\x0b \x03(\x0b\x32#.magenta.NoteSequence.ControlChange\x12\x32\n\npart_infos\x18\x0c \x03(\x0b\x32\x1e.magenta.NoteSequence.PartInfo\x12\x35\n\x0bsource_info\x18\r \x01(\x0b\x32 .magenta.NoteSequence.SourceInfo\x12>\n\x10text_annotations\x18\x0e \x03(\x0b\x32$.magenta.NoteSequence.TextAnnotation\x12\x44\n\x13section_annotations\x18\x14 \x03(\x0b\x32\'.magenta.NoteSequence.SectionAnnotation\x12:\n\x0esection_groups\x18\x15 \x03(\x0b\x32\".magenta.NoteSequence.SectionGroup\x12\x41\n\x11quantization_info\x18\x0f \x01(\x0b\x32&.magenta.NoteSequence.QuantizationInfo\x12?\n\x10subsequence_info\x18\x11 \x01(\x0b\x32%.magenta.NoteSequence.SubsequenceInfo\x12\x34\n\x11sequence_metadata\x18\x13 \x01(\x0b\x32\x19.magenta.SequenceMetadata\x12>\n\x10instrument_infos\x18\x17 \x03(\x0b\x32$.magenta.NoteSequence.InstrumentInfo\x1a\xb7\x02\n\x04Note\x12\r\n\x05pitch\x18\x01 \x01(\x05\x12\x33\n\npitch_name\x18\x0b \x01(\x0e\x32\x1f.magenta.NoteSequence.PitchName\x12\x10\n\x08velocity\x18\x02 \x01(\x05\x12\x12\n\nstart_time\x18\x03 \x01(\x01\x12\x1c\n\x14quantized_start_step\x18\r \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x01\x12\x1a\n\x12quantized_end_step\x18\x0e \x01(\x03\x12\x11\n\tnumerator\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65nominator\x18\x06 \x01(\x05\x12\x12\n\ninstrument\x18\x07 \x01(\x05\x12\x0f\n\x07program\x18\x08 \x01(\x05\x12\x0f\n\x07is_drum\x18\t \x01(\x08\x12\x0c\n\x04part\x18\n \x01(\x05\x12\r\n\x05voice\x18\x0c \x01(\x05\x1a\x45\n\rTimeSignature\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x11\n\tnumerator\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65nominator\x18\x03 \x01(\x05\x1a\xb6\x03\n\x0cKeySignature\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x33\n\x03key\x18\x02 \x01(\x0e\x32&.magenta.NoteSequence.KeySignature.Key\x12\x35\n\x04mode\x18\x03 \x01(\x0e\x32\'.magenta.NoteSequence.KeySignature.Mode\"\xb7\x01\n\x03Key\x12\x05\n\x01\x43\x10\x00\x12\x0b\n\x07\x43_SHARP\x10\x01\x12\n\n\x06\x44_FLAT\x10\x01\x12\x05\n\x01\x44\x10\x02\x12\x0b\n\x07\x44_SHARP\x10\x03\x12\n\n\x06\x45_FLAT\x10\x03\x12\x05\n\x01\x45\x10\x04\x12\x05\n\x01\x46\x10\x05\x12\x0b\n\x07\x46_SHARP\x10\x06\x12\n\n\x06G_FLAT\x10\x06\x12\x05\n\x01G\x10\x07\x12\x0b\n\x07G_SHARP\x10\x08\x12\n\n\x06\x41_FLAT\x10\x08\x12\x05\n\x01\x41\x10\t\x12\x0b\n\x07\x41_SHARP\x10\n\x12\n\n\x06\x42_FLAT\x10\n\x12\x05\n\x01\x42\x10\x0b\x1a\x02\x10\x01\"r\n\x04Mode\x12\t\n\x05MAJOR\x10\x00\x12\t\n\x05MINOR\x10\x01\x12\x11\n\rNOT_SPECIFIED\x10\x02\x12\x0e\n\nMIXOLYDIAN\x10\x03\x12\n\n\x06\x44ORIAN\x10\x04\x12\x0c\n\x08PHRYGIAN\x10\x05\x12\n\n\x06LYDIAN\x10\x06\x12\x0b\n\x07LOCRIAN\x10\x07\x1a\"\n\x05Tempo\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x0b\n\x03qpm\x18\x02 \x01(\x01\x1a]\n\tPitchBend\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x0c\n\x04\x62\x65nd\x18\x02 \x01(\x05\x12\x12\n\ninstrument\x18\x03 \x01(\x05\x12\x0f\n\x07program\x18\x04 \x01(\x05\x12\x0f\n\x07is_drum\x18\x05 \x01(\x08\x1a\x9a\x01\n\rControlChange\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x16\n\x0equantized_step\x18\x07 \x01(\x03\x12\x16\n\x0e\x63ontrol_number\x18\x02 \x01(\x05\x12\x15\n\rcontrol_value\x18\x03 \x01(\x05\x12\x12\n\ninstrument\x18\x04 \x01(\x05\x12\x0f\n\x07program\x18\x05 \x01(\x05\x12\x0f\n\x07is_drum\x18\x06 \x01(\x08\x1a&\n\x08PartInfo\x12\x0c\n\x04part\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x32\n\x0eInstrumentInfo\x12\x12\n\ninstrument\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x8b\x04\n\nSourceInfo\x12@\n\x0bsource_type\x18\x01 \x01(\x0e\x32+.magenta.NoteSequence.SourceInfo.SourceType\x12\x44\n\rencoding_type\x18\x02 \x01(\x0e\x32-.magenta.NoteSequence.SourceInfo.EncodingType\x12\x37\n\x06parser\x18\x03 \x01(\x0e\x32\'.magenta.NoteSequence.SourceInfo.Parser\"M\n\nSourceType\x12\x17\n\x13UNKNOWN_SOURCE_TYPE\x10\x00\x12\x0f\n\x0bSCORE_BASED\x10\x01\x12\x15\n\x11PERFORMANCE_BASED\x10\x02\"Y\n\x0c\x45ncodingType\x12\x19\n\x15UNKNOWN_ENCODING_TYPE\x10\x00\x12\r\n\tMUSIC_XML\x10\x01\x12\x07\n\x03\x41\x42\x43\x10\x02\x12\x08\n\x04MIDI\x10\x03\x12\x0c\n\x08MUSICNET\x10\x04\"\x91\x01\n\x06Parser\x12\x12\n\x0eUNKNOWN_PARSER\x10\x00\x12\x0b\n\x07MUSIC21\x10\x01\x12\x0f\n\x0bPRETTY_MIDI\x10\x02\x12\x15\n\x11MAGENTA_MUSIC_XML\x10\x03\x12\x14\n\x10MAGENTA_MUSICNET\x10\x04\x12\x0f\n\x0bMAGENTA_ABC\x10\x05\x12\x17\n\x13TONEJS_MIDI_CONVERT\x10\x06\x1a\xd5\x01\n\x0eTextAnnotation\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x16\n\x0equantized_step\x18\x04 \x01(\x03\x12\x0c\n\x04text\x18\x02 \x01(\t\x12P\n\x0f\x61nnotation_type\x18\x03 \x01(\x0e\x32\x37.magenta.NoteSequence.TextAnnotation.TextAnnotationType\"=\n\x12TextAnnotationType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x43HORD_SYMBOL\x10\x01\x12\x08\n\x04\x42\x45\x41T\x10\x02\x1aY\n\x10QuantizationInfo\x12\x1b\n\x11steps_per_quarter\x18\x01 \x01(\x05H\x00\x12\x1a\n\x10steps_per_second\x18\x02 \x01(\x05H\x00\x42\x0c\n\nresolution\x1a\x45\n\x0fSubsequenceInfo\x12\x19\n\x11start_time_offset\x18\x01 \x01(\x01\x12\x17\n\x0f\x65nd_time_offset\x18\x02 \x01(\x01\x1a\x35\n\x11SectionAnnotation\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x12\n\nsection_id\x18\x04 \x01(\x03\x1al\n\x07Section\x12\x14\n\nsection_id\x18\x01 \x01(\x03H\x00\x12;\n\rsection_group\x18\x02 \x01(\x0b\x32\".magenta.NoteSequence.SectionGroupH\x00\x42\x0e\n\x0csection_type\x1aR\n\x0cSectionGroup\x12/\n\x08sections\x18\x01 \x03(\x0b\x32\x1d.magenta.NoteSequence.Section\x12\x11\n\tnum_times\x18\x02 \x01(\x05\"\xff\x03\n\tPitchName\x12\x16\n\x12UNKNOWN_PITCH_NAME\x10\x00\x12\x0f\n\x0b\x46_FLAT_FLAT\x10\x01\x12\x0f\n\x0b\x43_FLAT_FLAT\x10\x02\x12\x0f\n\x0bG_FLAT_FLAT\x10\x03\x12\x0f\n\x0b\x44_FLAT_FLAT\x10\x04\x12\x0f\n\x0b\x41_FLAT_FLAT\x10\x05\x12\x0f\n\x0b\x45_FLAT_FLAT\x10\x06\x12\x0f\n\x0b\x42_FLAT_FLAT\x10\x07\x12\n\n\x06\x46_FLAT\x10\x08\x12\n\n\x06\x43_FLAT\x10\t\x12\n\n\x06G_FLAT\x10\n\x12\n\n\x06\x44_FLAT\x10\x0b\x12\n\n\x06\x41_FLAT\x10\x0c\x12\n\n\x06\x45_FLAT\x10\r\x12\n\n\x06\x42_FLAT\x10\x0e\x12\x05\n\x01\x46\x10\x0f\x12\x05\n\x01\x43\x10\x10\x12\x05\n\x01G\x10\x11\x12\x05\n\x01\x44\x10\x12\x12\x05\n\x01\x41\x10\x13\x12\x05\n\x01\x45\x10\x14\x12\x05\n\x01\x42\x10\x15\x12\x0b\n\x07\x46_SHARP\x10\x16\x12\x0b\n\x07\x43_SHARP\x10\x17\x12\x0b\n\x07G_SHARP\x10\x18\x12\x0b\n\x07\x44_SHARP\x10\x19\x12\x0b\n\x07\x41_SHARP\x10\x1a\x12\x0b\n\x07\x45_SHARP\x10\x1b\x12\x0b\n\x07\x42_SHARP\x10\x1c\x12\x11\n\rF_SHARP_SHARP\x10\x1d\x12\x11\n\rC_SHARP_SHARP\x10\x1e\x12\x11\n\rG_SHARP_SHARP\x10\x1f\x12\x11\n\rD_SHARP_SHARP\x10 \x12\x11\n\rA_SHARP_SHARP\x10!\x12\x11\n\rE_SHARP_SHARP\x10\"\x12\x11\n\rB_SHARP_SHARP\x10#\"S\n\x10SequenceMetadata\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x02 \x01(\t\x12\r\n\x05genre\x18\x03 \x03(\t\x12\x11\n\tcomposers\x18\x04 \x03(\t\")\n\rVelocityRange\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'music_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NOTESEQUENCE_KEYSIGNATURE_KEY']._options = None
  _globals['_NOTESEQUENCE_KEYSIGNATURE_KEY']._serialized_options = b'\020\001'
  _globals['_NOTESEQUENCE']._serialized_start=25
  _globals['_NOTESEQUENCE']._serialized_end=3948
  _globals['_NOTESEQUENCE_NOTE']._serialized_start=1078
  _globals['_NOTESEQUENCE_NOTE']._serialized_end=1389
  _globals['_NOTESEQUENCE_TIMESIGNATURE']._serialized_start=1391
  _globals['_NOTESEQUENCE_TIMESIGNATURE']._serialized_end=1460
  _globals['_NOTESEQUENCE_KEYSIGNATURE']._serialized_start=1463
  _globals['_NOTESEQUENCE_KEYSIGNATURE']._serialized_end=1901
  _globals['_NOTESEQUENCE_KEYSIGNATURE_KEY']._serialized_start=1602
  _globals['_NOTESEQUENCE_KEYSIGNATURE_KEY']._serialized_end=1785
  _globals['_NOTESEQUENCE_KEYSIGNATURE_MODE']._serialized_start=1787
  _globals['_NOTESEQUENCE_KEYSIGNATURE_MODE']._serialized_end=1901
  _globals['_NOTESEQUENCE_TEMPO']._serialized_start=1903
  _globals['_NOTESEQUENCE_TEMPO']._serialized_end=1937
  _globals['_NOTESEQUENCE_PITCHBEND']._serialized_start=1939
  _globals['_NOTESEQUENCE_PITCHBEND']._serialized_end=2032
  _globals['_NOTESEQUENCE_CONTROLCHANGE']._serialized_start=2035
  _globals['_NOTESEQUENCE_CONTROLCHANGE']._serialized_end=2189
  _globals['_NOTESEQUENCE_PARTINFO']._serialized_start=2191
  _globals['_NOTESEQUENCE_PARTINFO']._serialized_end=2229
  _globals['_NOTESEQUENCE_INSTRUMENTINFO']._serialized_start=2231
  _globals['_NOTESEQUENCE_INSTRUMENTINFO']._serialized_end=2281
  _globals['_NOTESEQUENCE_SOURCEINFO']._serialized_start=2284
  _globals['_NOTESEQUENCE_SOURCEINFO']._serialized_end=2807
  _globals['_NOTESEQUENCE_SOURCEINFO_SOURCETYPE']._serialized_start=2491
  _globals['_NOTESEQUENCE_SOURCEINFO_SOURCETYPE']._serialized_end=2568
  _globals['_NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE']._serialized_start=2570
  _globals['_NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE']._serialized_end=2659
  _globals['_NOTESEQUENCE_SOURCEINFO_PARSER']._serialized_start=2662
  _globals['_NOTESEQUENCE_SOURCEINFO_PARSER']._serialized_end=2807
  _globals['_NOTESEQUENCE_TEXTANNOTATION']._serialized_start=2810
  _globals['_NOTESEQUENCE_TEXTANNOTATION']._serialized_end=3023
  _globals['_NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE']._serialized_start=2962
  _globals['_NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE']._serialized_end=3023
  _globals['_NOTESEQUENCE_QUANTIZATIONINFO']._serialized_start=3025
  _globals['_NOTESEQUENCE_QUANTIZATIONINFO']._serialized_end=3114
  _globals['_NOTESEQUENCE_SUBSEQUENCEINFO']._serialized_start=3116
  _globals['_NOTESEQUENCE_SUBSEQUENCEINFO']._serialized_end=3185
  _globals['_NOTESEQUENCE_SECTIONANNOTATION']._serialized_start=3187
  _globals['_NOTESEQUENCE_SECTIONANNOTATION']._serialized_end=3240
  _globals['_NOTESEQUENCE_SECTION']._serialized_start=3242
  _globals['_NOTESEQUENCE_SECTION']._serialized_end=3350
  _globals['_NOTESEQUENCE_SECTIONGROUP']._serialized_start=3352
  _globals['_NOTESEQUENCE_SECTIONGROUP']._serialized_end=3434
  _globals['_NOTESEQUENCE_PITCHNAME']._serialized_start=3437
  _globals['_NOTESEQUENCE_PITCHNAME']._serialized_end=3948
  _globals['_SEQUENCEMETADATA']._serialized_start=3950
  _globals['_SEQUENCEMETADATA']._serialized_end=4033
  _globals['_VELOCITYRANGE']._serialized_start=4035
  _globals['_VELOCITYRANGE']._serialized_end=4076
# @@protoc_insertion_point(module_scope)