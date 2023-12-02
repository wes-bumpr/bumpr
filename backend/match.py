from score import Score
# from handle_requests import delete_Item_FromFirebase  # TODO: modified but not tested. Test if working
from get_request import db, GetRequest
from datetime import datetime
from get_userinfo import GetUserInfo


def add_match_info(request1_id, request2_id):
    """
    Given request1 id and request2 id,
    build the dictionary with the match information --> which will
    be the value for a match key in the match_dict dictionary.
    Dictionary consists of: list of users, list of origins and destinations, and earliest depart time.
    :param request1_id: string representing the first matched request ID
    :param request2_id: string representing the first matched request ID
    :return: dictionary representing the information of a match

    ex. {'users': ['C10004321', 'C10004500'], 'origin': 
    ['Wellesley College', '"21 Wellesley College"'], 'to': 
    ['700 Atlantic Ave, Boston, MA 02110, United States', '"21 Wellesley College"'], 
    'depart_time': '12/30/2030, 12:00:00 AM', 'request_ids': ['EjDOXx3H9yUFLmwz25DD', 
    'Vc1FkPEq9BDSApUHLYEV']}
    """
    request1 = GetRequest(request1_id)
    request2 = GetRequest(request2_id)
    request_ids = [request1_id, request2_id]
    origin = [request1.get_origin_address(), request2.get_destination_address()]
    to = [request1.get_destination_address(), request2.get_destination_address()]
    date_format = "%m/%d/%Y, %I:%M:%S %p"
    request1_depart_time = datetime.strptime(request1.get_depart_time(), date_format)
    request2_depart_time = datetime.strptime(request2.get_depart_time(), date_format)
    if request1_depart_time < request2_depart_time:
        depart_time = request1.get_depart_time()
    else:
        depart_time = request2.get_depart_time()
    # get user emails and phone numbers to display when there is a match
    users = [request1.get_user_id(),
             request2.get_user_id()]  # users that made the requests (note: a request may have more than 1 rider)
    #TODO: clean the db with correct user ids in requests info to give email and name info to frontend when match info is displayed
    # user_id1 = request1.get_user_id()
    # user_id2 = request2.get_user_id()
    # user1 = GetUserInfo(user_id1)
    # user2 = GetUserInfo(user_id2)
    # user_email1 = user1.get_email()
    # user_email2 = user2.get_email()
    # user_emails = [user_email1, user_email2]
    # user_name1 = user1.get_name()
    # user_name2 = user2.get_name()
    # users = [user_name1, user_name2]
    return {"users": users,"origin": origin, "to": to, "depart_time": depart_time, "request_ids": request_ids}
    # return {"users": users, "user_emails": user_emails,"origin": origin, "to": to, "depart_time": depart_time, "request_ids": request_ids}


def delete_expired_requests():
    """
    Intended to be a helper function.
    Identifies any expired ride requests, deletes them from Firebase,
    and notifies the user.
    """
    docs = db.collection(u"ride-requests-test").stream()

    to_be_deleted_requests_docid = []
    date_format = "%m/%d/%Y, %I:%M:%S %p"
    current_time = datetime.now().timestamp()  # current time in seconds
    print("current time: ", str(current_time))
    for doc in docs:
        request = GetRequest(doc.id)
        request_depart_time = datetime.strptime(request.get_depart_time(), date_format)
        print(f'depart time for request {doc.id}: {request_depart_time}')

        # current time is past the request’s depart time (way past their depart time)
        if current_time > request_depart_time.timestamp():
            # print("expired time: ", str(request_depart_time))
            to_be_deleted_requests_docid.append(doc.id)
            doc_ref = db.collection("ride-requests-test").document(doc.id)
            doc_ref.delete()
    print("requests to be deleted: ", to_be_deleted_requests_docid)
    # TODO: let users know that their ride request was deleted AND if their request was matched using the list


class Match:
    """
    This class handles the process of matching requests
    """
    def __init__(self):
        """
        performs the matching.
        1. Clean the database and delete expired requests
        2. Get requests and score each pair of requests.
           Score of -1 is a fail to match. Lower score is a better match.
        3. Rank scores and save them as successful matches

        request_to_match: list of unmatched requests
        """
        # check and delete expired requests prior to making matches
        delete_expired_requests()

        self.docs = db.collection(u"ride-requests-test").stream()

        # get requests to be matched from firebase
        self.requests_to_match = []
        for doc in self.docs:
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
        # print(self.match_dict)

    def get_match_dict(self):
        """
        getter for match dict
        :return: dictionary of successful matches
        """
        return self.match_dict

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

    def create_matches(self):
        """
        intended to be helper
        :return: null
        """
        while self.sorted_score_dict:
            # get best scored item
            best_scored = next(iter(self.sorted_score_dict.items()))  # gives ((request1, request2), score) tuple
            request1_name = best_scored[0][0]  # request id
            request2_name = best_scored[0][1]

            # add to match_dict
            match_id = request1_name + request2_name
            match_info = add_match_info(request1_name, request2_name)
            self.match_dict[match_id] = match_info  # best_scored[1]

            # remove other pairs of matches with either request1 or request2
            sorted_score_dict_original = self.sorted_score_dict.copy()
            for key in sorted_score_dict_original:
                if request1_name in key or request2_name in key:
                    del self.sorted_score_dict[key]


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
    # delete_expired_requests()


if __name__ == "__main__":
    main()