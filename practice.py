class MathUtills:
    @staticmethod
    def add(x,y):
        return x + y

new1=MathUtills()
#print(new1.add(5,3))

#print(MathUtills.add(5,4))

# class employee:
    
#     cmp_nm="OPENAI"
    
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def change_company_name(cls,new_name):
#         cls.cmp_nm=new_name

# emp1=employee('Bob')
# emp2=employee('Alice')
# emp1.change_company_name('GOOGLE')

# print(emp1.cmp_nm)
# print(emp2.cmp_nm)

def square(n):
    for i in range(1,n+1):
        yield i*i
gen=square(4)
# print(next(gen))
# print(next(gen))
# print(next(gen))



#print(square(6))

with open("sample_file.txt",'w') as f:
    f.write("Add some lines")
    f.close()

with open("sample_file.txt",'r') as f:
    lines= f.read()
    print(lines)