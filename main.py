from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__, static_url_path='/static')

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)
    # Start our TwiML response
    resp = MessagingResponse()
    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    else:
        resp.message("Your text was:\n{}".format(body))
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=80)
