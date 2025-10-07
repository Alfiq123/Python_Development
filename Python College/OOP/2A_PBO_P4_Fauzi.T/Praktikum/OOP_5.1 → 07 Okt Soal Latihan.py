# 3. Soal Latihan

# Buatlah kode program Python dengan menerapkan konsep Polimorfisme melalui Method
# Overriding dan/atau Duck Typing.

# Soal 1: Perhitungan Pakan

# Buatlah kelas induk `HewanPeliharaan` dengan metode `hitung_pakan_harian()`.
# Kemudian buatlah subclass `Kucing` dan `Anjing` yang mengesampingkan metode
# tersebut untuk menghitung kebutuhan pakan (dalam gram) berdasarkan beratnya.

# Kebutuhan pakan:
#   • Kucing: berat badan. Kebutuhan pakan kucing: 2% dari berat badan.
#   • Anjing: berat badan. Kebutuhan pakan anjing: 3% dari berat badan

# Tugas: Tampilkan kebutuhan pakan untuk Kucing (berat 4 kg) dan Anjing (berat 15 kg).

class HewanPeliharaan:
    def __init__(self):
        pass

    def hitung_pakan_harian(self, berat, persen):
        return berat * persen


class Kucing(HewanPeliharaan):
    def __init__(self):
        super().__init__()

    def hitung_pakan_harian(self, berat=4000, persen=0.02):
        return berat * persen


class Anjing(HewanPeliharaan):
    def __init__(self):
        super().__init__()

    def hitung_pakan_harian(self, berat=15000, persen=0.03):
        return berat * persen


if __name__ == "__main__":

    kucing_1, kucing_2, kucing_3 = Kucing(), Kucing(), Kucing()
    anjing_1, anjing_2, anjing_3 = Anjing(), Anjing(), Anjing()

    print(
        f"Pakan Kucing: {kucing_1.hitung_pakan_harian()} gram\n"
        f"Pakan Anjing: {anjing_1.hitung_pakan_harian()} gram\n"
        "\n"
        f"Pakan Kucing: {kucing_2.hitung_pakan_harian(berat=8000)} gram\n"
        f"Pakan Anjing: {anjing_2.hitung_pakan_harian(berat=30000)} gram\n"
        "\n"
        f"Pakan Kucing: {kucing_2.hitung_pakan_harian(berat=24000)} gram\n"
        f"Pakan Anjing: {anjing_2.hitung_pakan_harian(berat=45000)} gram\n"
    )
