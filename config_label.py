import tkinter as tk
import random

def change():
    choice = [ ('red','white'),('yellow','gray'),('white','green'),('silver','green'),
    ('purple','white'),('gold','blue'),('silver','black')]
    fg,bg = random.choice(choice)
    widget.config(fg=fg,bg=bg)

root = tk.Tk()

labelfont = ('times',20,'bold') # family, size, style

widget = tk.Label(root,text="Hello Config World!",)
widget.config(bg="black",fg="yellow")
widget.config(font=labelfont)
widget.config(height=3,width=20)
widget.pack(expand=tk.YES,fill=tk.BOTH)

button = tk.Button(root,text='change_color',command=change)
button.pack(side=tk.BOTTOM)
root.mainloop()
