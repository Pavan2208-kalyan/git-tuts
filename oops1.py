# # class car:
# #     def __init__(self,name,project):
# #         self.name=name
# #         self.prject=project

# #     def animal(self):
# #         print(f"Animal has {self.name} and {self.prject}")

# # c1=car('Rolls Royce','This year 2025')
# # c1.animal()

# class Animal:
#     def __init__(self,name):
#         self.name=name
    
#     def ani_pro(self):
#         print(f"Dog name is {self.name}")
# class Dog(Animal):

#     def __init__(self, breed,name):
#         self.breed=breed
#         Animal.__init__(self,name)
#     def animal_info(self):
#         print(f"Animal name is {self.name} and breed is {self.breed}")

# c1=Dog("Britania",'Pamerian')
# c1.animal_info()
# (c1.ani_pro())

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
    
c1=circle(5)
print(c1.area())
c2=rectangle(8,7)
print(c2.area())