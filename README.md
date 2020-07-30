Before start please install dependecies:

`$ pip install -r requirements.txt`

Generate the proto buffer files:

`$ python -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/calculator.proto`

Start the server:

`$ python server/server.py`

Then test the client:

`$ python client/client.py`