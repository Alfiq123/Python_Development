CREATE DATABASE "Kedaluwarsa";

DROP DATABASE "Kedaluwarsa";

USE "Kedaluwarsa";

CREATE TABLE "Bahan Makanan" (
    "ID"                  INT PRIMARY KEY AUTO_INCREMENT,
    "Nama"                VARCHAR(64) UNIQUE,
    "Jumlah"              INT,
    "Satuan"              ENUM('gram', 'kg', 'pcs', 'ml', 'liter'),
    "Tanggal Pembelian"   DATE,
    "Tanggal Kedaluwarsa" DATE,
    "Kategori"            ENUM('Daging', 'Sayuran', 'Buah', 'Susu', 'Roti', 'Lainnya')
);

TRUNCATE TABLE "Bahan Makanan";

INSERT INTO "Bahan Makanan" ("Nama", "Jumlah", "Satuan", "Tanggal Pembelian", "Tanggal Kedaluwarsa", "Kategori") 
    VALUES
        ('Daging Sapi',         1500, 'gram',  '2025-01-12', '2025-01-20', 'Daging'),
        ('Wortel',              1,    'kg',    '2025-01-10', '2025-01-25', 'Sayuran'),
        ('Apel Fuji',           5,    'pcs',   '2025-01-09', '2025-01-18', 'Buah'),
        ('Susu UHT Full Cream', 2,    'liter', '2025-01-11', '2025-01-28', 'Susu'),
        ('Roti Tawar Gandum',   1,    'pcs',   '2025-01-13', '2025-01-17', 'Roti'),
        ('Ayam Fillet',         750,  'gram',  '2025-01-14', '2025-01-21', 'Daging'),
        ('Bayam Segar',         500,  'gram',  '2025-01-10', '2025-01-13', 'Sayuran'),
        ('Jeruk Medan',         10,   'pcs',   '2025-01-08', '2025-01-22', 'Buah'),
        ('Keju Cheddar',        250,  'gram',  '2025-01-12', '2025-02-10', 'Susu'),
        ('Mentega',             200,  'gram',  '2025-01-09', '2025-06-09', 'Lainnya'),
        ('Tomat Merah',         600,  'gram',  '2025-01-03', '2025-01-12', 'Sayuran'),
        ('Ikan Salmon',         1,    'kg',    '2025-01-08', '2025-01-14', 'Daging'),
        ('Pisang Cavendish',    12,   'pcs',   '2025-01-05', '2025-01-27', 'Buah'),
        ('Telur Ayam Kampung',  20,   'pcs',   '2025-01-10', '2025-01-30', 'Lainnya'),
        ('Susu Kental Manis',   3,    'pcs',   '2025-01-09', '2025-01-31', 'Susu'),
        ('Roti Manis Coklat',   2,    'pcs',   '2025-01-11', '2025-01-15', 'Roti'),
        ('Bakso Sapi',          500,  'gram',  '2025-01-04', '2025-01-13', 'Daging'),
        ('Selada Hijau',        300,  'gram',  '2025-01-08', '2025-01-11', 'Sayuran'),
        ('Blueberry Pack',      2,    'pcs',   '2025-01-06', '2025-01-23', 'Buah'),
        ('Yogurt Stroberi',     4,    'pcs',   '2025-01-09', '2025-01-17', 'Susu'),
        ('Keju Parmesan',       150,  'gram',  '2025-01-10', '2025-03-01', 'Susu'),
        ('Madu Murni',          1,    'liter', '2025-01-02', '2026-12-30', 'Lainnya'),
        ('Nugget Ayam',         750,  'gram',  '2025-01-07', '2025-02-14', 'Daging'),
        ('Bayam Jepang',        500,  'gram',  '2025-01-10', '2025-01-12', 'Sayuran'),
        ('Apel Malang',         6,    'pcs',   '2025-01-08', '2025-01-29', 'Buah');

INSERT INTO "Bahan Makanan" ("Nama", "Jumlah", "Satuan", "Tanggal Pembelian", "Tanggal Kedaluwarsa", "Kategori") 
VALUES
-- Kategori: Daging (Segar & Olahan)
('Daging Sapi Giling',   500, 'gram', '2025-10-27', '2025-10-30', 'Daging'), -- 3 hari lagi
('Ayam Fillet Dada',     1,   'kg',   '2025-10-27', '2025-10-29', 'Daging'), -- 2 hari lagi
('Sosis Kanzler Beef',   3,   'pcs',  '2025-10-25', '2025-12-25', 'Daging'), -- 2 bulan
('Ikan Salmon Norwegia', 200, 'gram', '2025-10-27', '2025-11-03', 'Daging'), -- 1 minggu
('Nugget Fiesta',        1,   'kg',   '2025-10-20', '2026-10-20', 'Daging'), -- 1 tahun (Frozen)
('Corned Beef Pronas',   2,   'pcs',  '2025-09-01', '2027-09-01', 'Daging'), -- Jangka panjang (Kaleng)
-- Kategori: Sayuran
('Bayam Hijau',     2,   'pcs',  '2025-10-27', '2025-10-29', 'Sayuran'), -- Sangat cepat busuk
('Wortel Brastagi', 500, 'gram', '2025-10-26', '2025-11-10', 'Sayuran'), -- 2 minggu
('Kentang Dieng',   2,   'kg',   '2025-10-20', '2025-11-20', 'Sayuran'), -- 1 bulan
('Brokoli Segar',   1,   'pcs',  '2025-10-27', '2025-11-01', 'Sayuran'), -- 5 hari
('Bawang Putih',    250, 'gram', '2025-10-15', '2026-01-15', 'Sayuran'), -- 3 bulan
-- Kategori: Buah
('Pisang Cavendish', 1,   'pcs',  '2025-10-26', '2025-10-31', 'Buah'), -- Cepat matang
('Apel Fuji',        1,   'kg',   '2025-10-25', '2025-11-15', 'Buah'), -- 3 minggu
('Jeruk Mandarin',   500, 'gram', '2025-10-25', '2025-11-08', 'Buah'), -- 2 minggu
('Anggur Merah',     250, 'gram', '2025-10-27', '2025-11-03', 'Buah'), -- 1 minggu
-- Kategori: Susu (Dairy)
('Susu UHT Ultra Milk',       1,   'liter', '2025-10-01', '2026-06-01', 'Susu'), -- Jangka panjang
('Susu Pasteurisasi Diamond', 1,   'liter', '2025-10-27', '2025-11-05', 'Susu'), -- Pendek (Fresh milk)
('Yogurt Cimory',             200, 'ml',    '2025-10-25', '2025-12-10', 'Susu'), -- 1.5 bulan
('Keju Cheddar Kraft',        165, 'gram',  '2025-10-10', '2026-04-10', 'Susu'), -- 6 bulan
-- Kategori: Roti
('Roti Tawar Sari Roti', 1, 'pcs', '2025-10-27', '2025-11-01', 'Roti'), -- 5 hari
('Roti Gandum',          1, 'pcs', '2025-10-26', '2025-10-30', 'Roti'), -- 4 hari
('Donat Gula',           6, 'pcs', '2025-10-27', '2025-10-28', 'Roti'), -- 1 hari (Besok)
-- Kategori: Lainnya
('Telur Ayam Negeri',    1,   'kg',    '2025-10-27', '2025-11-17', 'Lainnya'), -- 3 minggu
('Kecap Bango',          500, 'ml',    '2025-08-01', '2027-08-01', 'Lainnya'), -- Sangat panjang
('Minyak Goreng Bimoli', 2,   'liter', '2025-09-15', '2027-03-15', 'Lainnya'); -- Sangat panjang
