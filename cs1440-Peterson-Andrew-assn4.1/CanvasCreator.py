from tkinter import Tk, PhotoImage, mainloop, Canvas

class CanvasCreator:
    def __init__(self, pixels, image = "data\elephants.frac"):
        self.__pixels = pixels
        self.__image = image
        self.__window = Tk()
        self.__photo = PhotoImage(width=512, height=512)


    def createCanvas(self):
        canvas = Canvas(self.__window, width=self.__pixels, height=self.__pixels, bg='#ffffff')
        canvas.pack()
        canvas.create_image((self.__pixels / 2, self.__pixels / 2), image=self.__photo, state="normal")

    def write(self):
        self.__photo.write(self.__image + ".png")
        print("Wrote picture " + self.__image + ".png")

    def put(self,c2, col, row):
        self.__photo.put(c2, (col, self.__pixels - row))

    def update(self):
        self.__window.update()

    def mainloop(self):
        mainloop()