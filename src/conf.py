import mysql.connector

# Conectar a MySQL
try:
    myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3307",
    password="1234",
    database="temperaturas"
    )
    print("Conexión exitosa"+ str(myDB))
except:
    print("No se pudo conectar a la base de datos")