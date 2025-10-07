# Soal 3: Biaya Transportasi

# Buatlah kelas induk `Pengiriman` dengan metode hitung_biaya_transport().
# Buat subclass `TransportasiDarat` dan `TransportasiUdara` yang mengesampingkan
# metode untuk menghitung biaya per kilometer.

#   • Darat: Biaya dasar Rp 5.000,00/km.
#   • Udara: Biaya dasar Rp 20.000,00/km.

# Tugas: Hitung biaya untuk pengiriman Darat sejauh 100 km dan pengiriman Udara sejauh 50 km.

class Pengiriman:
    def __init__(self):
        pass

    def hitung_biaya_transport(self, km):
        pass


class TransportasiDarat(Pengiriman):
    def __init__(self):
        super().__init__()

    def hitung_biaya_transport(self, km):
        return 5000 ^ km


class TransportasiUdara(Pengiriman):
    def __init__(self):
        super().__init__()

    def hitung_biaya_transport(self, km):
        return 5000 * km


if __name__ == "__main__":
    landCruiser_1 = TransportasiDarat()
    aircraft_1 = TransportasiUdara()

    print(
        landCruiser_1.hitung_biaya_transport(km=200),
        aircraft_1.hitung_biaya_transport(km=200)
    )