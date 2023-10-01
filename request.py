import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("bumpr-firebase-service-acckey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# put data
# for record in data:
#     doc_ref = db.collection(u"ride-requests").document(record["ride_request_ID"])
#     doc_ref.set(record)

# get data
# ride_requests_ref = db.collection(u"ride-requests")
# docs = ride_requests_ref.stream()
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
# print(next(docs).to_dict()) # get first doc
# Create a reference to the document
doc_ref = db.collection("ride-requests").document("Wmc7r9Jwj3KvQvW3Z6gV")
# Get the document data
doc = doc_ref.get()
# print(doc.to_dict())

class Request:
    """
    Ride request objects retrieved from database
    """
    def __init__(self, request_document_ID):
        """
        Initiallizes request objects based on its storage in database
        :param request_document_ID: Identifier to get the request object
        """
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
        # self.origin_address= geolocator.geocode(address) #TODO: get address from firebase need to check for address accuracy
        # self.destination_address = geolocator.geocode(address) #TODO: get address from firebase
        
        self.depart_time = self.request_list[request_document_ID]["depart_time"]
        self.desired_cost_max = self.request_list[request_document_ID]["desired_cost_max"]
        self.user_type = self.request_list[request_document_ID]["user_type"]
        self.number_desired_carpoolers = self.request_list[request_document_ID]["user_type"] #use this instead of desired cost or capacity

        print("Adress",address)

        #TODO: getters & setters

    def get_depart_time(self):
        """
        Returns data and time in this format: mm/dd/yyyy hh:mm
        of request's required departure time from origin address
        """
        return self.request_doc["depart_time"]

    def get_destination_address(self):
        """
        Returns a dictionary of the request's destination address:
        zip, state, city, street.
        """
        return self.request_doc["destination_address"]
    
    def get_destination_time(self):
        """
        Returns date and time in this format: mm/dd/yyyy hh:mm
        of request's destination time (time they need to get there)
        """
        return self.request_doc["destination_time"]
    
    def get_desired_num_carpoolers(self):
        """
        Returns integer of the request's desired number
        of people they want to carpool with.
        """
        return self.request_doc["desired_num_carpoolers"]

    def get_ride_share(self):
        """
        Returns True if user who made request wants to share rides via Lyft/Uber
        """
        return self.request_doc["ride_share"]

    def geT_personal_car(self):
        """
        Returns True if user that made request has a car (driver)
        """
        return self.request_doc["personal_car"]

    def get_user_ID(self):
        """
        Returns string of user's Wellesley ID of the user 
        who made the request
        """
        return self.request_doc["user_ID"]
    
    def get_user_type(self):
        """
        Returns string of whether user who made request is rider or driver
        """
        return self.request_doc["user_type"]

    
       
def main():
    # testing purposes
    request = Request("Wmc7r9Jwj3KvQvW3Z6gV")
    print(request.get_depart_time())
    print(request.get_destination_address())
    print("Hello, this is the main function!")

if __name__ == "__main__":
    main()
