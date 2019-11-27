import tkinter as tk
from gui7 import Hello
from sys import exit

master = tk.Tk()

Hello(master).pack(side=tk.RIGHT)
tk.Button(master,text='exit',command=exit).pack(sid=tk.LEFT)

master.mainloop()
