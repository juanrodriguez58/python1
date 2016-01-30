# treating strings

def tratar(txt):
	print("Tratando ...", txt)
	txt = txt + "t"
	return txt



linea = input("Introduce la línea: ")
print ("Tratada", tratar(linea))