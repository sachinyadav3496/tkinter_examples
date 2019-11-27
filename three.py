from tkinter import * #get a widget object
root = Tk()
widget = Label(root) #make one
widget.config(text="Hello GUI, World")
widget.pack(expand=YES,fill=BOTH) #arrange it
root.title('MyGUI')
root.wm_minsize(400,400)
root.mainloop()

"""
pseudo-program for mainloop

def mainloop():
    while the main window has not been closed:
        if an event has occurred:
            run the associated event handler function
"""
