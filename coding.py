def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    print(left,right)
    
    while left <= right:
        print("here",(left,right))
        mid = (left + right) // 2

        print("mid",mid,)
        print("mid_arr",arr[mid])

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1

            print("left",left)

        else:
            right = mid - 1
            print("right",right)
    
    return -1


def new_search(arr,target):
    left,right=0, len(arr)-1

    while left<=right:
        mid= (left + right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left= mid + 1

        else:
            right = mid -1
    return -1
        
            
def kay_rotations(arr,target):

    n=target%len(arr)
    print("original",arr)
    print(arr[:-n])


    #return arr[-n:] + arr[:-n]


# Example usage
# sorted_list = [1, 3, 5, 7, 9, 11, 15]
# target = 3
# print(kay_rotations(sorted_list, target))  # Output: 3



unsorted_list=[9,1,2,34,5,32,1]

n= len(unsorted_list)


for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if unsorted_list[j]<unsorted_list[min_index]:
            min_index=j
    unsorted_list[i],unsorted_list[min_index]=unsorted_list[min_index],unsorted_list[i]
#
# print(unsorted_list)

def characters_in(string):
    return sum (1 for char in string if char.lower() in 'aeiou')
#print(characters_in("Hello World"))

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged={**dict1,**dict2}
#print(merged)

def first_non_repeating_char(word):
    #word = word.split()
    print(word)
    char_count={}

    for char in word:
        char_count[char]= char_count.get(char,0)+1

    max_word=max(char_count,key=char_count.get)
    return(max_word)

    
#print(first_non_repeating_char("Pavan has a job and Pavan has aadhar and pavan has pan"))  # n


def flatten(list1):
    flat_list=[]

    for item in list1:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


#print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]

def max_subarray_sum(arr):

    current_sum=max_sum=arr[0]

    for num in arr[1:]:
        current_sum= max(num, current_sum + num)
        max_sum = max(max_sum,current_sum)
    return max_sum




print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6


    




    




