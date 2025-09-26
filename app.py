from flask import Flask, request, jsonify

#creating flask app instance
app = Flask(__name__)

#dictionary for storing users
users = {}

@app.route("/users", methods = ['GET'])
def get_users():
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")
    
    if user_id in users:
        return jsonify({"error" : "User already exists"}), 400
    
    users[user_id] = {"id" : user_id, "name" : name}
    return jsonify({"message" : "User added", "user" : users[user_id]}), 200


@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user}), 200

if __name__ == "__main__":
    app.run(debug=True)

