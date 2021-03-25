SHELL := /bin/bash

.PHONY: install proto proto_old
install:
	echo "install"
	. venv/bin/activate; pip install -r requirements.txt

proto:
	echo "proto"
	. venv/bin/activate; python setup.py

proto_old:
	echo "proto_old"
	. venv/bin/activate; python -m grpc_tools.protoc --python_out=./gen --grpc_python_out=./gen  -I./proto helloworld.proto

