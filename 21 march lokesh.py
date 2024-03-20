class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(f"{person1.name} is {person1.age} years old.")



class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("12345")
account.deposit(1000)
account.withdraw(500)
print("Balance:", account.get_balance())

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"{self.make} {self.model}"
class Car(Vehicle):
    def start_engine(self):
        return "Engine started"

car = Car("Toyota", "Corolla")
print(car.get_info())
print(car.start_engine())