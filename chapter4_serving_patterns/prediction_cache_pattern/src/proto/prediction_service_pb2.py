# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.proto import predict_pb2 as predict__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="prediction_service.proto",
    package="onnxruntime.server",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x18prediction_service.proto\x12\x12onnxruntime.server\x1a\rpredict.proto2g\n\x11PredictionService\x12R\n\x07Predict\x12".onnxruntime.server.PredictRequest\x1a#.onnxruntime.server.PredictResponseb\x06proto3',
    dependencies=[
        predict__pb2.DESCRIPTOR,
    ],
)


_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
    name="PredictionService",
    full_name="onnxruntime.server.PredictionService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=63,
    serialized_end=166,
    methods=[
        _descriptor.MethodDescriptor(
            name="Predict",
            full_name="onnxruntime.server.PredictionService.Predict",
            index=0,
            containing_service=None,
            input_type=predict__pb2._PREDICTREQUEST,
            output_type=predict__pb2._PREDICTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name["PredictionService"] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)
