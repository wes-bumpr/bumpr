
# Create a Match Class, where we match people based on the information we get
# from the data that Ride Request API (ex. sampledata-rider.json) imports (put into) into Firebase

# run an instance of a match for each user that is not matched yet
# TODO: need a list of all users that requested rides from Firebase

class Match:
    def __init__(self, currUserID):
        self.userID = currUserID # import a user from Firebase
        self.priorityQueue = []
        # user_list = get from firebase


    # function to match people based on priority queue
    def match_users():
        # using the priority queue, match people with this current user
        # based on cost and car capacity (if driver)

    # helper function: create a priority queue (using compareTo() method) for this current user
    # note: each user has their own priority queue
    def compareTo():
        # compare based on 
            # 1. start/end locations & depart time
            # create queue (make sure not to match driver with driver - skip over that user)