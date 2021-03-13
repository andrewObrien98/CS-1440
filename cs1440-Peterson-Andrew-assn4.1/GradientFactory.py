from Color1 import Color1
from Color2 import Color2
from Color3 import Color3

class GradientFactory():
    def __init__(self):
        self.__colorDicitonary = []

    def makeGradient(self,numColors, name = "Color1"):
        if name == "Color1":
            return Color1(numColors)

        elif name == "Color2":
            return Color2(numColors)

        elif name == "Color3":
            return Color3(numColors)
