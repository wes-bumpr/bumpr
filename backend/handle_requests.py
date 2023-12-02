# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
import random
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from get_request import db  # imports firebase admin and init app
from match import Match

app = Flask(__name__)
CORS(app, origins="*")  # Enable CORS for all routes

import testflask


@app.route("/")
def hello():
    print("new")
    testflask.test()
    # return "helloo"
    return render_template("template.html")


def input_Matches_ToFirebase(matchedDict):
    """
    Get the list of ride requests that were matched from score.py
    Put match into Firebase collection

    {match1: [riderequest1, riderequest2], ...}
    """
    for m in matchedDict:
        match = matchedDict[m]
        doc_ref = db.collection("matches").document(m)
        doc_ref.set(match)

def get_match(match_dict, request_id):
    '''
    Helper for input_RideRequest_ToFirebase().

    Given the current dict of all matches
    return the match for a given request id

    Return ex: {'users': ['testing1', 'testing1'], 'origin': 
                ['Wellesley, MA, USA', '231 Forest St, Babson Park, MA 02457, USA'],
                'to': ['231 Forest St, Babson Park, MA 02457, USA', '231 Forest St, Babson Park, 
                MA 02457, USA'], 'depart_time': '12/9/2023, 12:17:18 PM', 'request_ids': 
                ['testing176241', 'testing197388']}
    * if no match for the specified request id that was just inputted then returns None
    '''
    print("get_match: ", match_dict)
    print("get_match request id: ", request_id)
    for match in match_dict:
        print("get match match: ", match)
        if request_id in match_dict[match]["request_ids"]:
            print("match for request: ", match_dict[match])
            return match_dict[match]


#TODO: Currently tries to match inputted ride request with existing ride requests
# in order to display the match info if the inputted ride request has a match
# but also need to run the Match() for requests that weren't matched right away
# maybe need a timer that runs Match() every 8 hours or so
@app.route("/ride-request", methods=["POST"])
def input_RideRequest_ToFirebase():
    """
    @param rideRequestsList: list of ride requests (dictionary)
    Puts all ride request info into Firebase
    """

    ride_request_data = request.get_json()
    print("Received ride request data:")
    print(ride_request_data)

    if not isinstance(ride_request_data, dict):
        return jsonify({"error": "JSON ride request data must be a dictionary"})
    else:
        # Generate a random integer with 5 digits (between 10000 and 99999)
        random_integer = random.randrange(10000, 100000)
        request_doc_id = ride_request_data["user_ID"] + str(random_integer)
        doc_ref = db.collection("ride-requests-test").document(request_doc_id)
        doc_ref.set(ride_request_data) # data pushed into firebase

        # run match every time new ride request info is put into firebase
        match = Match()
        print("match dict: ", match.match_dict)
        input_Matches_ToFirebase(match.match_dict)

        # get the match for the specific request id 
        match_for_request = get_match(match.match_dict, request_doc_id)
        print("match for request: ", match_for_request)
        return jsonify(match_for_request)

        # Include match_dict in the response to send it back to the frontend
        # response_data = {
        #     "success": "Ride request data added to Firebase and matches created (if any)",
        #     "match_dict": match.match_dict
        # }

        # return jsonify(response_data)

#TODO: need to work on login and having user profiles
def input_User_ToFirebase(user):
    """
    @param request: singular user-- dictionary of info
    Put user into 'users' collection
    """
    # Generate a random integer with 5 digits (between 10000 and 99999)
    random_integer = random.randrange(10000, 100000)
    request_doc_id = user["user_ID"] + str(random_integer)
    doc_ref = db.collection("ride-requests").document(request_doc_id)
    doc_ref.set(user)


def delete_Item_FromFirebase(collection, doc_id):
    """
    Remove ride requests from Firebase ride-request collection
    """
    doc_ref = db.collection(collection).document(doc_id)
    doc_ref.delete()
    return doc_id


def archive_RideRequests_FromFirebase(
    from_collection, to_collection, ride_request_doc_id
):
    """
    Remove ride requests from Firebase ride-request collection
    """
    from_doc_ref = db.collection(from_collection).document(ride_request_doc_id)
    ride_request = from_doc_ref.get().to_dict()
    to_doc_ref = db.collection(to_collection).document(ride_request_doc_id)
    to_doc_ref.set(ride_request)
    from_doc_ref.delete()


def main():
    # matchDict = {'match1': ['riderequest1', 'riderequest2'], 'match2': ['riderequest3', 'riderequest4']}

    # testing match! yay
    match = Match()
    print("\nmatch dict: ", match.match_dict)
    input_Matches_ToFirebase(match.match_dict)
    match_for_request = get_match(match.match_dict, "Wmc7r9Jwj3KvQvW3Z6gV")
    print("\nmatch for request: ", match_for_request)

    # input_RideRequest_ToFirebase(ride_request_1)
    # delete_Item_FromFirebase("ride-requests", "C102485152896")
    # archive_RideRequests_FromFirebase("ride-requests", "deleted-requests", "C102485129977")


# if __name__ == "__main__":
    # main()
    # get_match(match_dict, request_id)
    

# if __name__ == "__main__":
#     app.run(port=8848)  # Specify the desired port
