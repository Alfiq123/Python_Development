CREATE DATABASE `Kedaluwarsa`;

USE `Kedaluwarsa`;

CREATE TABLE `Input User` (
    `Nama`                VARCHAR(64) PRIMARY KEY,
    `Jumlah`              INT,
    `Satuan`              ENUM("gram", "kg", "pcs", "ml", "liter"),
    `Tanggal Pembelian`   DATE,
    `Tanggal Kedaluwarsa` DATE,
    `Kategori`            ENUM("Daging", "Sayuran", "Buah", "Susu", "Roti", "Lainnya")
);

INSERT INTO `Input User` (`Nama`, `Jumlah`, `Satuan`, `Tanggal Pembelian`, `Tanggal Kedaluwarsa`, `Kategori`) 
    VALUES
        ("Daging Sapi Has Dalam", 1500, "gram", "2025-01-12", "2025-01-20", "Daging"),
        ("Wortel",                1,   "kg",    "2025-01-10", "2025-01-25", "Sayuran"),
        ("Apel Fuji",             5,   "pcs",   "2025-01-09", "2025-01-18", "Buah"),
        ("Susu UHT Full Cream",   2,   "liter", "2025-01-11", "2025-01-28", "Susu"),
        ("Roti Tawar Gandum",     1,   "pcs",   "2025-01-13", "2025-01-17", "Roti"),
        ("Ayam Fillet",           750, "gram",  "2025-01-14", "2025-01-21", "Daging"),
        ("Bayam Segar",           500, "gram",  "2025-01-10", "2025-01-13", "Sayuran"),
        ("Jeruk Medan",           10,  "pcs",   "2025-01-08", "2025-01-22", "Buah"),
        ("Keju Cheddar",          250, "gram",  "2025-01-12", "2025-02-10", "Susu"),
        ("Mentega",               200, "gram",  "2025-01-09", "2025-06-09", "Lainnya");
