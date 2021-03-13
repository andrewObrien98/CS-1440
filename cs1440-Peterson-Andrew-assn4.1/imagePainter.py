

class ImagePainter():
    def __init__(self, fractal, color, canvas):
        self.__fractal = fractal
        self.__color = color
        self.__pixels = fractal.getPixels()
        self.__pixelSize = fractal.getPixelSize()
        self.__minX = fractal.getMinX()
        self.__minY = fractal.getMinY()
        self.__canvas = canvas

    def setUp(self):
        self.__canvas.createCanvas()
        self.paint()
        self.__canvas.write()
        self.__canvas.mainloop()

    def paint(self):
        for row in range(self.__pixels, 0, -1):
            for col in range(self.__pixels):
                x = self.__minX + col * self.__pixelSize
                y = self.__minY + row * self.__pixelSize
                j = self.__fractal.count(complex(x, y))
                #right here is where I can pass the number into the gradient to get the color
                c2 = self.__color.getColor(j)
                self.__canvas.put(c2, col, row)
            self.__canvas.update()