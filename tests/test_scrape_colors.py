
from scrape_colors import make_map


def assert_color_equals(color_input, expected_r, expected_g, expected_b):
    color = colors.get(color_input)
    r = color['r']
    g = color['g']
    b = color['b']

    assert (r, g, b) == (expected_r, expected_g, expected_b)


def test_color_load():

    global colors

    colors = make_map('src/wikipedia_pages/colors.html')

    # First color in table
    assert_color_equals('Red', 237, 10, 63)

    # Two in middle of table
    assert_color_equals('Lemon Yellow', 255, 255, 159)
    assert_color_equals('Violet (II)', 131, 89, 163)

    # Last color in table
    assert_color_equals('White', 255, 255, 255)

