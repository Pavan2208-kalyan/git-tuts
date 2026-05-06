# class calculator:
#     def add(self,a,b=0):
#         return a+b
    
# calc=calculator()

# print(calc.add(10,5))
# print(calc.add(5))


from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
       self.radius=radius

    def area(self):
        return 3.14 * ((self.radius)**2)
    
class rectangle(shape):
    def __init__(self,length,breadth):
       self.length=length
       self.breadth=breadth

    def area(self):
        return self.length * self.breadth
    
cir=circle(5)
rec=rectangle(10,6)

print(cir.area())
print(rec.area())




