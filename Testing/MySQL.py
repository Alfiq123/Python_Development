import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="apache_123",
    database="pythonDB"
)

dbcursor = db.cursor()

# dbcursor.execute("""
# CREATE TABLE Person (
#     name VARCHAR(50),
#     age SMALLINT UNSIGNED,
#     personID INT PRIMARY KEY AUTO_INCREMENT
# );
# """)

# dbcursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("tim", 19))
# db.commit()

dbcursor.execute("SHOW TABLES")
for table in dbcursor:
    print(table)
