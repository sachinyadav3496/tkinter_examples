import tkinter as tk
import sys

def hello(event):
    print("Click Twice to exit!")

def quit(event):
    print("I must be going")
    sys.exit()

widget = tk.Button(None,text="Hello World!")
widget.pack()

widget.bind('<Button-1>',hello) # bind left butotn for single click
widget.bind('<Double-1>',quit) # bind left button for double click

widget.mainloop()
