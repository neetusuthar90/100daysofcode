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


account1 = Account('Liptan',Decimal('50.00'))
print(account1.balance)
print(account1.name)
account1.deposite(Decimal('145.75'))
print(account1.balance)
account1.deposite(Decimal('-200.00'))
