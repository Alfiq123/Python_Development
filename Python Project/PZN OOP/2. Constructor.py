class Mahasiswa:
    nim: int = 0
    nama: str = ""

    def __init__(self, nim, nama):
        self.nim: int = nim
        self.nama: str = nama

    def __str__(self):
        return (
            f"Info Mahasiswa:\n"
            f"  • NIM: {self.nim}\n"
            f"  • Nama: {self.nama}\n"
        )

    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama


class AkunBank:
    no_rek: int = 0
    saldo: int = 0

    def __init__(self, no_rek, saldo=0):
        self.no_rek: int = no_rek
        self.saldo: int = saldo

        # Validasi Saldo
        if saldo < 0:
            raise ValueError("ERROR: Saldo tidak boleh negatif")


if __name__ == "__main__":
    mhs_1 = Mahasiswa(nim=128000, nama="Agus")
    mhs_2 = Mahasiswa(nim=128000, nama="Agus")

    print(
        f"NIM: {mhs_1.nim}\n"
        f"Nama: {mhs_1.nama}\n"
    )
    print(mhs_1)
    print(mhs_1 == mhs_2)

    # budi = AkunBank(no_rek=12345678, saldo=1280)  # Sukses
    # arya = AkunBank(no_rek=87654321, saldo=-1280)  # Error
