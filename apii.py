import requests

base_url = 'http://127.0.0.1:5000/items'


# create item
data={'id':1,'name':"Dj Allu arjun"}

create_response=requests.post(base_url,json=data)
print(create_response.status_code)
print("\n",create_response.json())

# 1. Create item
# create_data = {"id": 1, "name": "Pavan"}
# create_response = requests.post(base_url, json=create_data)
# print("\nCreate Response:", create_response.json())
# 
#retrieve
get_response=requests.get(base_url)
print(get_response.status_code)
print(get_response.json())

# 2. Retrieve all items
# get_response = requests.get(base_url)
# print("\nGet All Items:", get_response.json())

# 3. Update the item

name_update={'name':'Bunny'}

update_response=requests.put(f"{base_url}/1",json=name_update)
print(update_response.status_code)
print(update_response.json())


upd_item=requests.get(base_url)
print(upd_item.status_code)
print(upd_item.json())

# update_data = {"name": "Pavan Updated"}
# update_response = requess.put(f"{base_url}/1", json=update_data)
# print("\nUpdate Response:", update_response.json())

# 4. Delete the item

delete_res=requests.delete(f"{base_url}/1")
print(delete_res.status_code)
print(delete_res.json())

# delete_response = requests.delete(f"{base_url}/1")
# print("\nDelete Response:", delete_response.json())

