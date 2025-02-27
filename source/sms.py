from twilio.rest import Client
from dotenv import load_dotenv
import os


def config():
    load_dotenv()


def main(message):
    config()
    sid=os.getenv('SID')
    account_sid = sid
    token=os.getenv("TOKEN")
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages.create(body=message,from_='+13525081703',to='+919578814692')

    print(message.sid)


