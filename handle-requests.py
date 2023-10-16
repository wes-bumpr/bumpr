import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

cred = credentials.Certificate("bumpr-firebase-service-acckey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def input_RideRequest_ToFirebase(rideRequestDict):
    '''
    Puts one ride request info into Firebase
    '''
    for r in rideRequestDict:
        request = {
            "depart_time": rideRequestDict["depart_time"],
            "destination_address": rideRequestDict["destination_address"],
            #TODO: finish up
        }
        # Generate a random integer with 5 digits (between 10000 and 99999)
        random_integer = random.randrange(10000, 100000)
        request_doc_id = request[user_ID] + random_integer
        doc_ref = db.collection(u"ride-requests").document(request_doc_id)


def input_Matches_ToFirebase(matchedDict):
    '''
    Get the list of ride requests that were matched from score.py
    Put match into Firebase collection

    {match1: [riderequest1, riderequest2], ...}
    '''
    for m in matchedDict:
        match = {
            'matchID': m,
            'ride_request_ID': matchedDict[m]
        }
        doc_ref = db.collection(u"matches").document(m)
        doc_ref.set(match)





def remove_RideRequest_FromFirebase():
    '''
    Remove ride requests from Firebase ride-request collection
    '''



def main():
    matchDict = {'match1': ['riderequest1', 'riderequest2'], 'match2': ['riderequest3', 'riderequest4']}
    matchListToJSON(matchDict)

if __name__ == "__main__":
    main()