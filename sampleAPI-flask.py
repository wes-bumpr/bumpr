from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a list of available rides
rides = [
    {
        "id": 1,
        "origin": "San Francisco",
        "destination": "San Jose",
        "departure_time": "2023-02-21 09:00:00",
        "seats_available": 2,
        "passengers": []
    },
    {
        "id": 2,
        "origin": "San Francisco",
        "destination": "Oakland",
        "departure_time": "2023-02-22 10:00:00",
        "seats_available": 1,
        "passengers": []
    }
]

# Endpoint to get all available rides
@app.route('/rides', methods=['GET'])
def get_rides():
    return jsonify(rides)

# Endpoint to create a new ride
@app.route('/rides', methods=['POST'])
def create_ride():
    data = request.get_json()
    new_ride = {
        "id": len(rides) + 1,
        "origin": data["origin"],
        "destination": data["destination"],
        "departure_time": data["departure_time"],
        "seats_available": data["seats_available"],
        "passengers": []
    }
    rides.append(new_ride)
    return jsonify(new_ride)

# Endpoint to join a ride
@app.route('/rides/<int:ride_id>/join', methods=['POST'])
def join_ride(ride_id):
    ride = next((r for r in rides if r["id"] == ride_id), None)
    if ride and ride["seats_available"] > 0:
        ride["seats_available"] -= 1
        ride["passengers"].append(request.remote_addr)
        return jsonify(ride)
    else:
        return jsonify({"message": "Ride not found or no seats available."}), 404

if __name__ == '__main__':
    app.run()
