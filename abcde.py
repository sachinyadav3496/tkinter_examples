import tkinter as tk

root = tk.Tk()

l = tk.Label(root,text="Menu time")
l.pack()

menu = tk.Menu(root)

sub_menu = tk.Menu(menu)
sub_menu.add_command(label="hi",command=lambda : print("hello world"))
sub_menu.add_command(label='bye',command=lambda : print("bye world"))
sub_menu.add_command(label='good',command=lambda : print("good bye"))

menu.add_cascade(label='options',menu=sub_menu)

root.config(menu=menu)

root.mainloop()
