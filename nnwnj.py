# declaring a dictionary 
import pandas as pd
d1= {}

my_set = {1, 2, 3}
#print("my_set",my_set)

dict1={"Employee_id":[100,200,300,400],
       "Names":['Pavan',"Pavi","Kumar","Pooja"],
       "Age":[18,30,23,21]}

df1=pd.DataFrame(dict1)

df1.to_excel("Employee.xlsx",index=False)
print("Print Excel generated successfully!")
#print(df1)
#print(list(dict1.values()))
#['Pavan','pava','sriny',kala]

# print value of a key
#print(dict1["name3"])





