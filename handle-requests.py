#authors: kim, sandy, alice, nissi, edith
#time: april 5th, 2023

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize the Firebase app with your project credentials
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from matchingAPI import matching #TODO: import matching API

# Get a reference to the Firestore collection
db = firestore.client()
unmatched_collection_ref = db.collection('unmatched-list')
matched_collection_ref = db.collection('matched-list')

#def match_unmatched(user_list)
    #matches = match.match_users(user_list)
        #here, we access the class from match API, and use their 
        #function to match the users in the user_list parameter and we put
        #the json file that is returned into variable 

def match_unmatched(unmatched_user_list):
    # put user_list of unmatched users into the matching algorithm from matching API
    matches = refresh(unmatched_user_list) # returns dictionary: key - rideID, value - list of user IDs in carpool

    for rideID in matches:
        pool = matches[rideID]  # [user1ID, user2ID, ...]
        for userID in pool:
            # Note: user 1 can have multiple ride requests so need to remove them 
            # from the unmatched_user_list based on user_ID AND depart_time
            # remove them from the unmatched_user_list using their user_ID and depart_time
            # AND add the matched user in the matched-list collection - to recover users for cancels
            # TODO: remove requests from matched-list collection once arrival time passed
            unmatched_doc_ref = unmatched_collection_ref.get() # gets all the documents in collection
            for request in unmatched_doc:
                if request["user_ID"] == request[userID]:
                    #TODO: assuming request is document ID
                    # Get the document data (dictionary) from the unmatched collection
                    unmatched_doc_ref = unmatched_collection_ref.document(request)
                    unmatched_doc = unmatched_doc_ref.get().to_dict() # make into dictionary
                    # create the document with same request id in matched collection
                    matched_doc_ref = matched_collection_ref.document(request)
                    # puts unmatched request info into the matched document 
                    matched_doc_ref.set(unmatched_doc)
                    print("Document from unmatched request collection added to matched request collection")
                    # remove the request from unmatched collection
                    unmatched_list_ref.document(request).delete()
                    print("Document deleted successfully!")




#def refresh(unmatched_user_list)
    # every xx time do this:
    return match.match_users(unmatched_user_list)

#def handle_user_bail()
    #case 1: normal
    #case 2: if user bails out
        #1. update pool in matched.json
        #OR
        #2. if other users in pool don't like new cost or user x was a driver,
        #then put them in user_list and remove pool from matched.json
            #assuming we get a cancel notification
