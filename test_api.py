import requests

# URL of your Flask API
BASE_URL = "http://127.0.0.1:5000/users"

# 1. Add a user (POST)
user_data = {"id": "1", "name": "Alice"}
response = requests.post(BASE_URL, json=user_data)
print("POST:", response.json())

# 2. Get all users (GET)
response = requests.get(BASE_URL)
print("GET:", response.json())

# 3. Update user (PUT)
update_data = {"name": "Alice Updated"}
response = requests.put(f"{BASE_URL}/1", json=update_data)
print("PUT:", response.json())

# 4. Delete user (DELETE)
response = requests.delete(f"{BASE_URL}/1")
print("DELETE:", response.json())
