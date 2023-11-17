# Carpooling website API for handling user & ride data
# sample code for a carpooling API with Firebase and Flask in MODULARS

from flask import Flask
from user_auth_module import user_auth_api
from ride_share_module import ride_share_api
from payment_module import payment_api
from notification_module import notification_api

app = Flask(__name__)

# Register the API modules
app.register_blueprint(user_auth_api, url_prefix='/api/user-auth')
app.register_blueprint(ride_share_api, url_prefix='/api/ride-share')
app.register_blueprint(payment_api, url_prefix='/api/payment')
app.register_blueprint(notification_api, url_prefix='/api/notification')

if __name__ == '__main__':
    app.run()


