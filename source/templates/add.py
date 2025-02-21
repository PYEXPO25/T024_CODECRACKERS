from twilio.rest import Client
import os
from dotenv import find_dotenv,load_dotenv


dotenv_path=find_dotenv()
load_dotenv(dotenv_path)


sid=os.getenv("SID")
token=os.getenv("TOKEN")

ct=Client(sid,token)

ct.messages.create(body="helo",from_="+13525081703",to='+91 9976775385')