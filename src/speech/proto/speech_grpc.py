# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: src/speech/proto/speech.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
from . import speech_pb2


class SpeechServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Say(self, stream: 'grpclib.server.Stream[src.speech.proto.speech_pb2.SayRequest, src.speech.proto.speech_pb2.SayResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Completion(self, stream: 'grpclib.server.Stream[src.speech.proto.speech_pb2.CompletionRequest, src.speech.proto.speech_pb2.CompletionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCommands(self, stream: 'grpclib.server.Stream[src.speech.proto.speech_pb2.GetCommandsRequest, src.speech.proto.speech_pb2.GetCommandsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/viamlabs.service.speech.v1.SpeechService/Say': grpclib.const.Handler(
                self.Say,
                grpclib.const.Cardinality.UNARY_UNARY,
                src.speech.proto.speech_pb2.SayRequest,
                src.speech.proto.speech_pb2.SayResponse,
            ),
            '/viamlabs.service.speech.v1.SpeechService/Completion': grpclib.const.Handler(
                self.Completion,
                grpclib.const.Cardinality.UNARY_UNARY,
                src.speech.proto.speech_pb2.CompletionRequest,
                src.speech.proto.speech_pb2.CompletionResponse,
            ),
            '/viamlabs.service.speech.v1.SpeechService/GetCommands': grpclib.const.Handler(
                self.GetCommands,
                grpclib.const.Cardinality.UNARY_UNARY,
                src.speech.proto.speech_pb2.GetCommandsRequest,
                src.speech.proto.speech_pb2.GetCommandsResponse,
            ),
        }


class SpeechServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Say = grpclib.client.UnaryUnaryMethod(
            channel,
            '/viamlabs.service.speech.v1.SpeechService/Say',
            src.speech.proto.speech_pb2.SayRequest,
            src.speech.proto.speech_pb2.SayResponse,
        )
        self.Completion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/viamlabs.service.speech.v1.SpeechService/Completion',
            src.speech.proto.speech_pb2.CompletionRequest,
            src.speech.proto.speech_pb2.CompletionResponse,
        )
        self.GetCommands = grpclib.client.UnaryUnaryMethod(
            channel,
            '/viamlabs.service.speech.v1.SpeechService/GetCommands',
            src.speech.proto.speech_pb2.GetCommandsRequest,
            src.speech.proto.speech_pb2.GetCommandsResponse,
        )
