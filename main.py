import grpc
import server.pb.RecognitionServer_pb2_grpc
import server.RecogninitonServer
from concurrent import futures
import logging


def serve():
    s = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.RecogninitonServer.RecognitionServer_pb2_grpc.add_RecognitionServerServicer_to_server(
        server.RecogninitonServer.RecognitionServicer(), s)
    s.add_insecure_port('[::]:50052')
    s.start()
    print("Recognition Begin to Serve")
    s.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
