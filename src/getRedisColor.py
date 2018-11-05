import redis
from name_converter import clean_name

def getColor(colorName):
    r = redis.Redis(
        host='localhost', port=6379, db=0)

    value = r.hget("colors", clean_name(str(colorName)))
    return value
