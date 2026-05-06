# String reversal
# Reverse of a string

# name_of_a_string="Analytics vidya"
# rev_string=""

# for char in name_of_a_string:
#     rev_string=char + rev_string
# print(rev_string)

# approach 2
"""
name_of_a_string="Analytics vidya"
print(name_of_a_string[::-1])"""

## Appraoch 3
# sorting a list in python

my_list=[4,3,2,1]
my_list.sort()
#print(my_list)

# Access, delete ,update element in numpy

# import numpy as np

# arr1=[2,3,4,5]
# x=np.delete(arr1,0)
# print(type(x))

list1 = ["apple", "banana", "cherry", "date", "elderberry"]
list2 = ["fig", "grape", "honeydew", "kiwi", "lemon"]

list3=[x+y for x,y in zip(list1,list2)]
#print(list3)


my_list=[4,3,2,1]
squaree=list(map(lambda x:x**2 ,my_list))
#print(squaree)

name_of_a_string="Analytics vidya"

# b=(name_of_a_string.split(" "))
# print(b)

# c='-'.join(b)
# print(c)


#
f=open("temp1.txt",mode='r')
contents=f.read()
#print(contents)


def args(*args,**kwargs):
    print(args,kwargs)
#args(1,2,3,A=10,B=19,C=100)

with open("temp1.txt",'r') as f:
    contents=f.read()
    ##print(contents)

# try:
#     number=int(input("Enter a number: "))
#     value=10//number
# except ZeroDivisionError:
#     print("Numbrer cannot be divided by zero")
# except ValueError:
#     print("Number cannot be zero")
# else:
#     print(value)
    
# finally:
#     print("Execution is done")


add=lambda x,y:x+y

print(add(5,3))


numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6]

eve_no=filter(lambda x:x%2==0,numbers)
print(list(eve_no))