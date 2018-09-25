from phue import Bridge, PhueException
import name_converter
from rgbxy import Converter
from name_converter import clean_name


saturation_val = 0
test_value = 0
class HueController:

    def __init__(self):
        self.bridge = None
        self.light = None
        self.name_to_color = name_converter.NameConverter()

    def connect(self):
        if self.light is not None:
            return

        self.bridge = Bridge('10.76.100.161')
        self.bridge.connect()
        self.light = self.bridge.lights[1]

    def set_color(self, color_name):
        try:
            self.connect()
        except PhueException:
            return "I'm sorry, but I cannot connect to the Hue Light." \
                   "Please try again later."

        rgb_values = self.name_to_color.convert(color_name)

        if rgb_values is None:
            return "I'm sorry, but I don't recognize " \
                   "the color {}".format(color_name)

        (r, g, b) = rgb_values
        converter = Converter()
        print(r, " ", g, " ", b)
        if r == 255 and b == 255 and g == 255:
            saturation_val = 0
            [x, y] = converter.rgb_to_xy(r, g, b)
        else:
            saturation_val = 255
            correction_value = 1.3
            r = ((r / 255) ** (1 / correction_value))
            g = ((g / 255) ** (1 / correction_value))
            b = ((b / 255) ** (1 / correction_value))
            [x, y] = converter.rgb_to_xy(r, g, b)

        try:
            self.light.xy = (x, y)
            self.light.saturation = saturation_val
            return "The light was changed to the color {}."\
                .format(clean_name(color_name))
        except PhueException:
            return "I'm sorry, but I cannot connect to the Hue Light." \
                   "Please try again later."
