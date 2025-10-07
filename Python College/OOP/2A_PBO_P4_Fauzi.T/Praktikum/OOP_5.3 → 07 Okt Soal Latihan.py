# Soal 3: Biaya Transportasi

# Buatlah kelas induk `Pengiriman` dengan metode `hitung_biaya_transport()`.
# Buat subclass `TransportasiDarat` dan `TransportasiUdara` yang
# mengesampingkan metode untuk menghitung biaya per kilometer.

#   • `Darat`: Biaya dasar Rp 5.000,00/km.
#   • `Udara`: Biaya dasar Rp 20.000,00/km.

# Tugas: Hitung biaya untuk pengiriman Darat sejauh 100 km dan
#        pengiriman Udara sejauh 50 km.

class Pengiriman:
    def __init__(self): pass
    def hitung_biaya_transport(self, km): pass


class TransportasiDarat(Pengiriman):
    def __init__(self): super().__init__()
    def hitung_biaya_transport(self, km):
        return (
            f"Pengiriman Darat sejauh {km} km dikenakan biaya sebesar "
            f"Rp {5000 * km:,}"
        )


class TransportasiUdara(Pengiriman):
    def __init__(self): super().__init__()
    def hitung_biaya_transport(self, km):
        return (
            f"Pengiriman Udara sejauh {km} km dikenakan biaya sebesar "
            f"Rp {20000 * km:,}"
        )


if __name__ == "__main__":
    tpDarat = [TransportasiDarat() for _ in range(6)]
    tpudara = [TransportasiUdara() for _ in range(6)]

    print(
        # Tugas
        f"{tpDarat[0].hitung_biaya_transport(km=100)}\n"
        f"{tpudara[0].hitung_biaya_transport(km=50)}\n"
        "\n"
        f"{tpDarat[1].hitung_biaya_transport(km=128)}\n"
        f"{tpudara[1].hitung_biaya_transport(km=64)}\n"
        "\n"
        f"{tpDarat[2].hitung_biaya_transport(km=30)}\n"
        f"{tpudara[2].hitung_biaya_transport(km=221)}\n"
        "\n"
        f"{tpDarat[3].hitung_biaya_transport(km=631)}\n"
        f"{tpudara[3].hitung_biaya_transport(km=941)}\n"
        "\n"
        f"{tpDarat[4].hitung_biaya_transport(km=431)}\n"
        f"{tpudara[4].hitung_biaya_transport(km=748)}\n"
        "\n"
        f"{tpDarat[5].hitung_biaya_transport(km=139)}\n"
        f"{tpudara[5].hitung_biaya_transport(km=776)}\n"
    )
