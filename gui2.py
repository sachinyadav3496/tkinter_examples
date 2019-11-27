import tkinter as tk
import sys
class HelloClass:
    def __init__(self):
        widget = tk.Button(None,text="Hello, World",command=self.quit)
        widget.pack()
    def quit(self):
        print("Hello Class!! Method World")
        sys.exit()

HelloClass()
tk.mainloop()
