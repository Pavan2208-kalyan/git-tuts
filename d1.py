# import pandas as pd

# # data = {
# #     "id": [1, 2, 2, 3, 4, 5, None],
# #     "name": [" Alice ", "Bob", "Charlie", "Bob", None, "Eve", "Alice"],
# #     "age": ["25", "30", None, "30", "40", "35", "25"],
# #     "salary": [50000, None, 60000, 60000, "70000", None, 50000],
# #     "city": ["Hyderabad", "  Bangalore", "Chennai", "Chennai", "Hyderabad", None, "Hyderabad"]
# # }

# # df=pd.DataFrame(data)
# # print(df)

# # df.to_excel("Dump_data.xlsx",index=False)

# df=pd.read_excel(r'C:\Users\pavan\Downloads\data_cleaning_demo_with_specials.xlsx')
# print("before \n",df)


# # df['name']=df['name'].str.replace(r'[^a-zA-z0-9]',' ',regex=True).str.strip()
# # df['city']=df['city'].str.replace(r'[^a-zA-Z0-9]',' ',regex=True).str.strip()
# # #df['salary']=df['salary'].fillna(df['salary'].median())
# # df['salary']=df['salary'].fillna(df['salary'].median())
# # df['age']=df['age'].fillna(df['age'].mode()[0])
# # df['age']=df['age'].astype('int64')
# # df['salary']=df['salary'].fillna(df['salary'].mean())
# # df['salary']=df['salary'].astype('int64')
# # df['date_column']=pd.to_datetime(df['date_column'],errors='coerce',dayfirst=True,infer_datetime_format=True)
# # df['date_column']=df['date_column'].fillna('unkwon')
# # #df.rename(columns={'salary':'updated_salary'},inplace=True)
# # filter_df=df[df['salary']>60000]
# # #df.drop_duplicates()
# # df['id']=df['id'].fillna('0').astype('int64')
# # df.loc[6,'id']=9
# # print(df.loc[0])
# #print(df.iloc[3,2])
# #df['id']=df['id'].astype('int64')
# #print("\n",df)


# # df['name']=df['name'].str.strip()
# # print("df",df)
# # df['age']=df['age'].fillna(0).astype(int)
# # #print(df)
# # df['salary']=pd.to_numeric(df['salary'],errors='coerce')
# # df['salary']=df['salary'].fillna(0).astype(int)
# # df=df.drop_duplicates(inplace=True)
# # df=df.dropna(inplace=True)

# #df.drop_duplicates(inplace=True)



l1=['a','b','c']
l2=[1,2,3]

d1={x:y for x,y in zip(l1,l2)}
print(d1)