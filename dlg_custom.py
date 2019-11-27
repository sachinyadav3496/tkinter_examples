import tkinter as tk
import sys

makemodal = len(sys.argv ) > 1

def dialog():
    win = tk.Toplevel()
    tk.Label(win,text="Hard Drive! Formatted!!").pack()
    tk.Button(win,text="OK",command=win.destroy).pack()
    if makemodal :
        win.focus_set() # take over input focus
        win.grab_set() # disable old windows while i am open
        win.wait_window() # and wait here untill window destroyed
    print("dialog exit")

root = tk.Tk()

tk.Button(root,text="PopUp",command=dialog).pack()
root.mainloop()
