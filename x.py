from tkinter import * 
root = Tk()

def keypress(event):
    print(event)
root.bind('<Control-z>',keypress)

root.mainloop()
