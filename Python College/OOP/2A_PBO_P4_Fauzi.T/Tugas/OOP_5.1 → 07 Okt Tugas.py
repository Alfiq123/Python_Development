# 1. Kelas Induk (Superclass)
class Ternak:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        """Menampilkan informasi umum ternak."""
        print(f"Nama: {self.nama}, Umur: {self.umur} tahun.")

    def bersuara(self):
        """Metode dasar untuk mengeluarkan suara."""
        raise NotImplementedError(
            "Subclass harus mengimplementasikan metode bersuara."
        )

# 2. Kelas Anak (Subclass) dengan Overriding Metode
class Sapi(Ternak):
    def bersuara(self):
        """Implementasi spesifik suara Sapi."""
        return "Moo!"

class Ayam(Ternak):
    def bersuara(self):
        """Implementasi spesifik suara Ayam."""
        return "Kokok-petok!"

class Kambing(Ternak):
    def bersuara(self):
        """Implementasi spesifik suara Kambing."""
        return "Mbeeek!"

# 3. Fungsi Polimorfik
def aksi_ternak(hewan):
    """
    Fungsi yang memanggil metode bersuara() pada objek Ternak apa pun.
    Ini adalah contoh polimorfisme (Duck Typing).
    """
    hewan.info()
    print(f"Suara yang dikeluarkan: {hewan.bersuara()}")
    print("---")

# 4. Penggunaan Program
if __name__ == "__main__":
    sapi_perah = Sapi("Molly", 3)
    ayam_pedaging = Ayam("Jago", 1)
    kambing_etawa = Kambing("Bento", 2)

    daftar_ternak = [sapi_perah, ayam_pedaging, kambing_etawa]

    print("## Laporan Suara Ternak Harian ##")

    for ternak in daftar_ternak:
        aksi_ternak(ternak)
