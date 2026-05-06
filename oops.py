# oops concepts
class Car:
    def __init__(self,brand,colour,price):
        self.brand=brand
        self.colour=colour
        self.price=price
    def display_info(self):
        print(f"car brand is {self.brand} and colur is {self.colour}")
    
    def car_price(self):
        print(f"car price is {self.price}")

temp1=Car("Rolls Royce","Black","20,00000")
temp1.car_price()

# 2. Encapsulation is the concept of restricting access to certain data or methods of a class to protect the data from being modified unintentionally.
#  This is achieved in Python by using private attributes and methods (prefixing with an underscore _ or double underscore __).

class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if(0<amount<self.__balance):
            self.__balance-= amount
        else:
            print("Insufficient Balance")
    def get_balance(self):
        return self.__balance

# balance=BankAccount()
# balance.deposit(100)
# print(balance.get_balance())
# balance.withdraw(200)
# print(balance.get_balance())

## Inhetritance

# Inheritance is the concept of creating a new class (child class) from an existing class (parent class).
#  The child class inherits the attributes and methods of the parent class and can have its own additional properties and methods.

#Example1
class Animal:
    def __init__(self,name):
        self.name=name
    def ani_pro(self):
        return f"Dog name is {self.name}"
        
class Dog(Animal):
    def __init__(self,breed,name):
        Animal.__init__(self,name)
        self.breed=breed
    
dog=Dog("Britania","pamerian")

# print(dog.ani_pro())
# print(dog.breed)
# print(dog.name)

# Example 2
# Parent class
class analytics:
    def __init__(self,brand,engine):
        self.brand=brand
        self.engine=engine
    def start_engine(self):
        return f"{self.engine} has started "
#child class 1
class car(analytics):
    def __init__(self, brand, engine,doors):
        super().__init__(brand, engine)
        self.doors=doors
    def vehicle_display(self):
        return f"{self.brand} has {self.engine} and {self.doors} doors"

class bike(analytics):
    def __init__(self, brand, engine,side_doors):
        super().__init__(brand, engine)
        self.side_doors=side_doors
        self.side_doors= "Has side doors" if self.side_doors else "No side doors"
    def bike_doors(self):
        return f"{self.brand} has {self.engine} many {self.side_doors} ,how may side doors {self.side_doors}"

car1=car("Toyato","Toyato engine","4")
bike2=bike("Hunter","250 cc hunter engine",False)
# print(car1.start_engine())
# print(car1.vehicle_display())
# print(bike2.start_engine())
# print(bike2.bike_doors())

"""Polymorphism allows the same operation to behave differently on different classes. 
It can be achieved through method overriding and method overloading 
(though Python doesn't support overloading directly, we simulate it with default parameters or variable arguments).

Example of Method Overriding"""

class Animal:
    def sound(self):
        return "every sound has a unique voice"
    
    def sleep(self):
        return "every animal sleeps"
class Dog(Animal):
    def sound(self):
        return "bow! bow!"
class Cat(Animal):
    def sound(self):
        return "Meow Meow"
    

def make_sound(animal):
    print(animal.sound())

dog=Dog()
cat=Cat()

# make_sound(dog)
# make_sound(cat)
# print(dog.sleep() )
#make_sound

# In this example:

# The sound method is overridden in both Dog and Cat.
# The make_sound function accepts any object that has a sound method, regardless of its class.
# This allows different animal types to provide their specific sounds.

# Method overloading

class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()
# print(calc.add(5, 10))  # Output: 15
# print(calc.add(5))      # Output: 5 (using the default value of b)

# Abstractions
from abc import ABC, abstractmethod


class shape:
    @abstractmethod
    
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14* ((self.radius)**2)

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth
        
# circ=circle(5)
# rec=rectangle(5,4)

# print(circ.area())
# print(rec.area())


# shapes=[circle(5),rectangle(5,4)]

# for shape_ in shapes:
#     print(shape_.area())






    

        
    

