from decimal import Decimal

class Account:
    """ Account class mainitaning account balance"""

    def __init__(self, name, balance):
        if balance <= Decimal("0.00"):
            raise ValueError("Invalial balance")
        self.name = name
        self.balance = balance
    
    def deposite(self, amount):
        if amount<Decimal('0.00'):
            raise ValueError('Amout must be positive')
        self.balance += amount
    
    """Withdrawing money"""
    def withdraw(self, money):
        if money>self.balance:
            raise ValueError('Withdraw amount must be less than or equal to balance')
        elif money == Decimal('0.00'):
            raise ValueError('Withdraw amount must be positive')
        self.balance -= money
name = input('Enter account holder name:')
val1 = float(input('Enter the account balance:'))
account1 = Account('Liptan',Decimal(val1))
print(account1.balance)
print(account1.name)
val2 = float(input('Enter deposite amount:'))
account1.deposite(Decimal(val2))
val3 = float(input('Enter the windraw amount:'))
account1.withdraw(Decimal(val3))
print(account1.balance)

