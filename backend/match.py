# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

from score import Score  # TODO: modified but not tested. Test if working
from handle_requests import delete_Item_FromFirebase  # TODO: modified but not tested. Test if working
from get_request import db, GetRequest  # TODO: modified but not tested. Test if working
from datetime import datetime


class Match:
    """
    Look over collection of unmatched ride requests to create matches based on score
    """

    def __init__(self):
        """
        performs the matching

        request_to_match: list of unmatched requests
        """
        docs = db.collection(u"ride-requests").stream()

        # create a list of expired ride requests to delete and let user who made request know it was deleted
        # to_be_deleted_requests_docid = []
        # date_format = "%m/%d/%Y %H:%M"
        # for doc in docs:
        #     request = GetRequest(doc.id)
        #     request_depart_time = datetime.strptime(request.get_depart_time(), date_format)
        #     current_time = datetime.now().timestamp() # current time in seconds
        #     print("current time: ", str(current_time))
        #     if current_time > request_depart_time.timestamp(): # current time is past the request's depart time (way past their depart time)
        #         print("expired time: ", str(request_depart_time))
        #         to_be_deleted_requests_docid.append(doc.id)
        #         delete_Item_FromFirebase("ride-requests", doc.id)
        
        # print("requests to be deleted: ", to_be_deleted_requests_docid)
        # TODO: let users know that their ride request was deleted AND if their request was matched using the list
            

        # get requests to be matched from firebase
        self.requests_to_match = []
        for doc in docs:
            self.requests_to_match.append(doc.id)
        # print(self.requests_to_match)
        # end of getting list of requests

        # initialize score dictionary
        self.sorted_score_dict = {}

        # initialize match dictionary
        self.match_dict = {}

        # run the match
        self.create_score_dictionary()
        self.create_matches()
        print(self.match_dict)

    def create_score_dictionary(self):
        """
        intended to be helper
        returns sorted score dictionary of valid scores with format {(request1, request2): score}
        generates score dictionary by checking request pairs
        :return: null
        """
        unsorted_score_dict = {}
        request_index = len(self.requests_to_match)
        for i in range(request_index):
            for j in range(i + 1, request_index):
                pair_score = Score(self.requests_to_match[i], self.requests_to_match[j]).match_score()
                if pair_score != -1:
                    match_id = (self.requests_to_match[i], self.requests_to_match[j])
                    unsorted_score_dict[match_id] = pair_score
        self.sorted_score_dict = dict(sorted(unsorted_score_dict.items(), key=lambda item: item[1]))

    def add_match_info(self, request1_id, request2_id):
        '''
        Given request1 id and request2 id
        build the dictionary with the match information --> which will
        be the value for a match key in the match_dict dictionary
        '''
        request1 = GetRequest(request1_id)
        request2 = GetRequest(request2_id)
        users = [request1.get_user_id(), request2.get_user_id()] # users that made the requests (note: a request may have more than 1 rider)
        origin = [request1.get_origin_address(), request2.get_destination_address()]
        to = [request1.get_destination_address(), request2.get_destination_address()]
        date_format = "%m/%d/%Y %H:%M"
        request1_depart_time = datetime.strptime(request1.get_depart_time(), date_format)
        request2_depart_time = datetime.strptime(request2.get_depart_time(), date_format)
        if request1_depart_time < request2_depart_time:
            depart_time = request1.get_depart_time()
        else:
            depart_time = request2.get_depart_time()
        return {"users": users, "origin": origin, "to": to, "depart_time": depart_time}

   
    def create_matches(self):
        """
        intended to be helper
        :return: null
        """
        while self.sorted_score_dict:
            # get best scored item
            best_scored = next(iter(self.sorted_score_dict.items()))  # gives ((request1, request2), score) tuple
            request1_name = best_scored[0][0] # request id
            request2_name = best_scored[0][1]

            # add to match_dict
            match_id = request1_name + request2_name
            match_info = self.add_match_info(request1_name, request2_name)
            self.match_dict[match_id] = match_info # best_scored[1]

            # remove other pairs of matches with either request1 or request2
            sorted_score_dict_original = self.sorted_score_dict.copy()
            for key in sorted_score_dict_original:
                if request1_name in key or request2_name in key:
                    del self.sorted_score_dict[key]

    def get_match_dict(self):
        return self.match_dict


def main():
    # unsorted_score_dict = {("1", "2"): 15, ("5", "2"): 18, ("6", "-1"): -1}
    # sorted_score_dict = dict(sorted(unsorted_score_dict.items(), key=lambda item: item[1]))
    # print(sorted_score_dict)
    # best_scored = next(iter(sorted_score_dict.items()))
    # print(best_scored)
    # match_id = best_scored[0][0] + best_scored[0][1]
    # print(match_id)
    test = Match()
    # print(test.get_match_dict())

    pass


if __name__ == "__main__":
    main()
