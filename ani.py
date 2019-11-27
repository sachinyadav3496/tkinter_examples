from tkinter import * 
from random import choice, shuffle

ch = list("1234567890ABCDEF")

root = Tk()

l = Label(root,text="Hello World",height=15,width=50)
l.pack(fill=BOTH, expand=YES)

b = Button(root,text="Kill Me",height=2,width=10,command=root.quit)
b.pack(fill=X,expand=YES)


def change():
    color = "#"+"".join([ choice(ch) for var in range(6) ])
    l.config(bg=color)
    color = "#"+"".join([ choice(ch) for var in range(6) ])
    l.config(fg=color)
    l.after(1000,change)

def hi():
    b.flash()
    color = "#"+"".join([ choice(ch) for var in range(6) ])
    b.config(bg=color)
    b.after(1000,hi)

change()
hi()
root.mainloop()
