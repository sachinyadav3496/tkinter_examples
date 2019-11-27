from tkinter import *
from random import choice
from time import sleep
root = Tk()

colors= [ 'red', 'green', 'blue', 'orange', 'yellow', 'pink' ]
class my(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        l = Label(root,text="Hello World",font=('courier',20,'bold'),
        height=10,width=40)
        l.pack(fill=BOTH,expand=YES)
        self.l = l 
        self.repeator()
    def repeator(self):
        c = choice(colors)
        self.l.config(bg=c)

        self.after(1000,self.repeator)

    def change(self):
        c = choice(colors)
        self.l.config(bg=c)

my(root)
root.mainloop()
