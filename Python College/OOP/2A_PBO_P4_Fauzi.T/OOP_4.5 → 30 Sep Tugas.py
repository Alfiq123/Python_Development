# ## Latihan 5: menghitung harga tiket

# • Buatlah sebuah program untuk menghitung harga tiket bioskop
#   yang menerapkan konsep inheritance.
# • Buatlah superclass `Tiket` dan subclass:
#   • `TiketBiasa`,
#   • `TiketVIP`, dan
#   • `TiketGold`.
# • Setiap subclass memiliki atribut dan method berisi harga tiket
#   yang berbeda-beda.

class Tiket:
    def __init__(self, harga):
        self.harga = harga

    def hitung_total(self, jumlah):
        return self.harga * jumlah


# Tiket Biasa → Rp. 30.000
class TiketBiasa(Tiket):
    def __init__(self):
        super().__init__(harga=30000)


# Tiket VIP → Rp. 50.000
class TiketVIP(Tiket):
    def __init__(self):
        super().__init__(harga=50000)


# Tiket Gold → Rp. 70.000
class TiketGold(Tiket):
    def __init__(self):
        super().__init__(harga=70000)


if __name__ == "__main__":
    tanya_jenis = input(
        "Masukkan jenis tiket (Biasa/Vip/Gold): "
    ).lower()
    tanya_jumlah = int(input("Masukkan jumlah tiket: "))

    if tanya_jenis == "biasa": tiket = TiketBiasa()
    elif tanya_jenis == "vip": tiket = TiketVIP()
    elif tanya_jenis == "gold": tiket = TiketGold()
    else: print("Jenis tiket tidak valid."); exit()

    total = tiket.hitung_total(tanya_jumlah)
    print(f"Total Harga Tiket : Rp {total:,}")
