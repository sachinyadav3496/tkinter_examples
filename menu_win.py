import tkinter as tk
from tkinter.messagebox import *

def notdone():
    showerror("Not Implemented ","Not yet Available")

def makemenu(win):
    top = tk.Menu(win)
    win.config(menu=top)

    file = tk.Menu(top)
    file.add_command(label="New...",command=notdone,underline=0)
    file.add_command(label="Open...",command=notdone,underline=0)
    file.add_command(label="Quit...",command=win.quit,underline=0)
    top.add_cascade(label='File',menu=file,underline=0)

    edit = tk.Menu(top, tearoff=False)
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit', menu=edit, underline=0)

    submenu = tk.Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)

if __name__ == '__main__':
    root = tk.Tk() # or Toplevel()
    root.title('menu_win') # set window-mgr info
    makemenu(root) # associate a menu bar
    msg = tk.Label(root, text='Window menu basics') # add something below
    msg.pack(expand=tk.YES, fill=tk.BOTH)
    msg.config(relief=tk.SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
