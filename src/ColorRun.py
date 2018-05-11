from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from hue_controller import HueController

app = Flask(__name__)
controller = HueController()


@app.route('/', methods=['POST'])
def set_color():
    color_name = request.values.get('Body', None)

    if color_name == "Black":
        response = MessagingResponse()
        response.message("Haha... Next time, please send "
                    "a color that uses light.")
        return str(response)

    message = controller.set_color(color_name)
    response = MessagingResponse()
    response.message(message)
    return str(response)


if __name__ == '__main__':
    app.run()
