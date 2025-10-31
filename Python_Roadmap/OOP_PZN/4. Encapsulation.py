class AkunBank:
    __nama_rek: str = ""
    __balance: int = 0

    def __init__(self, nama_rek: str):
        self.__nama_rek: str = nama_rek

    @property
    def balance(self):
        return self.__balance

    @property
    def nama_rek(self):
        return self.__nama_rek

    def topup(self, amount: int):
        self.__balance += amount

    def cashout(self, amount: int):
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount


if __name__ == "__main__":
    eko_account = AkunBank(nama_rek="Eko")
    eko_account.topup(1000000)
    eko_account.topup(2000000)

    print(f"Nama Akun: {eko_account.nama_rek}")
    print(f"Saldo: Rp. {eko_account.balance:,}")

    eko_account.cashout(amount=500000)
    eko_account.cashout(amount=1000000)

    print(f"Saldo: Rp. {eko_account.balance:,}")
