from tkinter import * #get a widget object
widget = Label(None,text="Hello GUI, World") #make one
widget.pack(expand=YES,fill=BOTH) #arrange it
widget.mainloop() #Start event loop

"""
pseudo-program for mainloop

def mainloop():
    while the main window has not been closed:
        if an event has occurred:
            run the associated event handler function
"""
