from concurrent import futures
import time
import grpc
import api.gen.helloworld_pb2 as helloworld_pb2
import api.gen.helloworld_pb2_grpc as helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # 工作函数
    def SayHello(self, request, context):
        print(request.name)
        message = "This message is from server."
        return helloworld_pb2.HelloReply(message=message)


def server():
    # Grpc服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    print("server is opening,waiting for message...")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    server()
