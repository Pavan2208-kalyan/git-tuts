from flask import request,jsonify,Flask

app=Flask(__name__)

data_store={}

# create an item

@app.route("/items",methods=['POST'])

def create_item():
    data=request.get_json()

    if not data or "id" not in data or "name" not in data:
        return jsonify({"error":"Invalid Request"}),400
    
    item=data['id']
    if item in data_store:
        return jsonify({"message":"Item already exists"}),404
    
    data_store[item]={"name":data['name']}
    return jsonify({"message":"Iteam  created successfully"}),201

@app.route('/items',methods=['GET'])

def get_item():
    return jsonify (data_store),200

@app.route("/items/<int:item_id>",methods=['PUT'])

def update_item(item_id):
    data= request.get_json()

    if not data or "name" not in data:
        return jsonify({"error":"Invalid Request"}),400
    
    if item_id not in data_store:
        return jsonify({"error":"item not found"}),404
    
    data_store[item_id]['name']=data['name']
    return jsonify({"message":"Item update successfully"}),200

@app.route("/items<int:item_id>",methods=['DELETE'])

def del_update(item_id):

    if item_id not in data_store:
        return jsonify({"error":"Item not found"}),404
    
    del data_store[item_id]

    return ({"message":"Item successfully deleted"}),200




if __name__=="__main__":
    app.run(debug=True)