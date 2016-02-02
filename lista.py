# listas
lista = []
nombre = "inicio"
while nombre != "fin": 
	elemento = input("Introduce un nombre: \n")
	lista.append(elemento)
	nombre = elemento

c=0
lista.remove("fin")
lista.sort()
for i in lista:
	c=c+1
	print(c, ".- ", i)
print("fin")
