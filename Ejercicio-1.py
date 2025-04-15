"""
1. Cree una clase de `BankAccount` que:
    1. Tenga un atributo de `balance`.
    2. Tenga un método para ingresar dinero.
    3. Tengo un método para retirar dinero.
    
    Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
    2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` 
    quede debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** 
    el `balance` quede arriba del `min_balance`.

"""


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance - self.min_balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal would result in balance below minimum balance.")