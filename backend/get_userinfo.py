

# TODO: db initialization could be put into a “main” eventually
from get_request import db


class GetUserInfo:
    """
    User objects retrieved from database
    """

    def __init__(self, user_doc_id):
        # get user doc from users collection from Firebase
        self.user_ref = db.collection(u"users").document(user_doc_id)
        # convert one user data from users collection to dictionary for each access
        self.user_doc = self.user_ref.get().to_dict()

    def get_name(self):
        """
        Returns name in string
        """
        return self.user_doc["name"]

    def get_email(self):
        """
        Returns email in string
        """
        return self.user_doc["email"]

    def get_phone_number(self):
        """
        Returns phone number in string
        """
        return self.user_doc["phone_number"]


def main():
    # testing purposes
    user = GetUserInfo("C10001050")
    print(user.get_email())
    print(user.get_name())
    print(user.get_phone_number())



if __name__ == "__main__":
    main()
