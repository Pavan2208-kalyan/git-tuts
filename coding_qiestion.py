# Reverse of a string without using string function

def rev_string(val):
    result=""
    for char in val:
        result=char+ result
    return result
#print(rev_string("python"))

# Delete all consonants in the word "Python and Data Science"

def del_consonants(val):

    check_string="aeiouAEIOU"
    res=''.join([char for char in val if not char.isalpha()  or  char in check_string])
    return res

#print(del_consonants("Python and Data Science 22 08"))

"Program to find sum of all prime numbers in between 1 to n"


def sum_prime_numbers(val):
        for j in range (2,val):
            if (val%j==0):
                return False
        return True
def add_num(val2):
    sum=0

    for j in range (2,val2):
       # print(j,val2)
        b=sum_prime_numbers(j)
       # print(j,b)

        if (b)==True:
            sum=sum + j
    return sum
#print(add_num(10))

####
# Leap year

def leap_year(year):

    if(year%400==0) and (year%100==0):
        return "Year is a leap year"
    if(year%4==0) and (year%100!=0):
        return "Year is a leap year"
    
    else:
        return"not a leap year"
    
#print(leap_year(int(input("Enter your year "))))
# Approach 1
def arm_strong_number(number):
    sum=0
    for i in range(len(number)):
        sum=int(number[i])**len(number)+sum
    return "arm strong number" if str(sum) == number else "not an arm strong number"
#print(arm_strong_number(str(input("Enter your arm strong number: "))))

#Appraoch 2
def arm_strong_number(number):
    number = str(number)
    length =len(number)
    total = sum(int(digit)**length for digit in number)
    return "arm strong number" if str(total) == number else "not an arm strong number"
#print(arm_strong_number((input("Enter your arm strong number: "))))

# Swap of a varibles

def swap_variable():
    x=10
    y=11
    x,y=y,x
    print(x,y)
#swap_variable()

# prime number

def is_prime_number(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        print(int(num**0.5)+1)
        print(i,"jj",num)
        if num%i==0:
            return False
    return True
#print(is_prime_number(26))

# factorial of number

# using recursion

def factorial_num(n):
    if n<0:
        return "factorial of a number is not possible for negative num"
    if(n==0) or (n==1):
        return 1
    else:
        return n * factorial_num(n-1)
#print(factorial_num(5))

# without using recursion
def factorial_num(n):
    if n<0:
        return "factorial of a number is not possible for negative num"
    if(n==0) or (n==1):
        return 1
    result=1
    for i in range (1,n+1):
        #print("i",i)
        result*=i
       # print("result",result)
    return result
#print(factorial_num(5))

# Fibonacci series

def fibonacci_series(n):
    if n<0:
        return False
    if n==1:
        return 1
    a,b=0,1
    for i in range (2,n+1):
       """ logic 1"""
       a,b=b,a+b
       """logic 2"""
        # c=a+b
        # a,b=b,c
       
    return b
#print(fibonacci_series(10))

# lambda functions
#Sample 1
number=[1,2,3,4]
new_list=list(map(lambda x: x**2,number))
#print(new_list)

#new_list=list(map(lambda x:x**2,number))
# Sample 2
add=lambda x,y:x+y
#print(add(3,4))
# Sample 3

division= lambda x,y:x//y
#print(division(10,2))


