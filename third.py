def imprime():
	print("Inicio...")

def tratarLinea(linea):
	pos=0
	try: 
			pos = linea.index("a", 0, len(linea))
			r = len(linea) - pos
			resto = linea.rjust(r)
			print("Posición", pos, " Resto ", resto, "\n")
	except:
		print("No se encuentra el caracter en la linea \n", linea)



nombre = input("Introduce el nombre del fichero \n")
try :
	imprime()
	fh = open(nombre, "r")
	count = 0
	num = 0
	for line in fh:
		tratarLinea(line)
		count = count + 1
	print (count,"Lineas")
	fh.close
except: 
	print("No se puede abrir el archivo: ", nombre)