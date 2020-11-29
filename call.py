import xml.etree.cElementTree as ET
import os
from twilio.rest import Client
# polyInstance Requirements
from boto3 import Session
import hashlib
import time
# Body string getting from other program.
import sys
import base64


class pollyInstance():

    def __init__(self, text):
        # need to strip the number here :)
        self._number, self._text = self.deriveNumberAndMessage(text)
        # md5 of message body
        self._filename = self.deriveName(text)
        # Create a client using the credentials and region defined in the [adminuser]
        # section of the AWS credentials file (~/.aws/credentials).
        self._session = Session(profile_name="sultan")
        self._polly_client = self._session.client("polly")

    def getNumber(self):
        return self._number

    def getFileName(self):
        return self._filename

    def parseResponse(self):
        """performs the call to the polly client and writes the output to file.
        """
        response = self._polly_client.synthesize_speech(VoiceId='Geraint',
                                                        OutputFormat='mp3',
                                                        Text=self._text)

        filename = (self._filename + '.mp3')
        file = open("audio/"+filename, 'wb')
        file.write(response['AudioStream'].read())
        file.close()

    def deriveNumberAndMessage(self, text):
        """tentative instance assumes that the first line will end with '\n'"""
        inter = text.split("\n")
        message = ""
        number = inter[0]
        for i in range(1, len(inter)):
            message += inter[i]
        return number, message

    def deriveName(self, text):
        to_be_hashed = text + str(time.time_ns())
        hasher = hashlib.md5()
        hasher.update(to_be_hashed.encode("utf-8"))
        result_str = hasher.digest()
        return result_str.hex()


def call(phonenumber,filename):
    #Create XML file with audiofile to allow for the call to access 
    Response = ET.Element("Response")
    ET.SubElement(Response, "Play").text = 'http://nevercallagain.frost.cx/audio/'+filename+'.mp3'

    ET.SubElement(Response, "Record", maxLength="10", finishOnKey="*",
    transcribeCallback="http://nevercallagain.frost.cx/receiver")

    tree = ET.ElementTree(Response)
    tree.write("twiml/"+filename + ".xml")
    
    #getting twilio authorisation
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    #make the call using phonenumber and audio

    call = client.calls.create(
        url='http://nevercallagain.frost.cx/twiml/'+filename+'.xml',
        to = phonenumber,
        from_ = '+447411226037'
    )


body = str(base64.urlsafe_b64decode(sys.argv[1]), "utf-8")
polly = pollyInstance(body)
polly.parseResponse()
call(polly.getNumber(), polly.getFileName())
