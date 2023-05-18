# Client-side code

import xmlrpc.client

# Connect to the XML-RPC server
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Get the current version of the resource
version = server.get_resource(0)

# Modify the resource
server.set_resource(version, 'new value')

# Get the updated version of the resource
version = server.get_resource(0)

# Retrieve the updated resource
resource = server.get_resource(version)
print(resource)