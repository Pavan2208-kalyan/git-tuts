
def arm_strong_number(i):
    number=str(i)
    length=len(number)
    total= sum( int(digit)**length  for digit in number )==i
    return total
    
# arms_strong_no=[i for i in range(1,1001) if arm_strong_number(i)]
# print(arms_strong_no)

def weightstring(str1):
    str1=str1.lower()
    str_weight= sum (ord(char)- ord('a') +1 for char in str1 if char.isalpha())
    return str_weight
# print(weightstring("Apple"))  # Output: 50
# print(weightstring("hello"))  # Output: 52
# print(weightstring("Python")) # Output: 98

def prime_factors(n):
    if n<1:
        return []
    
    factors=[]

    while n%2==0:
         factors.append(2)
         n//=2
    
    for i in range(3,int(n**0.5)+1,2):
         if n%i==0:
              factors.append(i)
              n//=i
    
    if n>2:
         factors.append(n)


    
    return factors

# print(prime_factors(6))   # Output: [2, 3]
# print(prime_factors(24))  # Output: [2, 2, 2, 3]
# print(prime_factors(1))   # Output: []
# print(prime_factors(-10)) # Output: []
# print(prime_factors(17))  # Output: [17]


def char_with_s(sentence):

    char_list=[ char for char in sentence if char.lower().startswith('s')]
    return char_list

def unique_char(word):

    return len(set(word))==len(word)



sentence=['apple','sample','search','cat']

# for word in sentence:
#     print(unique_char(word))
# print(char_with_s(sentence))

def longest_char(str1):

    max_char=str1[0]
    max_length=1
    max_index=0

    current_length=1
    current_index=0
    current_char=str1[0]

    for i in range (1,len(str1)):

        if str1[i]==current_char:
            current_length+=1
        else:
            if current_length>max_length:
                max_char=current_char
                max_length=current_length
                max_index=current_index
        
            current_char=str1[i]
            current_index=i
            current_length=1

    if current_length>max_length:
                max_char=current_char
                max_length=current_length
                max_index=current_index

    return f"Longest occurring character is '{max_char}' with length {max_length} at index {max_index}."
str1='aabbbbbcc'
#print(longest_char(str1))


def find_partitions(n, result=[],start=1):
     if n==0:
          print(" + ".join(map(str,result)))
          
          
     for i in range(start,n+1):
          find_partitions(n-i,result + [i],i)

# Example usage:
num = 3
#find_partitions(num)

def fibonacci_series(n):
     if n<0:
          return None
     if n==1:
          return 1
     a,b=0,1

     for i in range(2,n+1):
          a,b=b,a+b
     return b

#print(fibonacci_series(10))

def min_elements_for_target(arr,target):
     
    arr.sort(reverse=True)

    total=0
    count=0

    for num in arr:
        if total+num<=target:
               total+=num
               count+=1
        if total==target:
             return count
    return -1

    
          


# arr = [1, 2, 3, 4]
# target = 6
# print(min_elements_for_target(arr, target))  # Output: 2 (2 + 4)

# target = 12
# print(min_elements_for_target(arr, target))  # Output: -1 (Target out of scope)


def kay_rotations(sorted_list,target):
     
    n= target%len(sorted_list)
    return sorted_list[n:] + sorted_list[:n]

sorted_list = [1, 3, 5, 7, 9, 11, 15]
target = 3
print(kay_rotations(sorted_list, target))



