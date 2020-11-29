import subprocess
import base64
from flask import Flask, request, redirect, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Record

app = Flask(__name__, static_url_path='')


@app.route("/audio/<path:path>", methods=['GET', 'POST'])
def send_audio_files(path):
    """Sends the audio files out"""
    return send_from_directory("audio", path)


@app.route("/twiml/<path:path>", methods=['GET', 'POST'])
def send_twiml_files(path):
    """Sends the XML files out"""
    return send_from_directory("twiml", path)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    incoming_number = request.values.get('From', None)
    #print(body)
    # Encode body as base64 for safe transport as argument.
    b64_body = base64.urlsafe_b64encode(body.encode("utf-8"))
    # Spawn other program to do work on the message.
    subprocess.run(["python3", "call.py", b64_body])
    # Start our TwiML response to be sent as a SMS
    resp = MessagingResponse()
    resp.message("Your message was:\n{}".format(body))
    return str(resp)


@app.route("/receiver", methods=['GET', 'POST'])
def receiver():
    """Parses the transcript and texts it to the original sender."""
    reponse = VoiceResponse()
    print(reponse)
    return "A response."


if __name__ == "__main__":
    app.run(debug=True, port=80)
