import glob
import re

from grpc_tools import protoc

# Generate stubs from `api/*.proto` files in `api/gen` directory
protoc.main([
                'grpc_tools.protoc',
                '--proto_path=api',
                '--mypy_out=api/gen',
                '--python_out=api/gen',
                '--grpc_python_out=api/gen'
            ] + [proto for proto in glob.iglob('./api/*.proto')])

# Make pb2 imports in generated scripts relative
for script in glob.iglob('api/gen/*.py'):
    with open(script, 'r+') as file:
        code = file.read()
        file.seek(0)
        file.write(re.sub(r'\n(import .+_pb2.*)', 'from . \\1', code))
        file.truncate()
