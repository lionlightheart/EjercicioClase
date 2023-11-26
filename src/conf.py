import mysql.connector

# Conectar a MySQL
try:
    myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="1234",
    database="temperaturas"
    )
    print("Conexión exitosa"+ str(myDB))

except mysql.connector.Error as err:
    print("No se pudo conectar a la base de datos " + str(err))
