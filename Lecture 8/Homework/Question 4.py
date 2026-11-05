class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def show_balance(self):
        print(f"{self.owner}: Rs. {self.balance}")

class SavingsAccount(Account):
    def __init__(self,owner,balance,rate):
        super().__init__(owner,balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate / 100)

account1 = SavingsAccount("Hemanth",1000,10)
account1.deposit(1000)
account1.add_interest()
account1.show_balance()

