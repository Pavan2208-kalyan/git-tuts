# from flask import Flask,request,jsonify

# app=Flask(__name__)

# data_store={}

# @app.route('/items',methods=['POST'])


# def create_item():
#     data=request.get_json()

#     if not data or 'name' not in data or 'id' not in data:
#         return jsonify({"error":"Invalid Input"}),400
    
#     item_id=data['id']

#     if item_id in data_store:
#         return jsonify({'error':"Item already exist"}),400
    
#     data_store[item_id]={'name':data['name']}
#     return jsonify({"message":"Item created successfully"}),201

# @app.route('/items',methods=['GET'])

# def retrieve_json():
#     return jsonify(data_store),200


# @app.route('/items/<int:item_id>',methods=['PUT'])

# def update_item(item_id):
#     data=request.get_json()
#     if not data or 'name' not in data :
#         return jsonify({"error":"Invalid Input"}),400
#     if item_id not in data_store:
#         return jsonify({"error":"Item not found"}),404

    
#     data_store[item_id]['name']=data['name']
#     return jsonify({"message":"Item updated successfully"}),200

# @app.route('/items/<int:item_id>',methods=['DELETE'])

# def delete_item(item_id):
#     if item_id not in data_store:
#         return jsonify({"error":"Item not found"}),404
#     del data_store[item_id]

#     return jsonify({"message":"item deleted successfully"}),200


# if __name__=="__main__":
#     app.run(debug=True)



## Original


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Dummy secret token
# SECRET_TOKEN = "my_secret_token"

# @app.route('/public')
# def public_api():
#     return {"message": "✅ This is a public API!"}

# @app.route('/private')
# def private_api():
#     # Get token from the header
#     token = request.headers.get("Authorization")
    
#     if token != f"Bearer {SECRET_TOKEN}":
#         return jsonify({"error": "❌ Unauthorized access!"}), 401
    
#     return {"message": "🔐 This is a private API with token authentication!"}

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask,jsonify,request

# app=Flask(__name__)

# my_secret_token="my_secret_code"

# @app.route('/public')

# def public_api():
#     return {'message':"This is a public api"}


# @app.route('/private')

# def private_api():
#     token=request.headers.get('Authorization')

#     if token!=f"Bearer {my_secret_token}":
#         return jsonify({"error":"You are not authourized"}),401
    
#     return {"message":"Welcome this is private api"}


# if __name__=="__main__":
#     app.run(debug=True)