/* DATABASE BANK - AIVEN EDITION */

--                                                                   --
-- ════════════════════ MEMBUAT TABEL DAN KOLOM ════════════════════ --
--                                                                   --

# Membuat "DatabaseBank"
CREATE DATABASE "DatabaseBank";

# Menggunakan "DatabaseBank"
USE "DatabaseBank";

SELECT @@sql_mode;

# 1. Membuat Tabel "Nasabah"
CREATE TABLE "Nasabah"(
    "id_nasabah"    INT PRIMARY KEY,
    "nama"          VARCHAR(32),
    "nik"           VARCHAR(16),
    "alamat"        VARCHAR(64),
    "tanggal_lahir" DATE,
    "no_telepon"    VARCHAR(32)
);

# 2. Membuat Tabel "Rekening"
CREATE TABLE "Rekening"(
    "no_rekening"    INT PRIMARY KEY,
    "id_nasabah"     INT,
    "jenis_rekening" ENUM('Tabungan', 'Giro', 'Deposito'),
    "saldo"          DECIMAL(10,2),
    "tanggal_dibuka" DATE
);

# 3. Membuat Tabel "Transaksi"
CREATE TABLE "Transaksi"(
    "id_transaksi"      INT PRIMARY KEY,
    "no_rekening"       INT,
    "tanggal_transaksi" DATE,
    "jenis_transaksi"   ENUM('Setor', 'Tarik', 'Transfer'),
    "jumlah"            INT,
    "keterangan"        VARCHAR(128)
);

# 4. Membuat Tabel "Pegawai"
CREATE TABLE "Pegawai"(
    "id_pegawai" INT PRIMARY KEY,
    "nama"       VARCHAR(64),
    "jabatan"    VARCHAR(64),
    "id_cabang"  INT
);

# 5. Membuat Tabel "Cabang"
CREATE TABLE "Cabang"(
    "id_cabang"     INT PRIMARY KEY,
    "nama_cabang"   VARCHAR(64),
    "alamat_cabang" VARCHAR(64),
    "kota"          VARCHAR(64)
);

--                                          --
-- ══════════ RELASI ANTAR TABEL ══════════ --
--                                          --

# Relasi 1 → Nasabah bisa punya banyak rekening
ALTER TABLE "Rekening" 
    ADD FOREIGN KEY ("id_nasabah") 
        REFERENCES "Nasabah"("id_nasabah") 
        ON DELETE CASCADE 
        ON UPDATE CASCADE;

# Relasi 2 → Rekening bisa punya banyak transaksi
ALTER TABLE "Transaksi" 
    ADD FOREIGN KEY ("no_rekening") 
        REFERENCES "Rekening"("no_rekening") 
        ON DELETE CASCADE 
        ON UPDATE CASCADE;

# Relasi 3 → Cabang bisa punya banyak pegawai
ALTER TABLE "Pegawai" 
    ADD FOREIGN KEY ("id_cabang") 
        REFERENCES "Cabang"("id_cabang") 
        ON DELETE CASCADE 
        ON UPDATE CASCADE;

# Menambahkan Kolom Baru
-- ALTER TABLE "Pegawai" ADD "umur" INT;
-- ALTER TABLE "Pegawai" ADD "gender" VARCHAR(64);
-- ALTER TABLE "Cabang" ADD "provinsi" VARCHAR(64);

--                                                          --
-- ════════════════════ PENGISIAN DATA ════════════════════ --
--                                                          --

# Menambahkan data-data untuk tabel "Nasabah"
INSERT INTO "Nasabah" ("id_nasabah", "nama", "nik", "alamat", "tanggal_lahir", "no_telepon")
    VALUES
        (1,  'Andi Pratama',    '3174021201230001', 'Jl. Melati No. 14, Jakarta',    '1995-04-12', '081234567890'),
        (2,  'Siti Nurhaliza',  '3275032204560002', 'Jl. Kenanga No. 7, Bandung',    '1992-07-23', '082145678901'),
        (3,  'Budi Santoso',    '3578041909800003', 'Jl. Mawar No. 25, Surabaya',    '1980-09-19', '081355667788'),
        (4,  'Rina Kurniawati', '3374090503000004', 'Jl. Dahlia No. 31, Yogyakarta', '2000-03-05', '085266778899'),
        (5,  'Agus Salim',      '1675031012750005', 'Jl. Anggrek No. 9, Medan',      '1975-12-10', '081322334455'),
        (6,  'Maya Sari',       '3174080404880006', 'Jl. Flamboyan No. 12, Jakarta', '1988-04-04', '083145677889'),
        (7,  'Fajar Nugroho',   '3374100806990007', 'Jl. Teratai No. 17, Semarang',  '1999-06-08', '087822334466'),
        (8,  'Dewi Lestari',    '3275112211970008', 'Jl. Sakura No. 5, Bandung',     '1997-11-22', '081288990011'),
        (9,  'Yusuf Hidayat',   '3578061505890009', 'Jl. Cempaka No. 10, Surabaya',  '1989-05-15', '085312223344'),
        (10, 'Nur Aini',        '3374123012010010', 'Jl. Kamboja No. 3, Solo',       '2001-12-30', '081366778899');

# Menambahkan data-data untuk tabel "Rekening"
INSERT INTO "Rekening" ("no_rekening", "id_nasabah", "jenis_rekening", "saldo", "tanggal_dibuka")
    VALUES
        (100001, 1,  'Tabungan',  7500000.00, '2020-06-15'),
        (100002, 1,  'Deposito', 25000000.00, '2022-02-01'),
        (100003, 2,  'Tabungan', 12000000.00, '2019-08-20'),
        (100004, 3,  'Tabungan',  8500000.00, '2021-11-11'),
        (100005, 4,  'Tabungan',  5600000.00, '2023-04-05'),
        (100006, 5,  'Giro',     40000000.00, '2018-12-09'),
        (100007, 6,  'Tabungan', 10000000.00, '2021-02-14'),
        (100008, 7,  'Tabungan',  3400000.00, '2024-01-19'),
        (100009, 8,  'Deposito', 18000000.00, '2020-09-01'),
        (100010, 9,  'Tabungan',  9600000.00, '2019-05-23'),
        (100011, 9,  'Giro',     27500000.00, '2023-03-08'),
        (100012, 10, 'Tabungan',  4200000.00, '2024-05-02');

# Menambahkan data-data untuk tabel "Transaksi"
INSERT INTO "Transaksi" ("id_transaksi", "no_rekening", "tanggal_transaksi", "jenis_transaksi", "jumlah", "keterangan")
    VALUES
        (1,  100001, '2024-02-10', 'Setor',    2000000.00, 'Setoran tunai awal tahun'),
        (2,  100003, '2024-03-03', 'Tarik',    1500000.00, 'Penarikan untuk belanja'),
        (3,  100004, '2024-03-12', 'Setor',    3000000.00, 'Gaji bulan Maret'),
        (4,  100005, '2024-04-07', 'Transfer', 1000000.00, 'Transfer ke rekening 100012'),
        (5,  100012, '2024-04-07', 'Setor',    1000000.00, 'Menerima transfer dari 100005'),
        (6,  100006, '2024-04-15', 'Setor',   10000000.00, 'Deposit perusahaan'),
        (7,  100007, '2024-05-01', 'Tarik',    2000000.00, 'Bayar cicilan motor'),
        (8,  100009, '2024-05-19', 'Transfer', 5000000.00, 'Transfer ke rekening 100010'),
        (9,  100010, '2024-05-19', 'Setor',    5000000.00, 'Menerima transfer dari 100009'),
        (10, 100008, '2024-06-03', 'Setor',    1500000.00, 'Setoran tunai bulanan'),
        (11, 100002, '2024-07-11', 'Setor',    5000000.00, 'Penambahan deposito tahunan'),
        (12, 100011, '2024-07-22', 'Tarik',    7000000.00, 'Penarikan untuk investasi'),
        (13, 100003, '2024-08-04', 'Transfer', 2500000.00, 'Transfer ke rekening 100001'),
        (14, 100001, '2024-08-04', 'Setor',    2500000.00, 'Menerima transfer dari 100003'),
        (15, 100012, '2024-09-02', 'Tarik',    1200000.00, 'Penarikan tunai harian');

# Menambahkan data-data untuk tabel "Cabang"
INSERT INTO "Cabang" ("id_cabang", "nama_cabang", "alamat_cabang", "kota")
    VALUES
        (1, 'Cabang Jakarta Pusat',  'Jl. Sudirman No. 10',     'Jakarta'),
        (2, 'Cabang Bandung Utara',  'Jl. Dago No. 88',         'Bandung'),
        (3, 'Cabang Surabaya Timur', 'Jl. Darmo No. 45',        'Surabaya'),
        (4, 'Cabang Yogyakarta',     'Jl. Malioboro No. 12',    'Yogyakarta'),
        (5, 'Cabang Medan Kota',     'Jl. Gatot Subroto No. 5', 'Medan');

# Menambahkan data-data untuk tabel "Pegawai"
INSERT INTO "Pegawai" ("id_pegawai", "nama", "jabatan", "id_cabang", "umur", "gender")
    VALUES
        (1,  'Rudi Hartono',    'Manajer Cabang',   1, 42, 'L'),
        (2,  'Sari Wulandari',  'Teller',           1, 28, 'P'),
        (3,  'Dedi Kurniawan',  'Customer Service', 2, 31, 'L'),
        (4,  'Rina Setiawan',   'Manajer Cabang',   2, 38, 'P'),
        (5,  'Agung Prasetyo',  'Teller',           3, 26, 'L'),
        (6,  'Lina Marlina',    'Customer Service', 3, 29, 'P'),
        (7,  'Bambang Hidayat', 'Manajer Cabang',   4, 45, 'L'),
        (8,  'Dewi Puspita',    'Teller',           4, 27, 'P'),
        (9,  'Feriansyah',      'Customer Service', 5, 33, 'L'),
        (10, 'Nadia Rahmawati', 'Manajer Cabang',   5, 40, 'P');

# Merubah salah satu data
-- UPDATE "Nasabah" SET "nama" = "Nurul Iana" WHERE "nama" = "Nur Aini";
-- UPDATE "Rekening" SET "jenis_rekening" = "Giro" WHERE "no_rekening" = 100003;

# Menghapus salah satu data
-- DELETE FROM "Nasabah" WHERE "nama" = "Maya Sari";
-- DELETE FROM "Transaksi" WHERE "id_transaksi" = 100008;