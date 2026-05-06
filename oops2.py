class car:
    def __init__(self,colour,brand):
        self.colour=colour
        self.brand=brand

    def display(self):
        print(f"The car brand is {self.brand} and car colour is {self.colour} ")

# new_car=car("orange","Toyota")
# new_car.display()

class Bankaccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdrawl(self,amount):
        if(0<amount<self.__balance):
            self.__balance-=amount
        else:
            print("In sufficient balance")
    def getbalance(self):
        return self.__balance 
bankbalance=Bankaccount()
# bankbalance.deposit(100)
# print(bankbalance.getbalance())
# bankbalance.withdrawl(50)
# print(bankbalance.getbalance())
# bankbalance.withdrawl(50)
# print(bankbalance.getbalance())
# print(bankbalance.getbalance())


class animal:

    def __init__(self,name):
        self.name=name

    def anipro(self):
        print(f"The dog name is {self.name}")
        
class analytics(animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def analy_breed(self):
        print(f"Animal name is {self.name} and breed is {self.breed}")

# anal=analytics("Ranbir kapoor","Rotwheeler")
# anal.analy_breed()
# anal.anipro()

class animal:

    def sound(self):
        return "every animal sound"
    
    def sleep(self):
        return "every animal sleep"

class dog(animal):

    def sound(self):
        return "Bow Bow"

class cat(animal):

    def sound(self):
        return "meow"
    
def make_sound(animal):
    print(animal.sound())

dg=dog()
ct=cat()
# make_sound(dg)
# make_sound(ct)


from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):

    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * (self.radius**2)
    

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth 
    
shapes=[circle(5),rectangle(2,10)]

for shapes_ in shapes:
    print(shapes_.area())




# Why Declare the shape Class?
# The shape class is necessary because it serves as an abstract base class (ABC), which defines a common interface (or contract) for all shapes. While it does not directly calculate anything, its purpose is to:

# Enforce a Standard Interface:

# By using the @abstractmethod decorator, the shape class ensures that every subclass (like circle and rectangle) must implement the area() method.
# This ensures consistency in how different shapes are handled in the program.
# Without the shape class, subclasses could define different method names (e.g., get_area() or calculate()), leading to confusion or errors when writing generalized code.