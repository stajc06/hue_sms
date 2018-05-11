import string


class NameConverter:

    def __init__(self):
        self.color_map = {}

        with open('colors.csv') as colors:
            for line in colors:
                line = line.strip()
                (name, r, g, b) = line.split(',')

                name = self.clean_name(name)
                self.color_map[name] = (int(r), int(g), int(b))

    def clean_name(self, name):
        name = name.strip()
        name = name.replace('\'', '')
        name = name.replace('-', ' ')
        return name.translate(string.punctuation)

    def convert(self, color):
        return self.color_map.get(color, None)
