print ("Hola")
lista = []
h = 1
while h > 0:
        hora = input("Escribe un numero? \n")
        try :
                h = int(hora);
                y = 3
                lista.append(h)
                if h > y:
                        print( hora, " es mayor que 3")   # miro si es mayor que 3
                else:
                        print( hora, " es menor o igual que 3")
        except :
                print("Tienes que introducir un número")
print (lista)
print ("Fin del programa")
