from flask import Flask, request, jsonify
from flask_cors import CORS
import random  # For simulating mechanic response

app = Flask(__name__)
CORS(app)  # Allow requests from all domains (for testing purposes)

# Sample data for fuel efficiency (can be improved based on AI model)
fuel_efficiency = {
    "Car": 15,  # 15 km per liter for a car
    "Truck": 8  # 8 km per liter for a truck
}

# Sample users (for login)
users = {
    "user1": {"password": "password123", "logged_in": False},
    "user2": {"password": "password456", "logged_in": False}
}

# Sample mechanics (for mechanic requests)
mechanics = [
    {"id": 1, "name": "John Doe", "service": "Tire Change", "distance": 5},
    {"id": 2, "name": "Jane Smith", "service": "Oil Change", "distance": 10}
]

# Sample fuel requests
fuel_requests = []

# Sample mechanic requests
mechanic_requests = []

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username]["password"] == password:
        users[username]["logged_in"] = True
        return jsonify({"success": True, "message": "Login successful!"}), 200
    return jsonify({"success": False, "message": "Invalid username or password."}), 401

@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    username = data.get('username')
    
    if username in users and users[username]["logged_in"]:
        users[username]["logged_in"] = False
        return jsonify({"success": True, "message": "Logout successful!"}), 200
    return jsonify({"success": False, "message": "User not logged in."}), 400

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username not in users:
        users[username] = {"password": password, "logged_in": False}
        return jsonify({"success": True, "message": "Signup successful!"}), 201
    return jsonify({"success": False, "message": "Username already exists."}), 400

@app.route('/predict_fuel', methods=['POST'])
def predict_fuel():
    data = request.get_json()
    vehicle_type = data.get('vehicle_type')
    current_fuel_level = data.get('current_fuel_level')
    desired_distance = data.get('desired_distance')

    efficiency = fuel_efficiency.get(vehicle_type, 10)  # Default efficiency if vehicle type is unknown
    expected_distance = current_fuel_level * efficiency

    if expected_distance >= desired_distance:
        return jsonify({"success": True, "message": "You have enough fuel for your journey!", "expected_distance": expected_distance}), 200
    return jsonify({"success": False, "message": f"You don't have enough fuel. You can travel up to {expected_distance} km.", "expected_distance": expected_distance}), 400

@app.route('/fuel_request', methods=['POST'])
def fuel_request():
    data = request.get_json()
    # Handle the fuel request submission here (e.g., store in a database or list)
    fuel_requests.append(data)
    return jsonify({"success": True, "message": "Fuel request submitted!"}), 200

@app.route('/mechanic_request', methods=['POST'])
def mechanic_request():
    data = request.get_json()
    # Randomly assign a mechanic for the request
    selected_mechanic = random.choice(mechanics)
    mechanic_requests.append(data)
    return jsonify({
        "success": True,
        "message": "Mechanic request submitted!",
        "mechanic": selected_mechanic
    }), 200

@app.route('/view_requests', methods=['GET'])
def view_requests():
    return jsonify({
        "fuel_requests": fuel_requests,
        "mechanic_requests": mechanic_requests
    })

if __name__ == "__main__":
    app.run(debug=True)
