from menu_frm import makemenu
from tkinter import *

root = Tk()
for i in range(2):
    mnu = makemenu(root)
    mnu.config(bd=2,relief=RAISED)
    Label(root,bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root,text="bye",command=root.quit).pack()

root.mainloop()
