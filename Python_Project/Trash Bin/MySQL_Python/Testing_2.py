import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="apache_123",
    database="Minecraft_Elite"
)

kursor = koneksi.cursor()

# # Membuat Database "Minecraft_Elite"
# SQL_1 = """
#     CREATE DATABASE `Minecraft_Elite`;
#     USE `Minecraft_Elite`;
# """

# # Membuat Tabel - "Mobs"
# SQL_2 = """
#     CREATE TABLE `Mobs` (
#         `id_mob`    VARCHAR(64) PRIMARY KEY               NOT NULL,
#         `nama_mob`  VARCHAR(64)                           NOT NULL,
#         `kelas_mob` ENUM("Neutral", "Passive", "Hostile") NOT NULL,
#         `health`    INT                                   NOT NULL,
#         `kecepatan` DECIMAL(10,2)                         NOT NULL
#     );
# """

# # Membuat Tabel - "Senjata"
# SQL_3 = """
#     CREATE TABLE `Senjata` (
#         `id_senjata`   VARCHAR(64) PRIMARY KEY NOT NULL,
#         `nama_senjata` VARCHAR(64)             NOT NULL,
#         `damage`       DECIMAL(10,2)           NOT NULL
#     );
# """

# # Mengeksekusi Kode SQL
# kursor.execute(SQL_1)
# kursor.execute(SQL_2)
# kursor.execute(SQL_3)

mob_id = str(input("Masukkan ID Mob: "))
mob_nama = str(input("Masukkan Nama Mob: "))
mob_kelas = str(input("Masukkan Kelas Mob: "))
mob_health = int(input("Masukkan Health Mob: "))
mob_kecepatan = float(input("Masukkan Kecepatan Mob: "))

SQL_1_1 = """
    INSERT INTO `Mobs` (`id_mob`, `nama_mob`, `kelas_mob`, `health`, `kecepatan`)
    VALUES (%s, %s, %s, %s, %s)
"""

SQL_1_2 = (mob_id, mob_nama, mob_kelas, mob_health, mob_kecepatan)

kursor.execute(SQL_1_1, SQL_1_2)

koneksi.commit()

kursor.close()
koneksi.close()
