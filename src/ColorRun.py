from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from flask import Flask, request
import nameConverter
from phue import Bridge
from scrape_colors import make_map
from rgbxy import Converter


app = Flask(__name__)
name_to_color = nameConverter.NameConverter()


@app.route('/', methods=['POST'])
def set_color():
    color_name = request.values.get('Body', None)

    if color_name == "Black":
        msg = MessagingResponse()
        msg.message("Haha... Next time, please send "
                    "a color that uses light.")
        return str(msg)

    rgb_values = name_to_color.convert(color_name)

    if rgb_values is None:
        msg = MessagingResponse()
        msg.message("I'm sorry, but I don't recognize "
                    "the color {}".format(color_name))
        return str(msg)

    (r, g, b) = rgb_values
    converter = Converter()
    [x, y] = converter.rgb_to_xy(r, g, b)
    entry.xy = (x, y)
    msg = MessagingResponse()
    msg.message("The light was changed to the "
                "color {}.".format(color_name))
    return str(msg)


if __name__ == '__main__':
    color_map = make_map('wikipedia_pages/colors.html')
    test = "."
    b = Bridge('10.76.100.161')
    b.connect()
    entry = b.lights[1]

    app.run(debug=True)
