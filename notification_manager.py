import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class NotificationManager():

    def send_alert_message(self, cheapest_price, destination_city, departure_date, destination_date):
        account_sid = os.getenv('ACCOUNT_SID')
        auth_token = os.getenv('AUTH_TOKEN')

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Low price alert! Only ${cheapest_price} to fly from \n"
                 f"Toronto-YYZ to {destination_city}, from {destination_date} to {destination_date}",
            from_='+18782066486',
            to='+14372889397'
        )
        print(message.sid)
