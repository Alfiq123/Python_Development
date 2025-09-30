# 8. Latihan Soal

Buatlah ode program sesuai studi kasus berikut!
Latihan 1: Peralatan Pertanian Umum

Buatlah Kelas Induk `AlatPertanian` dengan atribut `nama` dan `tenaga` (manual/mesin) serta metode `gunakan()`.
Buat Kelas Anak `Cangkul` dan `Traktor` yang mewarisi dari `AlatPertanian`.

- Cangkul harus meng-override `gunakan()` untuk menampilkan "Menggali tanah secara manual."
- Traktor harus meng-override `gunakan()` untuk menampilkan "Membajak lahan dengan mesin."

# Latihan 2: Klasifikasi Tanaman

Buat Kelas Induk Tanaman dengan atribut nama dan metode tumbuh().
Buat Kelas Anak TanamanPangan dan TanamanHias.

- `TanamanPangan` harus menambahkan atribut `masa_panen` (hari).
- `TanamanHias` harus menambahkan atribut `warna_bunga`.
- Kedua kelas anak harus memiliki metode `informasi_spesifik()` yang menampilkan data spesifiknya.

```py
print("Hallo")
```