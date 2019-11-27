from tkinter import * 

root = Tk()

menu  = Menu(root)

fmenu  = Menu(menu)
fmenu.add_command(label="Open...",command=lambda : print("...open..."))
fmenu.add_command(label="New...",command=lambda : print("...new..."))
fmenu.add_command(label="Quit...",command=root.quit)

other = Menu(menu)
x = Menu(other)
x.add_command(label='ha ha',command=lambda :print("ha ha ah"))
x.add_command(label='hi hi',command=lambda : print('hiii hii hii'))

other.add_cascade(label='new menu',menu=x)

menu.add_cascade(label="file",menu=fmenu)
menu.add_separator()
menu.add_cascade(label='other',menu=other)
root.config(menu=menu)

root.mainloop()
