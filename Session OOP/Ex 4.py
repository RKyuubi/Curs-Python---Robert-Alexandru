class BankAccount:
    def __init__(self, owner, balance):
        self.name = owner
        self.balance = balance

    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"Deposit {amount}")
            return True
        else:
            print("Deposit value must be positive")
            return False
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Not enough money")
            return False
        else:
            self.balance -= amount
            print(f"Withdrew {amount}")
            return True

    def __str__(self):
        return f"BankAccount {self.name} balance: {self.balance}"

if __name__ == "__main__":
    bankaccount = BankAccount("Robert Alexandru", 0)
    bankaccount.deposit(1000)
    print(bankaccount)
    bankaccount.withdraw(2000)
    print(bankaccount)