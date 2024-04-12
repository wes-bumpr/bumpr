import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
from email.message import EmailMessage

# Set up Firebase credentials
cred = credentials.Certificate("bumpr-firebase-service-acckey.json") #TODO: check key
firebase_admin.initialize_app(cred)
db = firestore.client()
# Get a reference to the carpool data
# carpool_ref = db.reference('/matches')
# Set up email credentials
email_address = 'wesbumpr@gmail.com'
email_password = 'seku lfis hbpi prao' # https://myaccount.google.com/u/3/apppasswords
#'wesbumpr@2001' - email pwd

def get_user_info(user_id):
    doc_ref = db.collection('users').document(user_id)
    return doc_ref.get().to_dict()

def get_user_email(user_id):
    doc_ref = db.collection('users').document(user_id)
    user_info = doc_ref.get().to_dict()
    user_email = user_info['email']
    return user_email

def get_user_name(user_id):
    doc_ref = db.collection('users').document(user_id)
    user_info = doc_ref.get().to_dict()
    user_name = user_info['name']
    return user_name

def get_ride_request_info(ride_request_id):
    doc_ref = db.collection('ride-requests').document(ride_request_id)
    return doc_ref.get().to_dict()

def send_email_notification(match):
    # Parse Match dictionary -- as found in firebase.
    # for user1_ID, user2_ID in match['users']:
    user1_ID, user2_ID = match['users']
    # ride_request_info = get_ride_request_info(ride_request)
    # user_info = get_user_info(ride_request_info['user_ID'])
    user1_email = get_user_email(user1_ID)
    user2_email = get_user_email(user2_ID)
    user1_name = get_user_name(user1_ID)
    user2_name = get_user_name(user2_ID)
    # other_riders_names = [get_user_info(get_ride_request_info(ride_req)['user_ID'])['name'] for ride_req in list(filter(lambda x: x != ride_request, match['ride_request_ID']))]
    # Set up email message
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['Subject'] = 'Carpool Match Found!'
    # greeting = 'Hi {},\n'.format(user_info['name'])
    greeting = 'Hi {},\n'.format(user1_name)
    msg.attach(MIMEText(greeting, 'plain'))
    body1 = 'A carpool match has been found!\n\nDetails:\nFrom: {}\nTo: {}\nDate: {}\n'.format(
        match['origin'], match['to'], match['depart_time'])
    msg.attach(MIMEText(body1, 'plain'))
    # body2 = 'Your fellow carpoolers are: ' + ", ".join(other_riders_names) + '.\n'
    body2 = 'Your fellow carpooler is: ' + user1_name + " " + user2_name + \
            "\nEmails: " + user1_email + " " + user2_email
    msg.attach(MIMEText(body2, 'plain'))
    # body3 = 'Currently there are: {} passengers out of {} seats.\n'.format(
    #     match['numRiders'], match['maxSpace'])
    # msg.attach(MIMEText(body3, 'plain'))
    closing = "Enjoy your ride!\nBUMPR Team"
    msg.attach(MIMEText(closing, 'plain'))
    recipients = [user1_email, user2_email]
    for recipient in recipients:
        msg['To'] = recipient
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # context = ssl.create_default_context()
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        # server.starttls()
        server.login(email_address, email_password) # ask ashley
        server.sendmail(email_address, recipient, msg.as_string())
        server.quit()

# carpool_ref.listen(send_email_notification)
def main():
    matchEX = db.collection('matches').document('EjDOXx3H9yUFLmwz25DDVc1FkPEq9BDSApUHLYEV').get().to_dict()
    send_email_notification(matchEX)

main()
