class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def depostit(self,amount):
        if amount>0:
            self.balance=self.balance +amount
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount<= balance:
            self.balance = self.balance-amount
        else:
            print("Insufficent balance")

    def check_balance(self):
        print(self.balance)

account1=BankAccount(1000)
print(account1.balance)