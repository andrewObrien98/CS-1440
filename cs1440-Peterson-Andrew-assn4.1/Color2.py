from Gradient import Gradient
import colour


class Color2(Gradient):
    def __int__(self, numColors):
        self.colorList = []
        self.colorList.append(colour.Color("magneta").range_to(colour.Color("black"), numColors))

    def getColor(self, number):
        return self.colorList[number]