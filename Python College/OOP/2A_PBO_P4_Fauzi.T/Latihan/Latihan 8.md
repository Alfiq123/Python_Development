# 8. Latihan Soal

Buatlah ode program sesuai studi kasus berikut!

---

## Latihan 1: Peralatan Pertanian Umum

Buatlah Kelas Induk `AlatPertanian` dengan atribut `nama` dan `tenaga` (manual/mesin) serta metode `gunakan()`.
Buat Kelas Anak `Cangkul` dan `Traktor` yang mewarisi dari `AlatPertanian`.

- Cangkul harus meng-override `gunakan()` untuk menampilkan "Menggali tanah secara manual."
- Traktor harus meng-override `gunakan()` untuk menampilkan "Membajak lahan dengan mesin."

## Latihan 2: Klasifikasi Tanaman

Buat Kelas Induk Tanaman dengan atribut nama dan metode tumbuh().
Buat Kelas Anak TanamanPangan dan TanamanHias.

- `TanamanPangan` harus menambahkan atribut `masa_panen` (hari).
- `TanamanHias` harus menambahkan atribut `warna_bunga`.
- Kedua kelas anak harus memiliki metode `informasi_spesifik()` yang menampilkan data spesifiknya.

## Latihan 3: Transportasi Hasil Tani

Buat Kelas Induk `Kendaraan` dengan atribut `kapasitas_muatan` dan metode `angkut()`.
Buat Kelas Anak `PickUp` dan `Truk`.

- Kedua kelas harus menginisialisasi kapasitas muatan melalui `super()`.
- Kedua kelas harus meng-*override* `angkut()`:
  - `PickUp`: "Mengangkut hasil tani dengan kecepatan tinggi di jalan desa."
  - `Truk`: "Mengangkut hasil tani dalam jumlah besar ke pasar kota."

## Latihan 4: Pengelolaan Hama (Pewarisan Bertingkat)

Buat Kelas Induk `Organisme` (`metode hidup()`).
Buat Kelas Anak `Hama` (mewarisi dari `Organisme`, atribut `tingkat_kerusakan`). 
Buat Kelas `Ulat` dan `Wereng` (mewarisi dari `Hama`).

- `Ulat` dan `Wereng` harus memiliki metode `serang_tanaman()` yang berbeda-beda.
- Gunakan `super()` untuk inisialisasi bertingkat.

## Latihan 5: menghitung harga tiket

- Buatlah sebuah program untuk menghitung harga tiket bioskop yang menerapkan konsep inheritance.
- Buatlah superclass `Tiket` dan subclass:
  - `TiketBiasa`,
  - `TiketVIP`, dan
  - `TiketGold`.
- Setiap subclass memiliki atribut dan method berisi harga tiket yang berbeda-beda.
- Output yang diharapkan dari program ini adalah seperti berikut:

```txt
Masukkan jenis tiket (biasa/vip/gold) : (input dari user)
Masukkan jumlah tiket : (input dari user)
Total Harga Tiket : Rp (Output Hasil perhitungan sistem)
```
