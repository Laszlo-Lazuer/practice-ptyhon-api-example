# Flask application
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-user/<user_id>") #decorator
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user/", methods=["POST"]) #decorator - not using default get, need to specify accepted method
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201

"""
GET Request data
POST Create a resource
PUT Update a resource
DELETE Remove a resources
"""

if __name__ == "__main__":
    app.run(port=8000, debug=True) # Issue - Port 5000 returned a 403 on mac