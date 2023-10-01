# Create a Match Class, where we match people based on the information we get
# from the data that Ride Request API (ex. sampledata-rider.json) imports (put into) into Firebase

# Note: Run an instance of a match for each user that is not matched yet

import heapq  # for priority queue
import numpy as np  # for various path calculations
import unittest
from request import *

# command line: pip install geopy
# Initialize the geolocator with the OpenStreetMap provider
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="bumprTest")  # TODO: set to correct app (bumpr)


# TODO: Clear document up with new request.py api
class Match:
    """
    Creates Single Match (?) by drawing out pairs from current unmatched list
    """
    def __init__(self, currUserID):
        # Necessary Info: unmatched list
        pass

    def match_users(self):
        """
        Matches other users to this user
        based on other users' match scores
        relative to this user. 
        """
        match_pool = {}
        for otherUser in self.user_list:
            otherUser_score = self.matchScore(otherUser)
            # note: need to negate the scores for queue to have highest scores at top
            heapq.heappush(self.priorityQueue, (-otherUser_score, otherUser.userID))

        match_pool[self.rideID] = [self.userID]
        for _ in range(self.number_desired_carpoolers):
            match_pool[self.rideID].append(heapq.heappop())
        # TODO: using the priority queue, match this user to the users based on car capacity AND/OR on desired cost
        return match_pool

    def matchScore(self, otherUser):
        """
        Create a match score for every other user relative to this user 
        and use this to create a priority queue for this user
        Note: each user has their own priority queue
        Returns: otherUser matching score relative to this user
        """
        match_score = 0
        location_threshold = 10  # TODO: need to get units of the location len diff (assume 1 mile for now) #originally 1
        angle_threshold = 90  # TODO: need more accurate angle in degrees
        depart_time_threshold = 1800  # TODO: need to get units of time diff (assume seconds for now)
        desired_carpoolers_threshold = 1  # assume this difference in desired number of carpoolers now

        # get absolute value difference to see if they are similar enough
        # need to first group users departing from similar origin locations: get length of path diff between users' origins
        origin_location_diff = np.linalg.norm(self.calculate_path(self.origin_address, otherUser.origin_address))
        # angle diff shows us how far their destinations are from each other & if
        # users are going in relatively same direction
        this_user_path = self.calculate_path(self.origin_address, self.destination_address)
        other_user_path = self.calculate_path(otherUser.origin_address, otherUser.destination_address)
        dest_angle = self.calculate_angle(this_user_path, other_user_path)
        # 2nd priorities: travel time and desired cost (may not need desired cost?)
        depart_time_diff = abs(self.depart_time - otherUser.depart_time)
        desired_carpoolers_diff = abs(self.number_desired_carpoolers - otherUser.number_desired_carpoolers)

        # don't match a driver with a driver
        if not (self.user_type == "driver" and otherUser.user_type == "driver"):
            # TODO: adjust the point system to get more accurate matches
            if origin_location_diff <= location_threshold:
                match_score += 10 - origin_location_diff  # adds more to match_score if the difference is smaller (max is 10 points)
            if dest_angle <= angle_threshold:
                match_score += 10 * ((
                                             90 - dest_angle) / 90)  # adds more to match_score if the dest_angle is smaller (max is 10 points) ...etc.
            if depart_time_diff <= depart_time_threshold:
                match_score += 10 * (1800 - depart_time_diff) / 1800
            if desired_carpoolers_diff <= desired_carpoolers_threshold:
                match_score += 5

        return match_score


def calculate_path(origin, destination):
    """
    Helper function: calculate path line of users origin to dest points
    for simplicity, we assume all paths are straight lines (or else we need to sum the integrals eek)
    :param: point1 and point2. Pre-processed geocode information
    :return: line between two points
    """
    # Get the latitude and longitude of each location
    lat1, lon1 = origin.latitude, origin.longitude
    lat2, lon2 = destination.latitude, destination.longitude

    # Convert the latitude and longitude values to radians
    lat1 = np.deg2rad(lat1)
    lon1 = np.deg2rad(lon1)
    lat2 = np.deg2rad(lat2)
    lon2 = np.deg2rad(lon2)

    # Calculate the slope and y-intercept of the line
    m = (lat2 - lat1) / (lon2 - lon1)
    b = lat1 - m * lon1

    # Create an array of x-values (longitude values)
    x = np.linspace(lon1, lon2, 100)  # generates an array of 100 lon values between the 2 points

    # Calculate the corresponding y-values (latitude values)
    y = m * x + b

    # Convert the latitude and longitude values back to degrees
    x_deg = np.rad2deg(x)
    y_deg = np.rad2deg(y)

    # The resulting line as an array of latitude and longitude coordinates
    return np.array([y_deg, x_deg])


def calculate_angle(line1, line2):
    """
    # Helper function: calculates the angle between the two lines using dot product
    # This information will be needed to group people traveling along
    # similar paths together
    :param line1: np array
    :param line2:
    :return: angle between paths in degrees
    """
    # Calculate the direction vectors of the lines
    direction_vector1 = line1[:, 1:] - line1[:, :-1]  # Calculate differences along columns
    direction_vector2 = line2[:, 1:] - line2[:, :-1]

    # Calculate the dot product between the direction vectors
    dot_product = np.dot(direction_vector1.flatten(), direction_vector2.flatten())

    # Calculate the magnitudes (norms) of the direction vectors
    magnitude1 = np.linalg.norm(direction_vector1)
    magnitude2 = np.linalg.norm(direction_vector2)

    # Calculate the angle in radians between the two lines
    angle_radians = np.arccos(dot_product / (magnitude1 * magnitude2))

    # Convert the angle to degrees if needed
    angle_degrees = np.degrees(angle_radians)

    return angle_degrees


def main():
    ## test geolocator - input locations ##
    loc1 = geolocator.geocode({'zip': '02453', 'state': 'MA', 'city': 'Waltham', 'street': '415 South St'})
    loc2 = geolocator.geocode({'zip': '02481', 'state': 'MA', 'city': 'Wellesley',
                               'street': '106 Central Street'})  # 21 Wellesley College Rd returns no result
    loc3 = geolocator.geocode({'zip': '02139', 'state': 'MA', 'city': 'Cambridge',
                               'street': '77 Massachusetts Ave'})
    # print(loc1)
    # print(loc2)
    # print(loc3)
    # print(loc2.latitude)

    ## test path calculation - returns np-array ##
    # print(calculate_path(loc1, loc2))

    ## test angle calculation ##
    # path1 = calculate_path(loc2, loc1)
    # path2 = calculate_path(loc2, loc3)
    # path3 = calculate_path(loc3, loc2)
    # print(calculate_angle(path1, path2))  # prints 41 degrees
    # print(calculate_angle(path1, path3))  # prints 139 degrees


if __name__ == "__main__":
    main()
