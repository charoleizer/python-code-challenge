import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc

from core import calculator


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Sum(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.sum_custom(request.value)
        return response

    def Substract(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.substract_custom(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print("Starting server. Listening on port 50051.")
server.add_insecure_port("[::]:50051")
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
