from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Define a reference to the "rides" collection in Firestore
rides_ref = db.collection('rides')

# Endpoint to get all available rides
@app.route('/rides', methods=['GET'])
def get_rides():
    rides = []
    for ride in rides_ref.stream():
        rides.append(ride.to_dict())
    return jsonify(rides)

# Endpoint to create a new ride
@app.route('/rides', methods=['POST'])
def create_ride():
    data = request.get_json()
    new_ride = {
        "origin": data["origin"],
        "destination": data["destination"],
        "departure_time": data["departure_time"],
        "seats_available": data["seats_available"],
        "passengers": []
    }
    ride_ref = rides_ref.document()
    ride_ref.set(new_ride)
    new_ride['id'] = ride_ref.id
    return jsonify(new_ride)

# Endpoint to join a ride
@app.route('/rides/<string:ride_id>/join', methods=['POST'])
def join_ride(ride_id):
    ride_ref = rides_ref.document(ride_id)
    ride = ride_ref.get()
    if ride.exists and ride.to_dict()["seats_available"] > 0:
        ride_ref.update({
            "seats_available": ride.to_dict()["seats_available"] - 1,
            "passengers": firestore.ArrayUnion([request.remote_addr])
        })
        return jsonify(ride_ref.get().to_dict())
    else:
        return jsonify({"message": "Ride not found or no seats available."}), 404

if __name__ == '__main__':
    app.run()
