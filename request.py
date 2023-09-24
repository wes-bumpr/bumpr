import firebase_admin
from firebase_admin import firestore
cred = credentials.Certificate('/path/to/bumpr-firebase-service-acckey.json')
firebase_admin.initialize_app(cred)

# Initialize to retrieve data from Firebase - ride-request collection
db = firestore.client()
riderequests_ref = db.collection('ride-requests')

# Initialize the geolocator with the OpenStreetMap provider
geolocator = Nominatim(user_agent="my-application") #TODO: set to correct app (bumpr)

import pyrebase

config = {
  "apiKey": "AIzaSyAhw3p7cqnaQmczTxfUAts4lLfMLWJYG5Y",
  "authDomain": "domain", #find
  "databaseURL": "https://bumpr-db1f3-default-rtdb.firebaseio.com/", #from realtime database, need to check
  "storageBucket": " " #find
}

firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()

class Request:
    def __init__(self, request_document_ID):
        self.priorityQueue = []

        # a list of users not matched yet
        self.request_list = firebase_db.child("ride-request").get().val() #TODO: get from firebase need to check for accuracy

        # ride request ID
        self.rideID = self.request_list[request_document_ID]["ride_request_ID"]

        # geocode gives us longitude and latitude in degrees
        #TODO: need to format the addresses in firebase json file for riders and drivers for OpenStreetMap
        address = self.request_list[request_document_ID]["origin_address"]["street"] + ", " 
        + self.request_list[request_document_ID]["origin_address"]["city"] + ", " 
        + self.request_list[request_document_ID]["origin_address"]["state"] + " " 
        + self.request_list[request_document_ID]["origin_address"]["zip"]
        self.origin_address= geolocator.geocode(address) #TODO: get address from firebase need to check for address accuracy
        # self.destination_address = geolocator.geocode(address) #TODO: get address from firebase
        
        self.depart_time = self.request_list[request_document_ID]["depart_time"]
        self.desired_cost_max = self.request_list[request_document_ID]["desired_cost_max"]
        self.user_type = self.request_list[request_document_ID]["user_type"]
        self.number_desired_carpoolers = self.request_list[request_document_ID]["user_type"] #use this instead of desired cost or capacity


