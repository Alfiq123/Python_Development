### Soal 1: Sistem lahan pertanian

Sebuah sistem sederhana diperlukan untuk mengelola berbagai jenis lahan pertanian.
Semua lahan memiliki atribut dasar (luas dan lokasi) dan memerlukan operasi penanaman, 
cara penanaman dan pemeliharaannya berbeda sesuai jenis lahan.
Output berupa informasi tentang tanaman yang ditanam di sawah dan lahan kering.

1. Kelas `Lahan` (Superkelas) memiliki atribut dan metode secara umum.
2. Kelas `Sawah` (Subkelas) diidentifikasi dengan jenis irigasinya dan memiliki metode penanaman spesifik untuk padi.
3. Kelas `KebunKering` (Subkelas) tidak memerlukan irigasi dan memiliki metode penanaman spesifik untuk tanaman palawija.
4. Kelas `Sawah` dan `KebunKering` adalah kelas anak yang dibuat dengan mewarisi atribut dan metode dari kelas induk (Lahan) menggunakan `super().__init__()`. 
   Kedua kelas anak ini memiliki `luasHektar` dan lokasi serta metode `panen()`tanpa harus mendefinisikannya ulang.

---

### Soal 2: Kasus: Kebutuhan Pakan Ternak

1. `Peternakan` memiliki berbagai jenis `HewanTernak` (kelas induk).
2. `Sapi` dan `Kambing` adalah jenis khusus dari `HewanTernak` (Inheritance).
3. Setiap `HewanTernak` memiliki kebutuhan `Pakan` spesifik per hari. 
    - Misalkan kebutuhan pakan sapi harian terdiri dari pakan hijauan (10% dari berat badan) dan pakan konsentrat (2% dari berat badan). 
    - Sedangkan kebutuhan pakan harian kambing terdiri dari pakan hijauan (8% dari berat badan) dan pakan konsentrat (1% dari berat badan)
4. Sebuah `Peternakan` memiliki (mengelola) banyak `HewanTernak` (Aggregation). 
   Setiap `Pakan` terdiri dari beberapa `KomposisiPakan` (Misalnya: jenis serat, protein, mineral)
