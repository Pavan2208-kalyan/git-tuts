
# from flask import Flask

# # Step 1: Create a Flask app instance
# app = Flask(__name__)

# # Step 2: Define a route and its corresponding view function
# @app.route('/')
# def home():
#     return "Welcome to the Flask App!"

# # Step 3: Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)


# POST of an item
from flask import Flask,jsonify,request

app=Flask(__name__)

data_store={}

#get 
@app.route('/items',methods=['GET'])

def get_items():
    return jsonify(data_store), 200

# POST
@app.route('/items',methods=['POST'])

def create_item():
    data = request.get_json()

    if "id" not in data or "name" not in data:
        return jsonify({"error":"Invalid input"}),400
    if data['id'] in data_store:
        return jsonify({"error":"Item already present"}),400
    data_store[data['id']]={'name':data['name']}
    return jsonify({'message':'item is created'}), 201

# @app.route('/items/<int:item_id>', methods=['PUT'])
# def update_item(item_id):
#     data = request.get_json()
#     if 'name' not in data:
#         return jsonify({"error": "Invalid input"}), 400
#     if item_id not in data_store:
#         return jsonify({"error": "Item not found"}), 404
#     data_store[item_id]['name'] = data['name']
#     return jsonify({"message": "Item updated"}), 200


# Update
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    data=request.get_json()
    print(data)
    if  'name' not in data:
        return jsonify({'error':"invalid input"}), 400
    if item_id not in data_store:
        return jsonify({'error',"item id not found"}), 404
    data_store[item_id]['name']=data['name']
    return jsonify({'message':"Item updated"}), 200

#DELETE

@app.route('/items/<int:item_id>',methods=['DELETE'])

def delete_item(item_id):

    if item_id not in data_store:
        return jsonify({"error":"Item not found"}),404
    del data_store[item_id]
    return jsonify({'message':"Item has been deleted"}),200


if __name__=='__main__':
    app.run(debug=True)


import requests
url = 'http://127.0.0.1:5000/items'
headers = {'Content-Type': 'application/json'}
data = {'name': 'newName'}
response = requests.put(url, json=data, headers=headers)
print(response.status_code, response.json())