gifdir = "./images/"
from tkinter import *
win = Tk()
img = PhotoImage(file=gifdir + "one.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(),height=img.height()) # by default canvas does not fit entire surface
can.create_image(2,2, image=img, anchor=NW) # x, y coordinates
win.mainloop()
