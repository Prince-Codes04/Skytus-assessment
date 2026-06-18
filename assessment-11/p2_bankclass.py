class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited Amount:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn Amount:", amount)

    def display(self):
        print("Current Balance:", self.balance)

acc = BankAccount(10000)

print("Initial Balance:", acc.balance)

acc.deposit(5000)
acc.withdraw(2000)

acc.display()