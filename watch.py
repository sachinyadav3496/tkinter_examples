from tkinter import *

def clock():
    global hours, minutes, seconds
    if seconds == 60:
        seconds = 0
        if minutes < 60:
            minutes += 1
        else :
            hours += 1
            minutes = 0
    else:
        seconds += 1
    time = str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)
    lb.config(text=time)
    lb.after(1000, clock)

hours = 0
minutes = 0
seconds = 0

time = str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)

root = Tk()

lb = Label(root, text=time, height=5, width=25, bg="#123456", fg="#eeeeee")
lb.pack(fill=BOTH,expand=YES)
lb.after(1000, clock)

root.mainloop()
