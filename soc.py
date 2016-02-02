import socket

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('www.py4inf.com', 80))
msg = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
misock.send(msg.encode(encoding='utf_8'))

while True:
    datos = misock.recv(512)
    if ( len(datos) < 1 ) :
        break
    print (datos)

misock.close()
