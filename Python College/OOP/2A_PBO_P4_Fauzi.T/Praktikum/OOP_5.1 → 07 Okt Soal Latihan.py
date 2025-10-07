# Soal 1: Perhitungan Pakan

# Buatlah kelas induk `HewanPeliharaan` dengan metode `hitung_pakan_harian()`.
# Kemudian buatlah subclass `Kucing` dan `Anjing` yang mengesampingkan metode
# tersebut untuk menghitung kebutuhan pakan (dalam gram) berdasarkan beratnya.

# Kebutuhan pakan:
#   • Kucing: berat badan. Kebutuhan pakan kucing: 2% dari berat badan.
#   • Anjing: berat badan. Kebutuhan pakan anjing: 3% dari berat badan

# Tugas: Tampilkan kebutuhan pakan untuk Kucing (berat 4 kg) dan
#        Anjing (berat 15 kg).

class HewanPeliharaan:
    def __init__(self): pass

    def hitung_pakan_harian(self, berat, persen):
        return berat * persen


class Kucing(HewanPeliharaan):
    def __init__(self): super().__init__()

    def hitung_pakan_harian(self, berat=4, persen=0.02):
        return (
            f"Kucing dengan berat: {berat:,} kg, "
            f"Membutuhkan pakan seberat: {(berat * 1000) * persen:,.2f} gram"
        )


class Anjing(HewanPeliharaan):
    def __init__(self): super().__init__()

    def hitung_pakan_harian(self, berat=15, persen=0.03):
        return (
            f"Anjing dengan berat: {berat:,} kg, "
            f"Membutuhkan pakan seberat: {(berat * 1000) * persen:,.2f} gram"
        )


if __name__ == "__main__":
    kucing = [Kucing() for _ in range(6)]
    anjing = [Anjing() for _ in range(6)]

    print(
        f"{kucing[0].hitung_pakan_harian()}\n"
        f"{anjing[0].hitung_pakan_harian()}\n"
        "\n"
        f"{kucing[1].hitung_pakan_harian(berat=8)}\n"
        f"{anjing[1].hitung_pakan_harian(berat=30)}\n"
        "\n"
        f"{kucing[2].hitung_pakan_harian(berat=24)}\n"
        f"{anjing[2].hitung_pakan_harian(berat=45)}\n"
    )
