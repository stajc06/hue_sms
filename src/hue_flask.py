from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from hue_controller import HueController
from name_converter import clean_name

app = Flask(__name__)
controller = HueController()


@app.route('/', methods=['POST'])
def set_color():
    color_name = request.values.get('Body', None)
    color_name = clean_name(color_name)

    if color_name == "black":
        response = MessagingResponse()
        response.message("Haha... please use a color that contains light.")
        return str(response)

    message = controller.set_color(color_name)
    response = MessagingResponse()
    response.message(message)
    return str(response)


if __name__ == '__main__':
    app.run()
