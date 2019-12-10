from server.pb import RecognitionServer_pb2_grpc
from server.pb import RecognitionServer_pb2
from server.pb.RecognitionServer_pb2 import GestureRecognitionRequest
from server.pb.RecognitionServer_pb2 import GestureRecognitionReply


class RecognitionServicer(RecognitionServer_pb2_grpc.RecognitionServerServicer):
    def GestureRecognition(self, request_iterator, context):
        preReqs = []
        for eachReq in request_iterator:
            preReqs.append(eachReq)
            for preReq in preReqs:
                if int(preReq.ids) * 10 == int(eachReq.ids):
                    rep = GestureRecognitionReply()
                    rep.ids = eachReq.ids
                    rep.result = int(eachReq.ids) * 10
                    print(rep.ids)
                    yield rep
