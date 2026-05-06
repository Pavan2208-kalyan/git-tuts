# import multiprocessing

query1= """hi bro {0} other variable is {1}"""

# def cube(n):
#     print(" Cube of a number is {}".format(n**3))

# def square(n):
#     print("Square of a number is {}".format(n**2))

# # if "__name__"=="__main__":
# #     p1=multiprocessing.Process(target=cube,args=(10,))
# #     p2=multiprocessing.Process(target=square,args=(10,))

# #     p1.start()
# #     p2.start()

# #     p1.join()
# #     p2.join()

# # print("Both processes are done")


# from threading import Thread
# from threading import Lock
# import time

# num=0
# num_lock=Lock()

# def count(n):
#     global num
#     for _ in range(n):
#         with num_lock:
#             num+=1

# thread_count=100

# p1=Thread(target=count,args=(thread_count,))
# p2=Thread(target=count,args=(thread_count,))

# start_time=time.time()

# p1.start()
# p2.start()

# p1.join()

# p2.join()

# end_time=time.time()

# print("Execution time ",end_time-start_time)

# Without generator

def fibonacci_series(n):

    if n<0:
        raise ValueError("Number cannot be negative")
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    
    for i in range(2,n+1):
        a,b=b,a+b

    return b
#print(fibonacci_series(10))

# Using Generator

# def fibonacci_series():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# f1=fibonacci_series()
# print(next(f1))


# Sorting of an array with and without functions

# without sort function using selection sort

list1=[28,1,31,45,67,9,5]
n=len(list1)
for i in range(n):
    for j in range(i+1,n):
        print("i",i,"j",j)
        print("bf ",list1[i],list1[j])
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
        print("af",list1)

#print(list1)

# Is Palindrome or not
# apprch 1
str1='ROTOM'

# if str1==str1[::-1]:
#     print("The give string is a palindrome")
# else:
#     print("Not a palindrome")

#print("The give string is a palindrome" if str1==str1[::-1] else "Not a palindrome" )

#apprch 2

n=len(str1)
x=0
for i in range (n):
    if str1[i]!=str1[n-i-1]:
        x=1
        break
#print("The give string is a palindrome" if x==0 else "Not a palindrome" )

def decorator_func(func):
    def wrapper_func():
        print("Wrapper func worked")
        return func()
    print("decorator func worked")
    return wrapper_func

# @decorator_func

# def show():
#     print("Show wroked")
# show()


def count_upto_n(n):
    count=0
    while count<=n:
        yield count
        count +=1
counter=count_upto_n(6)

# for i in counter:
#     print(i)


list1=iter(['n','b','p'])
#print(next(list1))


# dict11={361:"Apple",201:"JAM",252:"Butter"}

# d=sorted(dict11.keys())
# print(d)

# d2={}

# for i in d:
#     d2[i]=dict11[i]
# print(d2)

"Write a program to find all pairs of elements in a list that add up to a given sum (k)."

list1=[8,2,3,7,5,1]

n=len(list1)
k=10

for i in range(n):
    for j in range(i+1,n):
        if (list1[i]+list1[j]==k):
            (list1[i],list1[j])

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

# def fibo(n):
#     if n == 0:  # Base case for fibo(0)
#         return 0
#     elif n == 1:  # Base case for fibo(1)
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# nterms=int(input("Enter a positive integer: "))

# if nterms<0:
#     print("Please enter a positive integer")

# else:
#     for i in range(nterms):
#         print(fibo(i))


# str1="the sky is blue"

# l=str1.split()
# print(l)
# l=l[::-1]
# print(l)
# l=' '.join(l)
# print(l)

# Max repeated character complexity should br o(n)

str1='yudidoioooppp'

chr={}

for i in str1:
    if i in chr:
        chr[i] +=1
    else:
        chr[i] =1
max_char=max(chr,key=chr.get)
#print(max_char,chr[max_char])

lis1=[10,8,1,3,55,6,77,8]

min=lis1[0]
max=lis1[0]

for i in lis1:
    if i>max:
        max=i
    if i<min:
        min=1

#print(min,max)

def isprime(n):

    if n<2:
        return False
    for i in range(2,int(n**0.5+1)):
        if n %i==0:
            return False
    return True

#print(isprime(9))

def factorial(n):
    pass
    # if n==0 or n==1:
    #     return 1

    # return n * factorial(n-1)

    
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
#print(fruit_list1)
fruit_list2 = fruit_list1
##print(fruit_list1)
fruit_list3 = fruit_list1[:]
#print(fruit_list1)
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
##print(fruit_list1)
sum = 0
# print(fruit_list1)
# print(fruit_list2)
# print(fruit_list3)

# for ls in (fruit_list1, fruit_list2, fruit_list3):
# 	if ls[0] == 'Guava':
# 		sum += 1
# 	if ls[1] == 'Kiwi':
# 		sum += 20


# print (sum)

a = [1,2,3]
print(a)