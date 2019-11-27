import tkinter as tk
import sys

root =tk.Tk()
root.title("MyApp")
root.wm_minsize(400,400)

def quit():
    print("Hey, I must be going")
    sys.exit(0)

widget = tk.Button(root,text="Press",command=quit)
widget.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)

root.mainloop()
