from flask import Flask,jsonify,request

app=Flask(__name__)
print(app)

data_store={}


# For posting an item
@app.route('/items',methods=['POST'])

def create_items():
    data=request.get_json()

    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error":"invalid input"}),400
    
    item=data['id']
    
    if item in data_store:
        return jsonify({"error":"Item already exists"}),400
    
    data_store[item]={"name":data['name']}
    return jsonify({"message":"Item successfully created"}),201


# # For updating an item PUT Method

@app.route('/items/<int:item_id>',methods=['PUT'])

def update_item(item_id):

    data=request.get_json()

    if not data or 'name' not in data:
        return jsonify({'error':" Invalid input"}),400
    
    if item_id not in data_store:
        return jsonify({"message":"Item not found"}),404
    
    data_store[item_id]['name']=data['name']

    return jsonify({'message':'Item updated'}),200

# get

@app.route('/items',methods=['GET'])

def retrieve_data():
    return jsonify(data_store),200

# delete 

@app.route('/items/<int:item_id>',methods=['DELETE'])

def delete_item(item_id):

    if item_id not in data_store:
        return jsonify({"error":"Item not found"}),404
    
    del data_store[item_id]
    return jsonify({"message":"Item successfully deleted"}),200
    


if __name__=='__main__':
    app.run(debug=True)
    

