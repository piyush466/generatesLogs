class Vehicle:

    def __init__(self):
        self.bike = "TVS"
        self.__four= "duster"

    def getbike(self):
        return self.bike

    def getfour(self):
        return self.__four

    def setfourr(self,newfours):
        self.__four = newfours

v = Vehicle()
v.bike = "honda"
print(v.getbike())
# v.__four = "car"
# print(v.getfour())

v.setfourr("verna")
print(v.getfour())
