import tkinter as tk

class Hello(tk.Frame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.pack()
        self.data = 1
        self.make_widgets()
    def make_widgets(self):
        widget = tk.Button(self,text="Hello frame World",command=self.message)
        widget.pack(side=tk.LEFT)
    def message(self):
        print(f"Hello World! {self.data}")
        self.data += 1

if __name__ == "__main__":
    Hello().mainloop()
