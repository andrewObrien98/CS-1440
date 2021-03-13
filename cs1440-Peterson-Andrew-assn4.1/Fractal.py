class Fractal():
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self, c):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def getPixels(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement getPixels() method")

    def getMinX(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement getMinX() method")

    def getMinY(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement getMinY() method")

    def getPixelSize(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement getPixelSize() method")

    def getIteration(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement getIteration() method")