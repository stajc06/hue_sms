
from phue import Bridge
from scrape_colors import make_map
from rgbxy import Converter


def go():
    color_map = make_map('wikipedia_pages/colors.html')

    rgb_color = color_map['Green']
    print(rgb_color)

    r = rgb_color['r']
    g = rgb_color['g']
    b = rgb_color['b']

    converter = Converter()
    [x, y] = converter.rgb_to_xy(r, g, b)
    print(x, y)

    #b = Bridge('10.0.1.2')
    b = Bridge('10.76.100.161')

    b.connect()

    entry = b.lights[1]

    entry.xy = (x, y)


if __name__ == '__main__':
    go()

