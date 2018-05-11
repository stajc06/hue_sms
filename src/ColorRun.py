from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from flask import Flask, request
import nameConverter
from phue import Bridge
from scrape_colors import make_map
from rgbxy import Converter


app = Flask(__name__)
name_to_color = nameConverter.NameConverter()


@app.route('/', methods=['POST'])
def __init__():
    input_value = request.values.get('Body', None)

    input_value = name_to_color.convert(input_value)

    if input_value == "None":
        send_message = "I'm sorry, but I don't recognize the color " + \
                      input_value + "."

    else:
        if not entry.on:
            entry.on = True
        if input_value == "Black":
            send_message = "Haha... Next time, please send a color that uses light."
        else:
            rgb_color = color_map[input_value]
            r = rgb_color['r']
            g = rgb_color['g']
            b = rgb_color['b']
            converter = Converter()
            [x, y] = converter.rgb_to_xy(r, g, b)
            entry.xy = (x, y)
            send_message = "The light was changed to the color " + input_value + "."

    response = MessagingResponse()
    response.message(send_message)

    return str(response)


if __name__ == '__main__':
    color_map = make_map('wikipedia_pages/colors.html')
    test = "."
    b = Bridge('10.76.100.161')
    b.connect()
    entry = b.lights[1]

    app.run(debug=True)
