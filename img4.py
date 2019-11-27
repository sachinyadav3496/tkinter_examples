from glob import glob
import tkinter as tk
from PIL import ImageTk
from random import choice
import os
root = tk.Tk()
img_obj = [ ImageTk.PhotoImage(file="./images/"+fname) for fname in os.listdir("images")]
print(img_obj)
def change():
    img = choice(img_obj)
    print(img,img.height(),img.width())
    b.config(height=img.height(),width=img.width())
    b.config(image=img)

#photoimg = ImageTk.PhotoImage(file='images/one.jpg')
b = tk.Button(root,text='image',command=change)
b.pack()

root.mainloop()
