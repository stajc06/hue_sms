from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from flask import Flask, request
import nameConverter
from phue import Bridge
from scrape_colors import make_map
from rgbxy import Converter


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def __init__():
    """Creates Flask server for use in communication between Twilio and Philips Hue Light.
    No methods set up so far for GET request.  Must use POST for now.
    Takes SMS body as input.  Extracts color name from message, and calls nameConverter.py to check if input is valid"""
    if request.method == 'GET':
        response = MessagingResponse()
        message = Message()


    if request.method == 'POST':
        body = request.values.get('Body', None)

        print(body)
        inputValue = body
        inputValue = nameConverter.convert(inputValue)

        if(inputValue == "None"):
            sendMessage = "I'm sorry, but I don't recognize the color " + body + "."

        else:
            if not entry.on:
                entry.on = True
            if inputValue == "Black":
                sendMessage = "Haha... Next time, please send a color which uses light."
            else:
                rgb_color = color_map[inputValue]
                print(rgb_color)
                r = rgb_color['r']
                g = rgb_color['g']
                b = rgb_color['b']
                converter = Converter()
                [x, y] = converter.rgb_to_xy(r, g, b)
                print(x, y)
                entry.xy = (x, y)
                sendMessage = "The light was changed to the color " + body + "."

        response = MessagingResponse()
        response.message(sendMessage)

        return str(response)


if __name__ == '__main__':
    color_map = make_map('wikipedia_pages/colors.html')
    test = "."
    b = Bridge('10.76.100.161')
    b.connect()
    entry = b.lights[1]

    app.run(debug=True)
