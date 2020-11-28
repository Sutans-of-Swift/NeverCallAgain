import subprocess
import base64
from flask import Flask, request, redirect, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__, static_url_path='')


@app.route("/audio/<path:path>")
def send_audio_files(path):
    """Sends the audio files out"""
    return send_from_directory("audio", path)


@app.route("/twiml/<path:path>")
def send_twiml_files(path):
    """Sends the XML files out"""
    return send_from_directory("twiml", path)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)
    # Encode body as base64 for safe transport as argument.
    b64_body = base64.urlsafe_b64encode(body.encode("utf-8"))
    # Spawn Sam's module to do work on the message.
    subprocess.run(["python3", "call.py", b64_body])
    # Start our TwiML response to be sent as a SMS
    resp = MessagingResponse()
    resp.message("Your message was:\n{}".format(body))
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=80)
