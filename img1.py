import tkinter as tk

gifdir = "./images/"

win = tk.Tk()

igm = tk.PhotoImage(file=gifdir+'one.gif')
tk.Button(win,image=igm).pack()
win.mainloop()
