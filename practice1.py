from flask import Flask, jsonify,request

app=Flask(__name__)

#Posting the data
data_store={}
@app.route('/items',methods=['POST'])

def create_item():
    data=request.get_json()

    if not data or 'name' not in data or 'id' not in data:
        return jsonify({"error":"Invalid input"}),400
    item=data['id']

    if item in data_store:
        return jsonify({"error":"item already exixts"}),400
    
    data_store[item]={"name":data['name']}
    return jsonify({"message":"item created successfully"}),201

# updating an existing item

@app.route('/items/<int:item_id>',methods=['PUT'])

def update_item(item_id):
    data=request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error":"invalid input"}),400
    
    if item_id not in data_store:
        return jsonify({"error":"item does not exist"}),404
    
    data_store[item_id]['name']=data['name']
    return jsonify({"message":"item updated successfully"}),200

# to retrive an object 
@app.route('/items',methods=['GET'])

def retrive():
    return jsonify(data_store),200

@app.route('/items/<int:item_id>',methods=['DELETE'])


def delete_item(item_id):

    if item_id not in data_store:
        return jsonify({"error":"item not found"}),404
    del data_store[item_id]
    return jsonify({"message":"item deleted successfully"}),200


if __name__=="__main__":
    app.run(debug=True)

