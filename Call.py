gimport xml.etree.cElementTree as ET
import uuid
import datetime
import os
from twilio.rest import Client



def Call(phonenumber,Filename):
    #create XML file
    
    Response = ET.Element("Response")
    ET.SubElement(Response, "Play").text = 'http://nevercallagain.frost.cx/audio/'+Filename+'.mp3'

    tree = ET.ElementTree(Response)
    tree.write(Filename + ".xml")
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url='http://nevercallagain.frost.cx/twiml/'+Filename+'.Xml',
        to = phonenumber,
        from_ = '+447411226037'
    )





