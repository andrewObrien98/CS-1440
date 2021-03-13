from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, coordinates):
        self.minX = coordinates["centerX"] - (coordinates["axisLength"] / 2.0)
        self.minY = coordinates["centerY"] - (coordinates["axisLength"] / 2.0)
        self.maxX = coordinates["centerX"] + (coordinates["axisLength"] / 2.0)
        self.pixels = coordinates["pixels"]
        self.pixelSize = abs(self.maxX - self.minX) / self.pixels
        self.iterations = coordinates["iterations"]

    def count(self, z):
        c = complex(-1.0, 0.0)

        for i in range(self.iterations):
            z = z * z + c  # Iteratively compute z1, z2, z3 ...
            if abs(z) > 2:
                return i # The sequence is unbounded

        return self.iterations

    def getPixels(self):
        return self.pixels

    def getMinX(self):
        return self.minX

    def getMinY(self):
        return self.minY

    def getPixelSize(self):
        return self.pixelSize

    def getIteration(self):
        return self.iterations