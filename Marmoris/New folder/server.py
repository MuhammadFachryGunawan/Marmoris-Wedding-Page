# Server-side code

import xmlrpc.server

# Define an XML-RPC server
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))

# Define a shared resource and its current version
resource = {'data': 'initial value'}
resource_version = 1

# Define an XML-RPC method for accessing the resource
def get_resource(version):
  if version == resource_version:
    return resource['data']
  else:
    raise Exception('Resource has been modified')

# Define an XML-RPC method for modifying the resource
def set_resource(version, new_value):
  if version == resource_version:
    resource['data'] = new_value
    resource_version += 1
    return resource_version
  else:
    raise Exception('Resource has been modified')

# Register the XML-RPC methods with the server
server.register_function(get_resource, 'get_resource')
server.register_function(set_resource, 'set_resource')

# Start the XML-RPC server
server.serve_forever()