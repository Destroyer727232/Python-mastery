class BankAccount:
    def __init__(self):
        self.account_holder = ""
        self.account_number = ""
        self.balance = ""

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def set_account_holder(self,name):
        if name == "":
            return None
        else:
            self.account_holder = name

    def set_account_number(self,number):
        if number != 6:
            return None
        else:
            self.account_number = number

    def set_balance(self,amount):
        if amount < 0:
            return None
        else:
            self.balance = amount

    def deposit(self,amount):
        if amount != 0 or amount > 0:
            self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount != 0 or amount < 0 or amount > self.balance:
            self.balance = self.balance - amount

    def display_account_details(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.balance}")

account = BankAccount()
account.set_account_holder("Hemanth")
account.set_account_number("ACC123")
account.set_balance(10)
print(account.get_account_holder())
print(account.get_balance())
account.deposit(2000)
print(account.get_balance())
account.withdraw(1500)
print(account.get_balance())
account.set_account_holder("Hemanth Medagam")
account.display_account_details()
