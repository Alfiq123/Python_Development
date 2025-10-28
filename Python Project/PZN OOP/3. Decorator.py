class Matematika:

    @staticmethod  # Method yang berdiri sendiri
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b


class AkunBank:
    no_rek: int = 0
    balance: int = 0
    active: bool = True

    def __init__(self, no_rek, balance=0):
        self.no_rek = no_rek
        self.balance = balance

    @classmethod
    def disabled(cls, no_rek, balance=0):
        result = cls(no_rek, balance)
        result.active = False
        return result


class Kategogri:
    _nama: str = ""

    # def set_nama(self, nama):
    #     if nama == "":
    #         raise ValueError("Nama tidak boleh kosong")
    #     self._nama = nama

    # def get_nama(self):
    #     return self._nama

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama):
        if nama == "":
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama


if __name__ == "__main__":
    print(f"{Matematika.tambah(a=12, b=24)}\n"
          f"{Matematika.kurang(a=32, b=16)}\n")

    akun_bank_1 = AkunBank(no_rek=1, balance=10000)
    akun_bank_2 = AkunBank.disabled(no_rek=2, balance=20000)

    print(f"Bank Account {akun_bank_1.no_rek} has balance {akun_bank_1.balance} and status {akun_bank_1.active}\n"
          f"Bank Account {akun_bank_2.no_rek} has balance {akun_bank_2.balance} and status {akun_bank_2.active}\n")

    kategori_1 = Kategogri()
    kategori_1.nama = "Laptop"
    print(kategori_1.nama)

    # kategori_1.set_nama(nama="Laptop")
    # print(kategori_1.get_nama())
