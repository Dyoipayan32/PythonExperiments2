"""
10. Develop a Python program which has a base class "BankAccount" and derived classes "CheckingAccount" and "SavingsAccount".
Implement common functionality in the base class and unique methods in the derived classes.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class CheckingAccount(BankAccount):
    def write_check(self, amount):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        pass
