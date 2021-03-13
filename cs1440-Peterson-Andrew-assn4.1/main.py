import sys
from FractalFactory import FractalFactory
from CanvasCreator import CanvasCreator
from imagePainter import ImagePainter
from GradientFactory import GradientFactory

def main():
    fractal = ""
    gradient = ""

    if len(sys.argv) < 2:
        factory = FractalFactory()
        fractal = factory.makeFractal()
        gradient = GradientFactory().makeGradient(fractal.getIteration())


    elif len(sys.argv) == 2:
        factory = FractalFactory()
        fractal = factory.makeFractal(sys.argv[1])
        gradient = GradientFactory().makeGradient(fractal.getIteration())

    elif len(sys.argv) == 3:
        factory = FractalFactory()
        fractal = factory.makeFractal(sys.argv[1])
        gradient = GradientFactory().makeGradient(fractal.getIteration(), sys.argv[2])

    canvas = CanvasCreator(fractal.getPixels(), sys.argv[1] )
    image = ImagePainter(fractal, gradient, canvas)
    image.setUp()
