import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", 
passwd="paltas", database="aivocado")

cur = cnn.cursor()
cur.execute("SELECT * FROM maduracion")
datos = cur.fetchall()

id,maduras,inmaduras = datos[0]


print('TENEMOS',maduras,'PALTAS MADURAS')
print('TENEMOS',inmaduras,'PALTAS INMADURAS')