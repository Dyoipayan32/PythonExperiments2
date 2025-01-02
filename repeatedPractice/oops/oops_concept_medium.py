'''
Problem 1:
A. Create a class 'Account' with a private attribute 'balance'.
B. Include a method 'deposit' for adding money and
   'withdraw' for withdrawing money ensuring the balance doesn’t become negative.
C. Solution should cover: Private attribute, and ensuring integrity of the data (no negative balances).
'''


class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Please enter deposit amount greater than zero")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Account balance {}, is not sufficient to withdraw: {}".format(self.__balance, amount))

    def get_balance(self):
        return self.__balance


acc = Account(50)
print(acc.get_balance())
acc.deposit(10)
print(acc.get_balance())
acc.withdraw(60)
print(acc.get_balance())
