import re
text = "Hello! This is test#123 with numbers 45.67 and symbols @$%."
numbers = "Hello! This is test#123 with numbers 45.67 and symbols @$%."

# new_text= re.findall(r'\b[a-zA-Z]+\b',text)
# print("gdg",new_text)

# number=re.findall(r'\b\d+\.?\d+\b',text)
# print(number)

# wite=re.findall(r'[^\w\s]',text)
# print(wite)

wite=re.findall(r'[^\w\s]',text)
print(wite)

text1 = "the emails are support@codecademy.com or help@codecademy.com"
new_res=re.findall(r'\S+@\S+',text1)
print(new_res)

movie_str = "the evening shows start at 7:00pm and 10:15pm"

new2=re.findall(r'([\d:,.]+)(am|pm)?',movie_str)
new2=re.findall(r'([\d:;.]+)(am|pm)?')
print(new2)


# new_text=re.findall(r'\b[a-zA-Z]+\b',text)
# print(new_text)

# new1=re.findall(r'\b\d+\.?\d+\b',text)

# new1=re.findall(r'\b\d+\.?\d+\b',text)
# print(new1)
# new2=re.findall(r'[^\w\s]',text)
# print(new2)
# text1 = "the emails are support@codecademy.com or help@codecademy.com"

# new3=re.findall(r'\S+@\S+',text1)
# print(new3)

# movie_str = "the evening shows start at 7:00pm and 10:15pm"
# matches =re.findall(r"([\d:,.]+)(am|pm)?",movie_str)
# #matches = re.findall(r"([\d:,.]+)(am|pm)?", movie_str)
# matches=re.findall(r'([\d:,.]+)(am|pm)?',movie_str)
# print(matches)


# import pandas as pd

# # Step 1: Read the CSV file
# df = pd.read_csv("students.csv")
# print(df.columns)

# df['date Of Birth']=pd.to_datetime(df['date Of Birth'],format='%d/%m/%Y')
# print(df)
# yu=df.loc[df['date Of Birth'].idxmax()]
# print("yu",yu)



# # df['date Of Birth']=pd.to_datetime(df['date Of Birth'],format='%d/%m/%Y')
# # print(df)
# # young_stu=df.loc[df['date Of Birth'].idxmax()]
# # print(young_stu)

# we=df[df['address']=='street1'].nlargest(1,'weight')
# print(we)

# new1=df.groupby('school')
# print("new1",new1.size())

# student_street=df[df['address']=='street1'].nlargest(1,'weight')
# print(student_street)

# # Step 2: Convert 'date Of Birth' to datetime format
# df['date Of Birth'] = pd.to_datetime(df['date Of Birth'], format="%d/%m/%Y")

# df['date of birth']=pd.to_datetime(df['date of birth'],format='%d%m%y')
# youngest_student=df.loc[df['date of birth'].idxmax()]


# # Step 3: Get the youngest student (latest date of birth)
# youngest_student = df.loc[df['date Of Birth'].idxmax()]

# # Step 4: Group by 'school'
# grouped_by_school = df.groupby('school')

# # Step 5: Student in 'street1' with the highest weight
# student_street1 = df[df['address'] == 'street1'].nlargest(1, 'weight')

# Print outputs
# print(" Youngest student:\n", youngest_student, "\n")
# print("Grouped by school:\n", grouped_by_school.size(), "\n")
# print("Heaviest student in street1:\n", student_street1)


# import json

# data = [
#     {
#         "_id": {"$oid": "5968dd23fc13ae04d9000001"},
#         "product name": "sildenafil citrate",
#         "supplier": "Wisozk Inc",
#         "quantity": 261,
#         "unit cost": "$10.47"
#     },
#     {
#         "_id": {"$oid": "5968dd23fc13ae04d9000002"},
#         "product name": "Mountain Juniperus ashei",
#         "supplier": "Keebler-Hilpert",
#         "quantity": 292,
#         "unit cost": "$8.74"
#     },
#     {
#         "_id": {"$oid": "5968dd23fc13ae04d9000003"},
#         "product name": "Dextromathorphan HBr",
#         "supplier": "Schmitt-Weissnat",
#         "quantity": 211,
#         "unit cost": "$20.53"
#     }
# ]


# max_qantity=max(data,key=lambda x:x['quantity'])
# #print("max",max_qantity['_id'])

# for item in data:
#     item['unit_float_cost']=float(item['unit cost'].replace('$',''))
# print(data)

# min_least_prod=min(data,key=lambda x:x['unit_float_cost'])
# print("min",min_least_prod['product name'])



# # 1. ID of product with highest quantity
# max_quantity_product = max(data, key=lambda x: x['quantity'])
# max_quantity_id = max_quantity_product['_id']['$oid']

# # 2. Product with minimum unit cost
# for item in data:
#     item['unit_cost_float'] = float(item['unit cost'].replace('$', ''))

# min_cost_product = min(data, key=lambda x: x['unit_cost_float'])
# min_cost_product_name = min_cost_product['product name']

# # Print answers
# print("ID of product with highest quantity:", max_quantity_id)
# print("Product name with minimum unit cost:", min_cost_product_name)
