class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited")
    def withdraw(self,amount):
        if self.balance < amount:
            print("insuficeint money")
        else:
            self.balance -= amount
            print(f"{amount} successfully withdrawn")
    def check_balace(self):
        print(f" total balace is {self.balance}")


acc1 = BankAccount("Ayush",12000)
acc1.deposit(10000)
acc1.withdraw(12000)
acc1.check_balace()