from scrape_colors import make_map

value = ""


def convert(inputValue):
    """Function used to check if SMS message's body is valid input

    Parameters:
    ---------------
        inputValue: String
            SMS message's body, checked to see if valid color"""

    value = inputValue.lower()
    color_map = make_map('wikipedia_pages/colors.html')
    for entry in color_map:
        if value == entry.lower():
            return entry
    if value == "Blue".lower():
        return "Blue (I)"
    elif value == "Violet".lower():
        return "Violet (I)"
    elif value == "Lavender".lower():
        return "Lavender (I)"
    elif value == "Gold".lower():
        return "Gold (I)"
    elif value == "Pink".lower():
        return "Pink Flamingo"
    elif value == "Violet".lower():
        return "Violet (I)"
    elif value == "Purple".lower():
        return "Violet (II)"

    else:
        return "None"
