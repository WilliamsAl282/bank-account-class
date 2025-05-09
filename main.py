# Alex Williams
# 5/6/2025
# Three Ways to Modify BankAccount Class Attributes



# A simple class that models a bank account
class BankAccount:

    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance + amount
            print(f'The added fund of {amount} was added to your {self.balance}')
        else:






