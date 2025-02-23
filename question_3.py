class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
        self.__balance = balance

    def account_holder(self):
        return self.__account_holder

    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def display_balance(self)->None:
        print(f"your balance is {self.__balance}")

Account = BankAccount('Timothy', 500000)
Account.deposit(500)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=500,interest= 23):
        super().__init__(account_holder, balance)
        self.interest = interest

    def account_holder(self):
        return f"{self.__account_holder}"

    def add_interest(self, interest = 23):
        self.__balance += interest
        interest = interest / 100
        return interest


    def get_balance(self):
        return self.__balance

def display_balance(self)->None:
    print(f"your savings account balance is {self.__balance}")

Account_1 = SavingsAccount("Timothy", 5000,)
Account.display_balance()
Account_1.display_balance()
