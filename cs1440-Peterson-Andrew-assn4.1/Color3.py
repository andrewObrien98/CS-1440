from Gradient import Gradient
import colour


class Color3(Gradient):
    def __int__(self, numColors):
        self.colorList = []
        self.colorList.append(colour.Color("green").range_to(colour.Color("cyan"), numColors))

    def getColor(self, number):
        return self.colorList[number]