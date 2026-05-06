# import coding_ex2

# def my_decorator(func):
#     def wrapper():
#         print("something is called before func")
#         func()
#         print("Something is called after func")
#     return wrapper

# @my_decorator

# def say_hello():
#     print("Hello")
# #say_hello()


# # Exception handling

# def exception_handling():
#     try: 
#         global number
#         number=0
#         number= int(input("Enter your number: "))
#         result=10//number
#     except ValueError:
#         print(f"Given numberr is not an integer{number}")
#     except ZeroDivisionError:
#         print((f"Number cannot be divisible by zero {number}"))
#     else:
#         print(f"here is ur answer: {result}")
#     finally:
#         print("Execution completed")

# #exception_handling()

# #exception_handling custom error

# class NegativeErrorException(Exception):
#     pass


# def check_age(n):
#     if n<0:
#         raise NegativeErrorException("Age is invalid")
#     else:
#         "Age is a valid number"

# try:
#     #check_age(-1)
#     pass
# except NegativeErrorException as e:
#     print(e)
    
# def count_upto_n(n):
#     count=0
#     while (count<=n):
#         yield count
#         count+=1
# coun=count_upto_n(6)
# for i in coun:
#     (i)

# new="pk"
# new2="rockz"

# (coding_ex2.query1((new),str(new2)))

# #print("hi bro {} other variable is {}".format(new,new2))


items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
dict1={}

for item in items:
    if item in dict1:
        dict1[item]+=1
    else:
        dict1[item]=1
#print(dict1)

import pandas as pd

dict1={"name":['Pavan','kalyan','Pavithra','Kushi'],
       "age":[20,30,60,26],
       "gender":['M','M','U','F']}


df=pd.DataFrame(dict1)

print(df[df["age"]>=30])

