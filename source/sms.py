from twilio.rest import Client
from dotenv import load_dotenv
import os


def config():
    load_dotenv


def main():
    config()
    sid=os.getenv('STD')
    account_sid = sid
    token=os.getenv("TOKEN")
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages.create(body='Hello, this from twilio',from_='+13525081703',to='+919578814692')

    print(message.sid)


main()