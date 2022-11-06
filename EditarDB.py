import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", 
passwd="paltas", database="aivocado")

cursor = cnn.cursor()
cursor = cnn.cursor()
sql_update_query = """Update maduracion set Maduras = %s where id = %s"""
input_data = ('5', '1')
cursor.execute(sql_update_query, input_data)
cnn.commit()
print("Record Updated successfully ")