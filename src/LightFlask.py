from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def __init__():
    if request.method == 'GET':
        response = MessagingResponse()
        message = Message()
        message.body('Congratulations, you used GET')
        response.append(message)
        response.redirect("http://127.0.0.1:4040/api")

        print(response)

    if request.method == 'POST':
        body = request.values.get('Body', None)

        print(body)

        sendMessage = "You sent the message: " + body

        response = MessagingResponse()
        response.message(sendMessage)

        # message = Message()
        # message.body('This is a light test')
        # response.append(message)
        # response.redirect("http://127.0.0.1:4040/api")

        # print(response)

        return str(response)


if __name__ == '__main__':
    app.run(debug=True)
