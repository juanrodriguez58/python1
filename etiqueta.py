def tratarLinea(linea):
	pos=0
	try: 
			ini = linea.index("<", 0, len(linea))
			fin = linea.index(">", ini, len(linea))
			resto = linea[ini:fin+1]
			return(resto)
	except:
		print("No se encuentra el caracter en la linea \n", linea)



nombre = input("Introduce el nombre del fichero \n")
lista = []
try :
	fh = open(nombre, "r")
	count = 0
	num = 0
	for line in fh:
		lista.append(tratarLinea(line))
		count = count + 1
	
	print ("Finalizado, tratadas {} lineas \n".format(count))
except: 
	print("No se puede abrir el archivo: ", nombre)

for etiqueta in lista:
	print(etiqueta)
