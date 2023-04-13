
# Create a Match Class, where we match people based on the information we get
# from the data that Ride Request API (ex. sampledata-rider.json) imports (put into) into Firebase

# run an instance of a match for each user that is not matched yet
# TODO: need a list of all users that requested rides from Firebase

import heapq # for priority queue
import numpy as np # for various path calculations
from geopy.geocoders import Nominatim # for Open Street Map, to convert addresses to numerical values

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
class Match:
    def __init__(self, currUserID):
        self.userID = currUserID # import a user from Firebase
        self.priorityQueue = []
        # a list of users not matched yet
        self.user_list = firebase_db.child("riderequest").get().val() #TODO: get from firebase  need to check for accuracy

        # geocode give us longitude and latitude in degrees
        #TODO: need to format the addresses in firebase json file for riders and drivers for OpenStreetMap
        address = self.user_list[self.userID]["origin_address"]["street"] + ", " + self.user_list[self.userID]["origin_address"]["city"] + ", " + self.user_list[self.userID]["origin_address"]["state"] + " " + self.user_list[self.userID]["origin_address"]["zip"]

        self.origin_address= geolocator.geocode(address) #TODO: get address from firebase need to check for address accuracy
        # self.destination_address = geolocator.geocode(address) #TODO: get address from firebase
        
        # self.depart_time = #TODO: get from firebase
        # self.desired_cost_max = #TODO: get from firebase
        # self.user_type = #TODO: get from firebase
        self.depart_time =self.user_list[self.userID]["depart_time"]
        self.desired_cost_max =self.user_list[self.userID]["desired_cost_max"]
        self.user_type =self.user_list[self.userID]["user_type"]
        self.number_people = self.user_list[self.userID]["user_type"] #use this instead of desired cost or capacity


    # function to match people based on priority queue
    #for riders, match based on split costs (desired cost/number of users)
    #for drivers, match based on car capacity
    #use if statements

    def match_users():
        match_pool = {}

        for otherUser in user_list:
            otherUser_score = this.matchScore(otherUser)
            # note: need to negate the scores for queue to have highest scores at top
            heapq.heappush(this.priorityQueue, (-otherUser_score, otherUser.userID))
        
        
        match_pool[rideID] = [self.userID]
        for i in range(capacity-1):
            match_pool[rideID].append(heapq.heappop())
        #TODO: using the priority queue, match this user to the users based on car capacity or on desired cost 
        return match_pool

    # Create a match score for every other user relative to this user 
    # and use this to create a priority queue for this user
    # Note: each user has their own priority queue
    # Returns: otherUser matching score relative to this user
    def matchScore(otherUser):
        # compare based on 
            # 1. start/end locations & depart time
            # *create queue (make sure not to match driver with driver - skip over that user)
        match_score = 0
        location_threshold = 10 #TODO: need to get units of the location len diff (assume 1 mile for now) #originally 1
        angle_threshold = 90 #TODO: need more accurate angle in degrees
        depart_time_threshold = 1800 #TODO: need to get units of time diff (assume seconds for now)
        desired_cost_threshold = 10 # assume $10 difference in desired cost for now

        #TODO: need to get length difference of address locations 
        #TODO: these points need to be numerical before stored in firebase for matching API

        # get absolute value difference to see if they are similar enough
        # need to first group users departing from similar origin locations: get length of path diff between users' origins
        origin_location_diff = np.linalg.norm(calculate_path(this.origin_address, otherUser.origin_address))
        # angle diff shows us how far their destinations are from each other & if
        # users are going in relatively same direction
        this_user_path = calculate_path(this.origin_address, this.destination_address)
        other_user_path = calculate_path(otherUser.origin_address, otherUser.destination_address)
        dest_angle = calculate_angle(this_user_path, other_user_path)
        # 2nd priorities: travel time and desired cost (may not need desired cost?)
        depart_time_diff = abs(this.depart_time - otherUser.depart_time)
        desired_cost_diff = abs(this.desired_cost_max - otherUser.desired_cost_max)

        # don't match a driver with a driver
        if not (this.user_type == "driver" and otherUser.user_type == "driver"):
            # first priorities get 10 points
            #TODO: adjust the point system to get more accurate matches
            if origin_location_diff <= location_threshold:
                match_score += 10-origin_location_diff #adds more to match_score if the difference is smaller (max is 10 points) 
            if dest_angle <= angle_threshold:
                match_score += 10*((90-dest_angle)/90) #adds more to match_score if the dest_angle is smaller (max is 10 points) ...etc.
            if depart_time_diff <= depart_time_threshold:
                match_score += 10*(1800-depart_time_diff)/1800
            # second priorities get 5 points
            if desired_cost_diff <= desired_cost_threshold:
                match_score += 5

        return match_score 
            

    # Helper function: calculate path line of users origin to dest points
    # for simplicity, we assume all paths are straight lines (or else we need to sum the integrals eek)
    # Returns: line between two points
    def calculate_path(point1, point2):
        # Get the latitude and longitude of each location
        lat1, lon1 = point1.latitude, point1.longitude
        lat2, lon2 = point2.latitude, point2.longitude

        # Convert the latitude and longitude values to radians
        lat1 = np.deg2rad(lat1)
        lon1 = np.deg2rad(lon1)
        lat2 = np.deg2rad(lat2)
        lon2 = np.deg2rad(lon2)

        # Calculate the slope and y-intercept of the line
        m = (lat2 - lat1) / (lon2 - lon1)
        b = lat1 - m * lon1

        # Create an array of x-values (longitude values)
        x = np.linspace(lon1, lon2, 100) # generates an array of 100 lon values between the 2 points

        # Calculate the corresponding y-values (latitude values)
        y = m * x + b

        # Convert the latitude and longitude values back to degrees
        x_deg = np.rad2deg(x)
        y_deg = np.rad2deg(y)

        # The resulting line as an array of latitude and longitude coordinates
        return np.array([y_deg, x_deg])


    # Helper function: calculates the angle between the two lines using dot product
    # This information will be needed to group people traveling along
    # similar paths together
    # Returns: angle between paths in degrees
    def calculate_angle(line1, line2):
        # Calculate the angle between the lines using the dot product
        cos_theta = np.dot(line1, line2) / (np.linalg.norm(line1) * np.linalg.norm(line2))
        theta = np.arccos(cos_theta)
        # Convert the angle to degrees
        theta_degrees = np.degrees(theta)
        return theta_degrees

         
            
