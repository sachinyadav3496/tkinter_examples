import threading 
import tkinter as tk
from time import sleep
from random import choice
colors = [ 'red', 'green', 'blue','cyan','yellow','purple','pink','orange']

root = tk.Tk()

label = tk.Label(root,bg='gray',height=5,width=50,text="Hello World",font=('times',20))
label.pack(fill=tk.BOTH,expand=tk.YES)

label1 = tk.Label(root,bg="#333333",height=5,width=50,text="bye World",font=('courier',15))
label1.pack(fill=tk.BOTH,expand=tk.YES)

def change1():
    try :
        while True:
            ch = choice(colors)
            label.config(fg=ch)
            label.update()
            sleep(2)
    except :
        pass

def change2():
    try : 
        while True:
            ch = choice(colors)
            label1.config(fg=ch)
            label1.update()
            sleep(1)
    except : 
        pass
b = tk.Button(root,text='quit',command=root.quit)
b.pack(side=tk.BOTTOM,fill=tk.X,expand=tk.YES)

th1 = threading.Thread(target=change1)
th2 = threading.Thread(target=change2)

th1.start()
th2.start()

root.mainloop()
