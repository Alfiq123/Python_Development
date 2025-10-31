import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="apache_123",
    database="python_mysql"
)

cursor = conn.cursor()

#
# ══════════ PHASE I ══════════ #
#

# ## Create Table - Person
# cursor.execute("""
#     CREATE TABLE Person (
#         name      VARCHAR(64),
#         age       SMALLINT UNSIGNED,
#         person_id INT PRIMARY KEY AUTO_INCREMENT
#     )
# """)

# ## Insert Data - Person
# cursor.execute("""
#     INSERT INTO Person (name, age)
#     VALUES (%s, %s)
# """, ("Tim", 19))

#
# ══════════ PHASE II ══════════ #
#

# ## Create Table - Test
# cursor.execute("""
#     CREATE TABLE Test (
#         name    VARCHAR(64) NOT NULL,
#         created datetime NOT NULL,
#         gender  ENUM("Male", "Female", "Other") NOT NULL,
#         id      INT PRIMARY KEY NOT NULL AUTO_INCREMENT
#     );
# """)

# ## Insert Data - Test
# cursor.execute("""
#     INSERT INTO `Test` (`name`, `created`, `gender`)
#     VALUES (%s, %s, %s)
# """, ("Olie", datetime.now(), "Other"))

# ## Alter Table - Add Food
# cursor.execute("""
#     ALTER TABLE `Test` ADD COLUMN `food` VARCHAR(64) NOT NULL;
# """)

# ## Alter Table - Remove Food
# cursor.execute(""" ALTER TABLE `Test` DROP `food`; """)

# ## Alter Table - Change Name
# cursor.execute(""" ALTER TABLE `Test` CHANGE `name` `first_name` VARCHAR(64); """)

#
# ══════════ PHASE III ══════════ #
#

# users = [
#     ("Aditya", "S!mpleP@ss2025"),
#     ("Maya", "Mk#2025!box"),
#     ("Rizal", "R1z@l_Hd!90")
# ]

# user_scores = [
#     (50, 100),
#     (30, 200),
#     (75, 125)
# ]

# Q1 = """
#     CREATE TABLE `User` (
#         `id`       INT PRIMARY KEY AUTO_INCREMENT,
#         `name`     VARCHAR(64),
#         `password` VARCHAR(64)
#     );
# """

# Q2 = """
#     CREATE TABLE `User_Score` (
#         `userId` INT PRIMARY KEY, FOREIGN KEY (`userId`) REFERENCES `User`(`id`),
#         `game_1` INT DEFAULT 0,
#         `game_2` INT DEFAULT 0
#     );
# """

# cursor.execute(Q1)
# cursor.execute(Q2)

# Q3 = "INSERT INTO `User` (`name`, `password`) VALUES (%s, %s)"
# Q4 = "INSERT INTO `User_Score` (`userId`, game_1, game_2) VALUES (%s, %s, %s)"

# for i, user in enumerate(users):
#     cursor.execute(Q3, user)
#     last_id = cursor.lastrowid
#     cursor.execute(Q4, (last_id,) + user_scores[i])

#
# ══════════ PHASE IV ══════════ #
#

conn.commit()

cursor.close()
conn.close()
