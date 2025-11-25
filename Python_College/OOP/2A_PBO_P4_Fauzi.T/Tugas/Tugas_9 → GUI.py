# Import Modul "MySQL Connector"
import mysql.connector

# Membuat Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="apache_123",
    database="Biodata"
)

# Membuat Kursor
dbcursor = db.cursor()
