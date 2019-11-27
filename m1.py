from tkinter import  *

root = Tk()

menu = Menubutton(root,text='menu')
menu.pack(side=LEFT,expand=YES)
def hello():
    print("hello")

def bye():
    print("bye")
o = Menu(menu,tearoff=True)
o.add_command(label="Hello",command=hello)
o.add_command(label="Bye",command=bye)
menu.config(menu=o)
root.config(menu=menu)

root.mainloop()
