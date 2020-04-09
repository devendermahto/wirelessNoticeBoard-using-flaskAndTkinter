from tkinter import *
from PIL import ImageTk,Image
import cv2

class app():

    def __init__(self):
        self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
        self.canvas = Canvas(root, width = self.w, height = self.h)
        root.attributes("-fullscreen", True)
        im = cv2.imread("received.png")
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, (self.w, self.h))
        im = Image.fromarray(im)
        self.img = ImageTk.PhotoImage(im)
        self.imgArea = self.canvas.create_image(self.w/2, self.h/2, anchor = CENTER, image = self.img)
        self.canvas.pack()
        root.after(4000, self.changeImg)

    def changeImg(self):
        im = cv2.imread("received.png")
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, (self.w, self.h))
        im = Image.fromarray(im)
        self.img = ImageTk.PhotoImage(im)
        self.canvas.itemconfig(self.imgArea, image = self.img)
        root.after(4000, self.changeImg)


if __name__ == "__main__":
    root = Tk()
    app = app()
    root.mainloop()