import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up Firebase credentials
cred = credentials.Certificate("bumpr-firebase-service-acckey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Get a reference to the carpool data
# carpool_ref = db.reference('/matches')

# Set up email credentials
email_address = 'email@gmail.com'
email_password = 'password'

def get_user_info(user_id):
    doc_ref = db.collection('users').document(user_id)
    return doc_ref.get().to_dict()
    
def get_ride_request_info(ride_request_id):
    doc_ref = db.collection('ride-requests').document(ride_request_id)
    return doc_ref.get().to_dict()
    
def send_email_notification(match):
    # Parse Match dictionary -- as found in firebase.
    
    for ride_request in match['ride_request_ID']:
        ride_request_info = get_ride_request_info(ride_request)
        user_info = get_user_info(ride_request_info['user_ID'])
        
        other_riders_names = [get_user_info(get_ride_request_info(ride_req)['user_ID'])['name'] for ride_req in list(filter(lambda x: x != ride_request, match['ride_request_ID']))]
        # Set up email message
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['Subject'] = 'Carpool Match Found!'
        greeting = 'Hi {},\n'.format(user_info['name'])
        msg.attach(MIMEText(greeting, 'plain'))
        
        body1 = 'A carpool match has been found!\n\nDetails:\nFrom: {}\nTo: {}\nDate: {}\nTime: {}\n'.format(
                match['from'], match['to'], match['date'], match['departure_time'])
        msg.attach(MIMEText(body1, 'plain'))
        
        body2 = 'Your fellow carpoolers are: ' + ", ".join(other_riders_names) + '.\n'
        msg.attach(MIMEText(body2, 'plain'))
        
        body3 = 'Currently there are: {} passengers out of {} seats.\n'.format(
            match['numRiders'], match['maxSpace'])
        msg.attach(MIMEText(body3, 'plain'))

        closing = "Enjoy your ride!\nBUMPR Team"
        msg.attach(MIMEText(closing, 'plain'))
        
        recipients = [user_info['email']]
        for recipient in recipients:
            msg['To'] = recipient
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, recipient, msg.as_string())
            server.quit()

# carpool_ref.listen(send_email_notification)

def main():
    matchEX = db.collection('matches').document('117xZgdfXAr6OacBN8lc').get().to_dict()
    send_email_notification(matchEX)
    
main()
