from phue import Bridge
import name_converter
from rgbxy import Converter
from name_converter import clean_name

class HueController:

    def __init__(self):
        self.bridge = None
        self.light = None
        self.name_to_color = name_converter.NameConverter()

    def connect(self):
        if self.bridge is not None:
            return

        self.bridge = Bridge('10.76.100.161')
        self.bridge.connect()
        self.light = self.bridge.lights[1]

    def set_color(self, color_name):
        self.connect()

        rgb_values = self.name_to_color.convert(color_name)

        if rgb_values is None:
            return "I'm sorry, but I don't recognize " \
                   "the color {}".format(color_name)

        (r, g, b) = rgb_values
        converter = Converter()
        [x, y] = converter.rgb_to_xy(r, g, b)
        self.light.xy = (x, y)
        return "The light was changed to the color {}."\
            .format(clean_name(color_name))
