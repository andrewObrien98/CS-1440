from Gradient import Gradient
import colour

colors = {
    "red" : colour.Color("red"),
    "blue" : colour.Color("blue"),
    "myCol" : colour.Color("#009EA3")
}

class Color1(Gradient):
    def __init__(self, numColors):
        self.numColors = numColors
        self.colorList = []
        self.colorList.append(colour.Color("red").range_to(colour.Color("blue"), numColors))

    def getColor(self, number):