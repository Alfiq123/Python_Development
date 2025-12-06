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

INSERT INTO `Input User` (`Nama`, `Jumlah`, `Satuan`, `Tanggal Pembelian`, `Tanggal Kedaluwarsa`, `Kategori`)
    VALUES
        ("Tomat Merah",        600, "gram",  "2025-01-03", "2025-01-12", "Sayuran"),       -- Kedaluwarsa minggu ini
        ("Ikan Salmon",        1,   "kg",    "2025-01-08", "2025-01-14", "Daging"),            -- Kedaluwarsa minggu ini
        ("Pisang Cavendish",   12,  "pcs",   "2025-01-05", "2025-01-27", "Buah"),       -- Exp bulan ini
        ("Telur Ayam Kampung", 20,  "pcs",   "2025-01-10", "2025-01-30", "Lainnya"),  -- Exp bulan ini
        ("Susu Kental Manis",  3,   "pcs",   "2025-01-09", "2025-01-31", "Susu"),       -- Exp akhir bulan
        ("Roti Manis Coklat",  2,   "pcs",   "2025-01-11", "2025-01-15", "Roti"),       -- Exp minggu ini
        ("Bakso Sapi",         500, "gram",  "2025-01-04", "2025-01-13", "Daging"),         -- Hampir expired
        ("Selada Hijau",       300, "gram",  "2025-01-08", "2025-01-11", "Sayuran"),      -- Besok expired
        ("Blueberry Pack",     2,   "pcs",   "2025-01-06", "2025-01-23", "Buah"),          -- Bulan ini
        ("Yogurt Stroberi",    4,   "pcs",   "2025-01-09", "2025-01-17", "Susu"),         -- Minggu ini
        ("Keju Parmesan",      150, "gram",  "2025-01-10", "2025-03-01", "Susu"),        -- Masih panjang
        ("Madu Murni",         1,   "liter", "2025-01-02", "2026-12-30", "Lainnya"),         -- Sangat lama expired
        ("Nugget Ayam",        750, "gram",  "2025-01-07", "2025-02-14", "Daging"),        -- Bulan depan aman
        ("Bayam Jepang",       500, "gram",  "2025-01-10", "2025-01-12", "Sayuran"),      -- 2 hari lagi expired
        ("Apel Malang",        6,   "pcs",   "2025-01-08", "2025-01-29", "Buah");             -- Exp bulan ini
