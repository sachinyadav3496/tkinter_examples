import tkinter as tk

class HelloButton(tk.Button):
    def __init__(self,parent=None,**config):
        super().__init__(parent,**config)
        self.pack()
        self.config(command=self.callback)
    def callback(self):
        print("Good Bye World!!!")
        self.quit()

if __name__ == "__main__":
    master = tk.Tk()
    b = HelloButton(master,text="Hello subclass World")
    b.pack()
    master.mainloop()
