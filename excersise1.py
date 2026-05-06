# def get_letter_value(char):
#     mapping = {
#         1: 'AIJQY',
#         2: 'BKR',
#         3: 'CGLS',
#         4: 'DMT',
#         5: 'EHNX',
#         6: 'UVW',
#         7: 'OZ',
#         8: 'FP'
#     }
    
#     for key, letters in mapping.items():
#         if char in letters:
#             return key
#     return 0  # For spaces or unrecognized characters



# # Example usage
# input_str = "S. KANAPATHY"


# get_letter_value(input_str)


# import re

# s = "S. KANAPATHY 123!"
# cleaned= re.sub(r'[^A-Za-z]','',s)
# print(cleaned)  # Output: SKANAPATHY


l1= [23,4,5,78,9,8]
print(max(l1))

t1=(1,2,3)
t2=(4,)

t3=(t1)+(t2)

print(t3)


def palindrome(str1):
    x=0
    n=len(str1)

    for i in range(n):
        if str1[i]!=str1[n-i-1]:
            x=1
        
    return "palin" if  x== 0 else "Not a Palin"

print("Result", palindrome("12321"))