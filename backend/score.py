# Create a Score Class, where we score people based on the information we get
# from the data that Ride Request API (ex. sampledata-rider.json) imports (put into) into Firebase

# Note: Run an instance of a match for each user that is not matched yet

import numpy as np  # for various path calculations
from get_request import GetRequest  # TODO: modified but not tested. Test if working
from datetime import datetime

# for geo-related calculations
# command line: pip install geopy
from geopy import distance
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="bumprTest")


class Score:
    """
    Creates Single Match by drawing out pairs from current unmatched list
    """

    def __init__(self, request_id1, request_id2):

        self.request_id1 = request_id1
        self.request_id2 = request_id2

        self.request1 = GetRequest(request_id1)
        self.request2 = GetRequest(request_id2)

        self.request1_origin_geo_coordinates, self.request2_origin_geo_coordinates, self.request1_destination_geo_coordinates, self.request2_destination_geo_coordinates = self.get_geocode_points()

    def get_geocode_points(self):
        """
        extract geolocation information and process it to (latitude, longitude) format
        :return: geo coordinate representations or request 1 and request 2 origins and destinations
        """
        # geocode: general geo information storage
        request1_origin_geocode = geolocator.geocode(self.request1.get_origin_address())
        request2_origin_geocode = geolocator.geocode(self.request2.get_origin_address())
        request1_destination_geocode = geolocator.geocode(self.request1.get_destination_address())
        request2_destination_geocode = geolocator.geocode(self.request2.get_destination_address())
        # geo_coordinates: in the form of latitude, longitude
        request1_origin_geo_coordinates = (request1_origin_geocode.latitude, request1_origin_geocode.longitude)
        request2_origin_geo_coordinates = (request2_origin_geocode.latitude, request2_origin_geocode.longitude)
        request1_destination_geo_coordinates = (
            request1_destination_geocode.latitude, request1_destination_geocode.longitude)
        request2_destination_geo_coordinates = (
            request2_destination_geocode.latitude, request2_destination_geocode.longitude)
        return request1_origin_geo_coordinates, request2_origin_geo_coordinates, request1_destination_geo_coordinates, request2_destination_geo_coordinates

    # make helper functions that score one difference at
    # a time based on ranges. ex. score_time_diff (if between
    # 10 to 15 min, give higher score), if scores return 0 (too far
    #  or out of time range of an 1hr) return 0 in match_score. weight
    #  each scores based on priorities and return totaled score.

    def score_depart_time_diff(self):
        """
        Helper function for match_score().

        Scores request1 and request2 based on how close their depart time is.

        Note: score of 0-10 depends on where the diff lies in a range of 
        values from a depart time diff of 0-3600 with a step of 360 seconds
        (i.e. a diff of 365 seconds lies in range [360, 720) so it get a score of 1).
        Returns: a number between 0-10 or -1, where 0 means they ARE a good match
        and 10 means they're NOT a good match.

        **Note: a score of 0 means they ARE a good match, 10 means they are NOT
        and a score of -1 means they should not be a match.
        """
        depart_time_threshold = 3600  # in seconds - 1 hour threshold
        date_format = "%m/%d/%Y %H:%M"
        request1_depart_time = datetime.strptime(self.request1.get_depart_time(), date_format)
        request2_depart_time = datetime.strptime(self.request2.get_depart_time(), date_format)
        depart_time_diff = abs(request1_depart_time - request2_depart_time).total_seconds()
        # if depart time of request1 and request2 are more than an hour difference -> don't match
        if depart_time_diff > depart_time_threshold:
            return -1
        else:
            return int(
                depart_time_diff / 360)  # Note: a 1 hr diff gets a score of 10 while a 59 min diff gets a score of 9

    def score_origin_location_diff(self):
        """
        Helper function for match_score().

        First checks if origin_location_diff is greater than the threshold 
        and returns -1 if it is. Otherwise, it converts the origin_location_diff 
        into an integer value between 0 and 10 based on 0.1 mi step (i.e. diff between
        0.1 (inclusive) and 0.2 (exclusive) should get a score of 1).

        **Note: a score of 0 means they ARE a good match, 10 means they are NOT
        and a score of -1 means they should not be a match.
        """
        origin_location_threshold = 1  # in miles
        origin_location_diff = distance.distance(self.request1_origin_geo_coordinates,
                                                 self.request2_origin_geo_coordinates).miles
        # print("location_diff", origin_location_diff)
        if origin_location_diff > origin_location_threshold:
            return -1
        else:
            return int(origin_location_diff * 10)

    def score_path_angle(self):
        """
        Score is based on where the path angle lies in a 
        range of 0-90 degrees with a step of 9 degrees.

        **Note: a score of 0 means they ARE a good match, 10 means they are NOT
        and a score of -1 means they should not be a match.
        """
        angle_threshold = 60  # in degrees
        request1_path = calculate_path(self.request1_origin_geo_coordinates, self.request1_destination_geo_coordinates)
        request2_path = calculate_path(self.request2_origin_geo_coordinates, self.request2_destination_geo_coordinates)
        path_angles = calculate_angle(request1_path, request2_path)

        if path_angles > angle_threshold:
            return -1
        else:
            return int(path_angles / 6)  # Note: an angle of 60 deg gets a score of 10 while 59 deg gets score of 9

    def score_num_people_traveling(self):
        """
        Score is based on number of carpoolers

        **Note: a score of 0 means they ARE a good match, 10 means they are NOT
        and a score of -1 means they should not be a match.

        default max carpoolers: 4.
        """
        default_max_carpoolers = 4  # in person
        total_num_people = self.request1.get_total_num_people_traveling() + self.request2.get_total_num_people_traveling()
        if total_num_people > default_max_carpoolers:
            return -1
        else:
            # TODO: need a better way to score this
            # min of 2 people and max of 4 people
            if total_num_people == 2:
                return 10
            elif total_num_people == 3:
                return 5
            elif total_num_people == 4:
                return 0

    def match_score(self):
        """
        Create a match score for every other user relative to this user 
        and use this to create a priority queue for this user

        Note: each user has their own priority queue

        **Note: a score of 0 means they ARE a good match, 10 means they are NOT
        and a score of -1 means they should not be a match.

        Returns: request_id1, request_id2, score
        """
        match_score = 0

        # 1st priority: carpoolers limit (either works or doesn't)
        # If below limit, continue to other criteria. If not, return score of -1.
        num_people_traveling_score = self.score_num_people_traveling()
        if num_people_traveling_score == -1:
            print("terminated after num_people_traveling failed")
            return -1
        else:
            print("num_people_traveling: ", num_people_traveling_score)
            match_score += 0.5 * num_people_traveling_score

        # 2nd priority: depart time difference
        depart_time_score = self.score_depart_time_diff()
        if depart_time_score == -1:
            print("terminated after depart_time_score failed")
            return -1
        else:
            print("depart time: ", depart_time_score)
            match_score += depart_time_score

        # 3rd priority: origin location difference in miles
        origin_location_diff_score = self.score_origin_location_diff()
        if origin_location_diff_score == -1:
            print("terminated after origin location diff too big")
            return -1
        else:
            print("origin location diff: ", origin_location_diff_score)
            match_score += origin_location_diff_score

        # 4th priority: path angle (whether destinations are along the same route)
        path_angle_score = self.score_path_angle()
        if path_angle_score == -1:
            print("terminated after path_angle diff too big")
            return -1
        else:
            print("path angle diff: ", path_angle_score)
            match_score += path_angle_score

        # general check to ensure that overall score is not too big
        # max score is 35 based on current calculation
        if match_score > 30:
            print("overall assessment of score failed the match")
            return -1

        print("match successful.")
        return match_score


def calculate_path(origin, destination):
    """
    Helper function: calculate path line of users origin to dest points
    for simplicity, we assume all paths are straight lines (or else we need to sum the integrals eek)
    :param: origin and destination. Pre-processed tuples of (latitude, longitude)
    :return: line between two points
    """
    # # Get the latitude and longitude of each location
    # lat1, lon1 = origin.latitude, origin.longitude
    # lat2, lon2 = destination.latitude, destination.longitude
    lat1, lon1 = origin
    lat2, lon2 = destination

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
    print("angle degrees:", angle_degrees)
    return angle_degrees


def main():
    # ## test geolocator - input locations ##
    # loc1 = geolocator.geocode({'zip': '02453', 'state': 'MA', 'city': 'Waltham', 'street': '415 South St'})
    # loc2 = geolocator.geocode({'zip': '02481', 'state': 'MA', 'city': 'Wellesley',
    #                            'street': '106 Central Street'})  # 21 Wellesley College Rd returns no result
    # loc3 = geolocator.geocode({'zip': '02139', 'state': 'MA', 'city': 'Cambridge',
    #                            'street': '77 Massachusetts Ave'})
    # loc1_geo_coordinates = (loc1.latitude, loc1.longitude)
    # loc2_geo_coordinates = (loc2.latitude, loc2.longitude)
    # loc3_geo_coordinates = (loc3.latitude, loc3.longitude)
    # # print(loc1)
    # # print(loc2)
    # # print(loc3)
    # # print(loc2.latitude)
    #
    # ## test path calculation - returns np-array ##
    # path1 = calculate_path(loc2_geo_coordinates, loc1_geo_coordinates)
    # path2 = calculate_path(loc2_geo_coordinates, loc3_geo_coordinates)
    # path3 = calculate_path(loc3_geo_coordinates, loc2_geo_coordinates)
    # # print(path1)
    #
    # ## test angle calculation ##
    # print(calculate_angle(path1, path2))  # prints 41 degrees
    # print(calculate_angle(path1, path3))  # prints 139 degrees

    test = Score("Hailey1001", "Wmc7r9Jwj3KvQvW3Z6gV")
    print(test.match_score())


if __name__ == "__main__":
    main()
