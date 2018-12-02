from hue_controller import HueController
from name_converter import clean_name
from data_writer import writeFile,colorPercent,firstEntryDate
controller = HueController()
file = "data.csv"

def go():
    test = "."
    while (test != ""):
        test = input("Please enter a color: ")
        color_name = clean_name(test)
        print(test)
        if color_name == "black":
            print("No black")
        else:
            percent = colorPercent(file, color_name)
            message = controller.set_color(color_name)
            date = firstEntryDate(file)
            writeFile(file,"856-938-4220", str(color_name), str(message))
            print(message +" This entry has been chosen " + str(percent) + "% of the time since " + date + "!"
)


if __name__ == '__main__':
    go()