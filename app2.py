# def find_duplicates(input_list):

#     seen=set()
#     duplicates=set()
    
#     for item in input_list:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return list(duplicates)

# print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))  # Output: [1, 2]

from flask import Flask, jsonify,request

app=Flask(__name__)

data_store={}

#Post Item

@app.route("/items",methods=['POST'])

def post_item():

    data=request.get_json()

    if not data or "id" not in data or "name" not in data:
        return jsonify({"error":"Item not found"}),400
    
    item=data['id']

    if item in data_store:
        return jsonify({"error":"Item already present"}),400
    
    data_store[item] ={"name":data["name"]}
    return jsonify({"message":"Item added successfully"}),201

# Get Item

@app.route("/items",methods=['GET'])

def get_item():
    return jsonify(data_store),200

# PUT Item


@app.route("/items/<int:item_id>",methods=['PUT'])


def update_item(item_id):
    data=request.get_json()

    if  item_id not in data_store:
        return jsonify ({"error":"Item not found"}),404
    
    if  'name' not in data:
        return jsonify ({"error":"Invalid input"}),400
    
    data_store[item_id]['name']=data['name']
    return jsonify ({"message":"Item updated successfully"}),200
    
# Delete an item
@app.route("/items/<int:item_id>",methods=['DELETE'])

def delete_item(item_id):

    if item_id not in data_store:
        return jsonify ({"error":"Item not found"}),404
    
    del data_store[item_id]
    return jsonify ({"message":"Item successfully deleted"}),200





if __name__ =="__main__":
    app.run(debug=True)