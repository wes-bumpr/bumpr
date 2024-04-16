import base64
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import pickle

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_email(sender, to, subject, message_text, credentials):
    service = build('gmail', 'v1', credentials=credentials)
    message = create_message(sender, to, subject, message_text)
    send_message(service, 'me', message)

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except Exception as e:
        print('An error occurred: %s' % e)

def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def main():
    sender_email = 'wesbumpr@gmail.com'
    receiver_email = 'dc103@wellesley.edu'
    subject = 'bumpr test'
    body = 'Body of the Email'

    credentials = credentials.Certificate("bumpr-firebase-service-acckey.json") #get_credentials()
    send_email(sender_email, receiver_email, subject, body, credentials)

if __name__ == "__main__":
    main()
