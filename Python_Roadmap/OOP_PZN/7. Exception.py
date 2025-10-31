class BalanceNotEnough(Exception):
    def __init__(self, messege):
        self.messege = messege

    def __str__(self):
        return self.messege


class BankAccount:
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise BalanceNotEnough("Saldo tidak mencukupi")
        self.balance -= amount


if __name__ == "__main__":
    try:
        bank_account_1 = BankAccount(no="1234567890", balance=100)
        bank_account_1.transfer(amount=1000000)
    except BalanceNotEnough as e:
        print(f"Error: {e}")
