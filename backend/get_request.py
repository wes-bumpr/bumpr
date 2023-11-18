import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# TODO: db initialization could be put into a “main” eventually
cred = credentials.Certificate("bumpr-firebase-service-acckey.json")
firebase_admin.initialize_app(cred)  # only need to be called once

db = firestore.client()


class GetRequest:
    """
    Ride request objects retrieved from database
    """

    def __init__(self, request_doc_id):
        # get request doc from ride-requests collection from Firebase
        self.ride_requests_ref = db.collection(u"ride-requests-test").document(request_doc_id)
        # convert one request data from ride-request collection to dictionary for each access
        self.request_doc = self.ride_requests_ref.get().to_dict()

    def get_depart_time(self):
        """
        Returns data and time in this format: mm/dd/yyyy hh:mm
        of request's required departure time from origin address
        """
        return self.request_doc["depart_time"]

    def get_destination_address(self):
        """
        Returns a string of the request's destination address
        """
        return self.request_doc["destination_address"]

    def get_origin_address(self):
        """
        Returns a string of the request's destination address.
        """
        return self.request_doc["origin_address"]

    def get_total_num_people_traveling(self):
        """
        :return: number of people traveling in int format
        """
        return self.request_doc["total_num_people_traveling"]

    def get_user_id(self):
        """
        Returns string of user's Wellesley ID of the user
        who made the request
        """
        return self.request_doc["user_ID"]

    def get_origin_geocode_coordinates(self):
        """
        :return: geo coordinates in the format of (latitude, longitude)
        """
        return self.request_doc["origin_geocode"]["latitude"], self.request_doc["origin_geocode"]["longitude"]

    def get_destination_geocode_coordinates(self):
        """
        :return: geo coordinatesin the format of (latitude, longitude)
        """
        return self.request_doc["destination_geocode"]["latitude"], self.request_doc["destination_geocode"]["longitude"]

    # def get_ride_share(self):
    #     """
    #     Returns True if user who made request wants to share rides via Lyft/Uber
    #     """
    #     return self.request_doc["ride_share"]

    # def get_personal_car(self):
    #     """
    #     Returns True if user that made request has a car (driver)
    #     """
    #     return self.request_doc["personal_car"]

    # def get_user_type(self):
    #     """
    #     Returns string of whether user who made request is rider or driver
    #     """
    #     return self.request_doc["user_type"]


def main():
    # testing purposes
    request = GetRequest("Wmc7r9Jwj3KvQvW3Z6gV")
    # print(request.get_depart_time())
    # print(request.get_destination_address())
    # print(request.get_origin_geocode_coordinates())
    print("Hello, this is the main function!")


if __name__ == "__main__":
    main()

# newest
