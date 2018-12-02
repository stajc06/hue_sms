import datetime
import csv
from collections import deque
from getRedisColor import getColor

now = datetime.datetime.now()
#Writes the time, phone number, color, and response to a specified CSV file for data storage
def writeFile(file,number,color,response):
    with open(file, mode='a') as data:
        data_writer = csv.writer(data, quoting=csv.QUOTE_ALL)
        data_writer.writerow([now, number,color,response])
        data.close()

#Returns a list of the most recent colors the Hue Light changed to up to a total of 5 colors
def mostRecentColors(file):
    colors = []
    try:
        with open(file,'r') as data:
            lastFive = deque(csv.reader(data),5)
        for i in lastFive:
            colors.append(i[2])
        return colors
    except FileNotFoundError:
        colors = []
        return colors
#Returns a dictionary of colors paired with the number of times each color has been sent to the Hue Light
def numOfEachColor(file):
    colorsDict = {}
    try:
        with open(file,'r') as data:
            data_reader = csv.reader(data)
            for row in data_reader:
                key = row[2]
                if key in colorsDict:
                    colorsDict[key] += 1
                else:
                    colorsDict[key] = 1
        return colorsDict
    except FileNotFoundError:
        return colorsDict

def invalidColors(file):
    invalidList = []
    try:
        with open(file,'r') as data:
            data_reader = csv.reader(data)
            for row in data_reader:
                if getColor(row[2]) is None:
                    invalidList.append(row[2])
        return invalidList

    except FileNotFoundError:
        return invalidList
def colorPercent(file,color):
    try:
        colors = numOfEachColor(file)
        totalCalls = sum(colors.values())
        if(colors.get(color) != None):
            percent = colors.get(color) / totalCalls * 100
        else:
            percent = 1/totalCalls*100
        return percent
    except FileNotFoundError:
        return 0
def firstEntryDate(file):
    try:
        with open(file,'r') as data:
            data_reader = csv.reader(data)
            rowOne = next(data_reader)
            firstDate = rowOne[0]
            return firstDate[0:10]
    except FileNotFoundError:
        return ""