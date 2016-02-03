import sqlite3
conn = sqlite3.connect('musica.sqlite3')
cur = conn.cursor()

# cur.execute("CREATE TABLE Canciones (titulo TEXT, numero INTEGER)")

cur.execute("INSERT INTO Canciones (titulo, numero) VALUES (?,?)", ("Tres",3))

conn.commit()

cur.execute("SELECT titulo, numero FROM Canciones")
for fila in cur:
    print(fila[0])
