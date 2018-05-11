from phue import Bridge
import nameConverter
from rgbxy import Converter


class HueController:

    def __init__(self):
        self.b = None
        self.entry = None
        self.name_to_color = nameConverter.NameConverter()

    def connect(self):
        if self.b is not None:
            return

        self.b = Bridge('10.76.100.161')
        self.b.connect()
        self.entry = self.b.lights[1]

    def set_color(self, color_name):
        self.connect()

        rgb_values = self.name_to_color.convert(color_name)

        if rgb_values is None:
            return "I'm sorry, but I don't recognize " \
                   "the color {}".format(color_name)

        (r, g, b) = rgb_values
        converter = Converter()
        [x, y] = converter.rgb_to_xy(r, g, b)
        self.entry.xy = (x, y)
        return "The light was changed to the color {}.".format(color_name)
        return str(msg)
