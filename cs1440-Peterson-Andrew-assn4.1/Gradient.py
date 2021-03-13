class Gradient():
    def __init__(self, numColors):
        raise NotImplementedError("Concrete subclass of gradient must implement __init__")

    def getColor(self, number):
        raise NotImplementedError("Concrete subclass of gradient must implement getColor() method")