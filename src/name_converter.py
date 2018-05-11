import string
import os


class NameConverter:

    def __init__(self):
        self.color_map = {}

        location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        with open(location + '/colors.csv') as colors:
            for line in colors:
                line = line.strip()
                (name, r, g, b) = line.split(',')

                name = self.clean_name(name)
                self.color_map[name] = (int(r), int(g), int(b))

    def clean_name(self, name):
        name = name.lower()
        name = name.strip()
        name = name.replace('\'', '')
        name = name.replace('-', ' ')
        return name.translate(str.maketrans("","", string.punctuation))

    def convert(self, color):
        key_name = self.clean_name(color)
        return self.color_map.get(key_name, None)
