import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import grpc

import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")

stub = calculator_pb2_grpc.CalculatorStub(channel)

number = calculator_pb2.Number(value=5)

response = stub.Sum(number)

print(response.value)
