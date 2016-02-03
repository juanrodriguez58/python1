import socket
import urllib.request

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)

# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.voidspace.org.uk')
try:
    response = urllib.request.urlopen(req)
    print(response)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read()) 

