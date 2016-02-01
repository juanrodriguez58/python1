fh = open("Romeo.txt", "r")

count = 0
for line in fh:
    print ("-->", line.strip())
    count = count + 1

print (count,"Lineas")
linea = input()
f = open("myfile.txt", "w", encoding="utf-8")
f.write(linea)
f.close