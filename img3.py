from glob import glob
import tkinter as tk
from random import choice


def change():
    name,photo = choice(all_files)
    name = name.split('\\')[-1]
    label.config(text=name)
    pix.config(image=photo,width=photo.width(),height=photo.height())

root = tk.Tk()

pix = tk.Button(root,text="Draw",command=change, bg='white')
pix.pack(pady=10)

label = tk.Label(root)
label.pack(fill=tk.X, expand=tk.YES,pady=10  )

all_files = [ (fname,tk.PhotoImage(file=fname)) for fname in glob('.\\images\\*.png') ]

root.mainloop()
