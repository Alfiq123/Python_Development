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
    def __init__(self):
        pass

    def metode_tiket(self):
        pass


class TiketBiasa(Tiket):
    def __init__(self):
        super().__init__()

    def metode_tiket_biasa(self):
        pass


class TiketVIP(Tiket):
    def __init__(self):
        super().__init__()

    def metode_tiket_vip(self):
        pass


class TiketGold(Tiket):
    def __init__(self):
        super().__init__()

    def metode_tiket_gold(self):
        pass


if __name__ == "__main__":
    tanya_jenis = str(input("Masukkan jenis tiket (Biasa/Vip/Gold): "))
    tanya_jumlah = int(input("Masukkan jumlah tiket: "))
