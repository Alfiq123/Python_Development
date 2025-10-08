### Soal 1: Perhitungan Pakan

Buatlah kelas induk `HewanPeliharaan` dengan metode `hitung_pakan_harian()`. 
Kemudian buatlah subclass `Kucing` dan `Anjing` yang mengesampingkan metode
tersebut untuk menghitung kebutuhan pakan (dalam gram) berdasarkan beratnya.

Kebutuhan pakan:

- Kucing: berat badan. Kebutuhan pakan kucing: 2% dari berat badan.
- Anjing: berat badan. Kebutuhan pakan anjing: 3% dari berat badan

Tugas: Tampilkan kebutuhan pakan untuk Kucing (berat 4 kg) dan Anjing (berat 15 kg).

---

### Soal 2: Laporan Kesehatan

Buatlah kelas induk `TernakSehat` dengan metode `cek_kesehatan()`.
Buat subclass `SapiPerah` dan `AyamPetelur` yang mengesampingkan
metode tersebut untuk memberikan laporan kesehatan khusus.

- `SapiPerah`: Cek produksi susu (normal jika liter/hari).
- `AyamPetelur`: Cek jumlah telur (normal jika butir/hari).

Tugas: Cetak laporan kesehatan untuk Sapi Perah (produksi 22 liter) dan Ayam Petelur (produksi 0 butir).

---

### Soal 3: Biaya Transportasi

Buatlah kelas induk `Pengiriman` dengan metode `hitung_biaya_transport()`.
Buat subclass `TransportasiDarat` dan `TransportasiUdara` yang
mengesampingkan metode untuk menghitung biaya per kilometer.

- Darat: Biaya dasar Rp 5.000,00/km.
- Udara: Biaya dasar Rp 20.000,00/km.

Tugas: Hitung biaya untuk pengiriman Darat sejauh 100 km dan pengiriman Udara sejauh 50 km.

---

### Soal 4: Proses Panen

Buat kelas induk `ProdukTernak` dengan metode `proses_panen()`.
Buat subclass `DagingSapi` dan `TelurAyam` yang mengesampingkan metode
tersebut untuk mendeskripsikan langkah-langkah panen yang berbeda.

---

### Soal 5: Analisis Investasi

Buat fungsi polimorfik `analisis_return(objek_investasi)`
yang menerima objek dari kelas `InvestasiTernak`
dan memanggil metode `hitung_return_tahunan()`.

Buat subclass `InvestasiDomba` dan `InvestasiBebek`
yang mengimplementasikan metode tersebut.

- `InvestasiDomba`: Return.
- `InvestasiBebek`: Return.

Tugas: Analisis return untuk investasi domba (Modal Rp 10.000.000,00) dan investasi bebek (Modal Rp 5.000.000,00).
