# import multiprocessing

# def cube(n):
#     print(f'cube of a number is {n**3}')

# def square(n):
#     print(f' Square of a number is {n**2}')

# if __name__=="__main__":
#     p1=multiprocessing.Process(target=cube,args=(10,))
#     p2=multiprocessing.Process(target=square,args=(10,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# from threading import Thread, Lock

# import time

# num=0
# num_lock=Lock()


# def count(n):
#     global num
#     for _ in range(n):
#         with num_lock:
#             num+=1

# import_threading =100

# t1=Thread(target=count,args=(import_threading,))
# t2=Thread(target=count,args=(import_threading,))

# start_time=time.time()

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# end_time=time.time()

# print("final value of num",num)

# print("Execution time",end_time-start_time)

# def fibonacci_series(n):

#     if n<0:
#         raise ValueError("Number cannot be negative")

#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     a,b=0,1

#     for _ in range(2,n+1):
#         a,b=b,a+b

#     return b

# print(fibonacci_series(10))

# def fibonacci_series():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# f1=fibonacci_series()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))

list1=[90,32,41,2,3,109,161]
n= len(list1)

for i in range(n):
    for j in range(i+1,n):
        #print(list1[i],list1[j])
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
#print(list1)

# Given string is palindrom

# str1="ROTOM"

# x=0

# n=len(str1)

# for i in range(n):
#     if str1[i]!=str1[n-i-1]:
#         x=1
#         break

# print("palindrome" if x==0 else "Not a palindrome")


# def decorator_func(func):
#     def wrapper_func():
#         print("something has happened before the func")
#         func()
#         print("something has happened after the func")
#     return wrapper_func
# @decorator_func

# def say_hello():
#     print("Hello !!")

# say_hello()


# def decorator_func(func):
#     def wrapper_func(*args, **kwargs):
#         print("something has happened before the func")
#         result=func(*args, **kwargs)
#         print("something has happened after the func")
#         return result
#     return wrapper_func
# @decorator_func

# def say_hello(name):
#     print(f"Hello {name}")

# say_hello("pavan")



# generator

# def count_upto_n(n):
#     count=0
#     while count<n:
#         yield count
#         count +=1

# count1=count_upto_n(5)

# for count in count1:
#     print(count)


# dict11={361:"Apple",201:"JAM",252:"Butter"}
# d2= {key:dict11[key] for key in sorted(dict11)}
# print(d2)

"Write a program to find all pairs of elements in a list that add up to a given sum (k)."
list1=[8,2,3,7,5,1]

n=len(list1)

k=9

for i in range(n):
    for j in range(i+1,n):
        if (list1[i]+list1[j]==k):
            #print(list1[i],list1[j])
            pass
str1=[10,8,3,55,6,77,8]
chr={}
for i in str1:
    if i in chr:
        chr[i] +=1
    else:
        chr[i] = 1
print(chr)
max_char=max(chr,key=chr.get)


str1='yudidoioooppp'

#print("max_char",max_char)


lis1=[10,8,3,55,6,77,8]

min=lis1[0]
max=lis1[0]

for i in lis1:
    if i>max:
        max=i
    if i<min:
        min=i


#print(min,max)

def isprime(n):

    if n<2:
        return False
    
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
#print(isprime(5))


# add_ten= lambda x,y:x+y

# print(add_ten(5,20))

# number=[1,2,3,4,5,6,7,8]
# items = [(1, 3), (2, 1), (4, 5)]

# squared=list(filter(lambda x:x%2==0,number))
# print(squared)

# items.sort(key=lambda x:x[1])
# print(items)


def get_letter_value(char):
    mapping = {
        1: 'AIJQY',
        2: 'BKR',
        3: 'CGLS',
        4: 'DMT',
        5: 'EHNX',
        6: 'UVW',
        7: 'OZ',
        8: 'FP'
    }
    
    for key, letters in mapping.items():
        if char in letters:
            return key
    return 0  # For spaces or unrecognized characters



# Example usage
input_str = "S. KANAPATHY"


get_letter_value(input_str)


import re

s = "S. KANAPATHY 123!"
cleaned = re.sub(r'[^A-Za-z]', '', s)
cleaned= re.sub(r'[A-Za-z]','',s)
print(cleaned)  # Output: SKANAPATHY