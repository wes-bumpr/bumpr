import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate("bumpr-firebase-service-acckey.json")
# firebase_admin.initialize_app(cred)
#
# db = firestore.client()

from score import *


class Match:
    """
    Look over collection of unmatched ride requests to create matches based on score
    """

    def __init__(self):
        """
        performs the matching

        request_to_match: list of unmatched requests
        """
        # get requests to be matched from firebase
        docs = db.collection(u"ride-requests").stream()
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
            for j in range(i+1, request_index):
                pair_score = Score(self.requests_to_match[i], self.requests_to_match[j]).match_score()
                if pair_score != -1:
                    match_id = (self.requests_to_match[i], self.requests_to_match[j])
                    unsorted_score_dict[match_id] = pair_score
        self.sorted_score_dict = dict(sorted(unsorted_score_dict.items(), key=lambda item: item[1]))

    def create_matches(self):
        """
        intended to be helper
        :return: null
        """
        while self.sorted_score_dict:
            # get best scored item
            best_scored = next(iter(self.sorted_score_dict.items()))  # gives ((request1, request2), score) tuple
            request1_name = best_scored[0][0]
            request2_name = best_scored[0][1]

            # add to match_dict
            match_id = request1_name + request2_name
            self.match_dict[match_id] = best_scored[1]

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
    print(test.get_match_dict())
    pass


if __name__ == "__main__":
    main()
