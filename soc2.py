import socket

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('www.voidspace.org.uk', 80))
msg = 'GET http://www.voidspace.org.uk HTTP/1.0\n\n'
misock.send(msg.encode(encoding='utf_8'))
cod = " "

while True:
    datos = misock.recv(512)
    if ( len(datos) < 1 ) :
        break
    cod =  cod + datos.decode(encoding='utf_8')

misock.close()
for linea in cod:
    print(linea)
