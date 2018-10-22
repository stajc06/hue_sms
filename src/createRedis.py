import redis
import os
from name_converter import clean_name

def go():

    r = redis.Redis(
        host='localhost', port=6379, db=0)


    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(location + '/colors.csv') as colors:
        for line in colors:
            line = line.strip()
            (name, red, green, blue) = line.split(',')

            name = clean_name(name)
            inputVal = str(red + "," + green + "," + blue)
            print("name: ", name, "inputVal: ", inputVal)
            r.set(str(name), str(inputVal))


if __name__ == '__main__':
    go()
