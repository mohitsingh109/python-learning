class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!!"


dog = Dog("Jack")
print(dog.speak())
print(dog.name)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Mohit", 1000)
print(account.owner)
print(account.get_balance())
account.deposit(10)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())

account.owner = "Mohit Singh"
print(account.owner)

account.__setattr__("phone", "7888770232")
print(account.__getattribute__("phone"))
