class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def display(self):
        print("Savings Balance:", self.balance)

class CurrentAccount(BankAccount):
    def display(self):
        print("Current Balance:", self.balance)

s = SavingsAccount(10000)
c = CurrentAccount(20000)

s.display()
c.display()