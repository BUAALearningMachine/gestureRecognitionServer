from server.pb import RecognitionServer_pb2_grpc
from server.pb import RecognitionServer_pb2


class RecognitionServicer(RecognitionServer_pb2_grpc.RecognitionServerServicer):
    def GestureRecognition(self, request_iterator, context):
        reqSeq = []
        for eachReq in request_iterator:
            print(eachReq.ids)
            for eachRep in reqSeq:
                yield eachRep
            reqSeq.append(eachReq)
