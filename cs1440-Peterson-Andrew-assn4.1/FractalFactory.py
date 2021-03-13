import sys
# Import other fractals here
from Mandelbrot import Mandelbrot
from Julia import Julia


class FractalFactory():
    def __init__(self):
        self.centerX = 0
        self.centerY = 0
        self.axisLength = 0
        self.pixels = 0
        self.iterations = 0
        self.type = ""
        self.fractalInfo = ""

        self.__coorDic = {"centerX": "w",
                          "centerY": "w",
                          "axisLength": "w",
                          "pixels": "w",
                          "iteration": "w",
                          "type": "w"
                          }

    def makeFractal(self, fractal= "data\elephants.frac"):
        self.fractalInfo = self.extractFile(fractal)

        if self.__coorDic["type"] == "mandelbrot":
            return Mandelbrot(self.__coorDic)

        elif self.__coorDic["type"] == "julia":
            return Julia(self.__coorDic)

        elif self.__coorDic["type"] == "????":
            return print("you need to add this one")

    def extractFile(self, fractal):
        file = open(fractal)
        for line in file:
            self.check(line.lower())
        self.checkEnd()

    def check(self, line):
        if line.__contains__("centerx:"):
            try:
                self.__coorDic["centerX"] = int(line[8:])

            finally:
                raise NotImplementedError("Incorrect format in fractal configuration file")

        elif line.__contains__("centery:"):
            try:
                self.__coorDic["centerY"] = int(line[8:])

            finally:
                raise NotImplementedError("Incorrect format in fractal configuration file")

        elif line.__contains__("axislength:"):
            try:
                self.__coorDic["axisLength"] = int(line[11:])

            finally:
                raise NotImplementedError("Incorrect format in fractal configuration file")

        elif line.__contains__("pixels:"):
            try:
                self.__coorDic["pixels"] = int(line[7:])

            finally:
                raise NotImplementedError("Incorrect format in fractal configuration file")

        elif line.__contains__("iterations:"):
            try:
                self.__coorDic["iterations"] = int(line[11:])

            finally:
                raise NotImplementedError("Incorrect format in fractal configuration file")

        elif line.__contains__("type:"):
            try:
                self.__coorDic["type"] = line[5:].strip(" ")

            finally:
                raise NotImplementedError("Incorrect format in fractal configuration file")

    def checkEnd(self):
        keyList = self.__coorDic.keys()
        for i in keyList:
            if self.__coorDic[i] == "w":
                raise NotImplementedError("Incorrect format in fractal configuration file")


