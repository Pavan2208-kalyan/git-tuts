# import os
# import re

# directory="my_directory"
# file_path=os.path.join(directory,"my_file.txt")

# os.makedirs(directory,exist_ok=True)

# with open(file_path,'w') as f:
#     f.write("Hello I am viraj,\n viraj has a pan card\n Hello I am viraj")

# print(f"My directory created {directory} and file path is {file_path}")


# def count_occuences(word,file_path):
#     count=0

#     with open(file_path,'r',encoding='utf-8') as f:
#             text= f.read().lower()
#             #count= len(re.findall(rf"\b{re.escape(word.lower())}\b",text))

#            # count= len(re.findall(rf"\b{re.escape(word.lower())}\b",text))
#             count=len(re.findall(rf"\b {re.escape(word.lower())}\b",text))
          
#     return count,word

# word="Viraj"

# #print(count_occuences(word,file_path))

# def reverse_string(word):
#     char=""



#     char= word[::-1]
    
#     return char

# #print(reverse_string("VINAY"))


# my_directory="Practice_folder"

# file_path_new=os.path.join(my_directory,'new_file.txt')

# os.makedirs(my_directory,exist_ok=True)

# with open(file_path_new,'w') as n:
#      n.write("Hello I am Fruit\nIam a apple\nIam a mango\nIam a apple")

# from collections import Counter

# def new_counter(file_path_new):
#     duplicates=[]
#     with open (file_path_new, 'r',encoding='utf-8') as f:
#           lines=[line.strip() for line in f]
#           print(lines)

#           line_count=Counter(lines)
#           print(line_count)
#           duplicates= [ line for line, count in line_count.items() if count>1]
#     print(duplicates)
          
          
     

# new_counter(file_path_new)

def smallest_positive(numbers):

    lst= [num for num in numbers if num>0]
    return min(lst) if lst else None
numbers = [-3, -1, 0, -2, -5, -7, -1]
#print(smallest_positive(numbers))


class structure:

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def ani_name(self):
        return (f"Animal name is {self.name} and breed is {self.breed}")

class dog(structure):
    def __init__(self, name, breed,colour):
        self.colour=colour
        structure.__init__(self,name,breed)
    
    def dog_colour(self):
        return f" dog colour is {self.colour}"
    
        
# dg=dog("Hikkaa","Pomerian","white")

# print(dg.dog_colour())


num =10

def num_val():
    global num 
    num+=5

    print(num)

#num_val()

class static_varible:
    new_name="karan"

    def __init__(self,age,phone):
        self.age=age
        self.phone=phone
    
    def new_regime(self):
        return f" age is {self.age} and phone no is {self.phone}"

cg=static_varible("24","900000")

#print(cg.new_name)


# square= lambda x: x**2

# print(square(5))

# add= lambda a,b: a+b
# print(add(7,5))


from itertools import combinations

def min_elements_for_target(arr, target):
    arr.sort(reverse=True)  # Sorting in descending order for optimization
    
    for i in range(1, len(arr) + 1):  # Check all possible subset sizes
        for subset in combinations(arr, i):
            if sum(subset) == target:
                return i  # Return the minimum elements required
    
    return -1  # If no subset sums to the target

# Example usage
arr = [1, 2, 3, 4]
# print(min_elements_for_target(arr, 6))   # Output: 2 (e.g., 2+4 or 3+3)
# print(min_elements_for_target(arr, 12))  # Output: -1 (Not possible)


from itertools import combinations

def min_elements(arr,target):
    arr.sort(reverse=True)
    #print(arr)

    for i in range(1, len(arr)+1):
        for subset in combinations(arr,i):
            if sum(subset)==target:
                return i
    return -1

arr = [1, 2, 3, 4]
target=6

#print(min_elements(arr, target))

from collections import Counter
def second_element_count(str1):
    char_count=Counter(str1.lower())
    char_list=[char for char,count in char_count.items() if count==1]
    return char_list[1] if len(char_list)>1 else None
str1="Swiss"
#print(second_element_count(str1))

## smallest second element
# approach 1
# def second_smallest_element(arr1):
#     return list(set(sorted(arr1)))[1]


# approach 2

def second_smallest_element(arr1):

    if len(arr1)<2:
        return None
    
    sec_small=float('inf')
    smallest=float('inf')
    
    for num in arr1:
        if num<smallest:
            sec_small=smallest
            smallest=num

        elif smallest<num<sec_small:
            sec_small=num
        
    return sec_small if sec_small!=float('inf') else None

arr1 = [5, 1, 2, 9, 7, 2]
#print(second_smallest_element(arr1))


def run_length_of_string(s):

    if not s:
        return ''
    
    encoded=[]
    count=1
    
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1

        else:
            encoded.append(s[i-1] +str(count))
            count=1
    encoded.append(s[-1] +str(count))

    return ''.join(encoded)

s = "aaabbcddd"
#print(run_length_of_string(s))  # Output: "a3b2c1d3"

from collections import Counter

def char_frequency(s,char):

    char_count=Counter(s)

    return char_count.get(char,0)


s = "bananab"
char = "a"
#print(char_frequency(s, char))  # Output: 3


# The given string is anagram or not

def is_anagram(s1,s2):

    return Counter(s1)==Counter(s2)


#print(is_anagram("listen", "silent"))  

def perfect_number(n):

    return sum ( i for i in range(1,n) if n%i==0 )==n
    
# perfect_no=[ n for n in range(1,101) if perfect_number(n) ] 
# print(perfect_no)

import string

def find_missing_letter(sentence):
    sentence=sentence.lower()
    
    alphabet_set=set(string.ascii_lowercase)

    missing_letter=alphabet_set-set(sentence)

    return ''.join(missing_letter)

def is_panagram(sentence):
    return find_missing_letter(sentence)==''

sentence = "The quick brown fox jumps over the lazy dog."
#sentence = "Hello world"

# if is_panagram(sentence):
#     print("panagram")

# else:
#     print("Not a panagram")
#     find_missing_letter(sentence)


def remove_duplicate_words(sentence):

    words=sentence.split()
    seen=set()
    unique_word=[]

    for word in words:
        if word not in seen:
            seen.add(word)
           # print(seen)
            unique_word.append(word)
           # print(unique_word)
    return' '.join(unique_word)  




# Example Usage
sentence1 = "Good day day bye bye"
sentence2 = "greet the day user greet good day"

print(remove_duplicate_words(sentence1))  # Output: "Good day bye"
print(remove_duplicate_words(sentence2))  # Output: "greet the day user good"



    
        


