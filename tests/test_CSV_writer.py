import csv,unittest,os
from csv_writer import writeFile,mostRecentColors,numOfEachColor,invalidColors
from hue_controller import HueController

controller = HueController()
filename = "testdata.csv"
red_message = controller.set_color("red")
blue_message = controller.set_color("blue")
green_message = controller.set_color("green")
white_message = controller.set_color("white")
yellow_message = controller.set_color("yellow")
foo_message = controller.set_color("foo")
class csvTest(unittest.TestCase):
    def testWriteFile(self):

        writeFile(filename,"856-938-4220","red",red_message)
        writeFile(filename,"856-938-4220","blue",blue_message)

        with open(filename) as data:
            data_reader = csv.reader(data)
            num = []
            for row in data_reader:
                num.append(row)
        self.assertEqual(len(num),2)
        os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests",filename))

    def testListMostRecent(self):
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "green", green_message)
        writeFile(filename, "856-938-4220", "yellow", yellow_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "white", white_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        expectedColors = ["yellow","blue","red","white","blue"]
        self.assertListEqual(expectedColors,mostRecentColors(filename))
        os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))

    def testListMostRecentSmallFile(self):
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "green", green_message)
        expectedColors = ["red","blue","green"]
        self.assertListEqual(expectedColors,mostRecentColors(filename))
        os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))

    def testListMostRecentEmptyFile(self):
        expectedColors = []
        self.assertListEqual(expectedColors,mostRecentColors(filename))
        try:
            os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))
        except FileNotFoundError:
            return

    def testNumOfColors(self):
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "green", green_message)
        writeFile(filename, "856-938-4220", "yellow", yellow_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "white", white_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "green", green_message)
        writeFile(filename, "856-938-4220", "yellow", yellow_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "white", white_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        colorsNumber = numOfEachColor(filename)
        self.assertEqual(colorsNumber["red"],4)
        self.assertEqual(colorsNumber["blue"],6)
        self.assertEqual(colorsNumber["green"],2)
        self.assertEqual(colorsNumber["yellow"],2)
        os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))
    def testNumOfColorsEmptyFile(self):
        colorsNumber = numOfEachColor(filename)
        self.assertEqual(len(colorsNumber),0)
        try:
            os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))
        except FileNotFoundError:
            return
    def testNumberOfInvalidColors(self):
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "foo", foo_message)
        writeFile(filename, "856-938-4220", "foo", foo_message)
        writeFile(filename, "856-938-4220", "green", green_message)
        invalidList = invalidColors(filename)
        self.assertEquals(invalidList[0],"foo")
        self.assertEqual(len(invalidList),2)
        os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))
    def testNumberOfInvalidColorsAllValid(self):
        writeFile(filename, "856-938-4220", "red", red_message)
        writeFile(filename, "856-938-4220", "blue", blue_message)
        writeFile(filename, "856-938-4220", "green", green_message)
        invalidList = invalidColors(filename)
        self.assertEqual(len(invalidList),0)
        os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))

    def testNumberOfInvalidColorsEmptyFile(self):
        invalidList = invalidColors(filename)
        self.assertEqual(len(invalidList),0)
        try:
            os.remove(os.path.join("/Users/johnpolich/Desktop/hue_sms/tests", filename))
        except FileNotFoundError:
            return
if __name__ == '__main__':
    unittest.main()
