class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"se ha retirado el monto {amount}. saldo actual {self.balance}")

    def deactive_account(self):
        self.is_active = False
        print(f"la cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"la cuenta ha sido activada")

#Crear objetos
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

#llamada a los metodos
account1.deposit(200)
account1.deposit(100)

account1.deactive_account()
account1.deposit(50)

account1.activate_account()
account1.deposit(50)
