from redis import Redis
from name_converter import clean_name

class colorsRedis:

    def __init__(self):
        self.connect()

    def connect(self):
        self.db = Redis('localhost', 6379)

    def numColors(self):
        return len(self.db.hgetall("colors"))

    def register_color(self, colorName, r, g, b):
        key = clean_name(colorName)
        value = str(r + "," + g + "," + b)
        self.db.hset("colors", key, value)

    def is_color(self, colorName):
        key = clean_name(colorName)
        return self.db.hexists("colors", key)
