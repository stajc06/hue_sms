import datetime
import csv


now = datetime.datetime.now()

def writeFile(number,message,response):
    with open("data.csv", mode='a') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        data_writer.writerow([now, number,message,response])
        data.close()
