import tkinter as tk

class Checkbar(tk.Frame):
    def __init__(self,parent=None,picks=[],side=tk.LEFT,anchor=tk.W):
        tk.Frame.__init__(self,parent)
        self.vars= []
        for pick in picks :
            var = tk.IntVar()
            chk = tk.Checkbutton(self,text=pick,variable=var)
            chk.pack(side=side, anchor=anchor, expand=tk.YES)
            self.vars.append(var)

    def state(self):
        return [ var.get() for var in self.vars ]

class Radiobar(tk.Frame):
    def __init__(self,parent=None,picks=[],side=tk.LEFT,anchor=tk.W):
        tk.Frame.__init__(self,parent)
        self.var = tk.StringVar()
        self.var.set(picks[0])
        for pick in picks :
            rad = tk.Radiobutton(self,text=pick, value=pick, variable=self.var)
            rad.pack(side=side,anchor=anchor,expand=tk.YES)
    def state(self):
            return self.var.get()

if __name__ == "__main__":
    root = tk.Tk()
    lng = Checkbar(root,['Python', 'C#', 'JAVA', 'C++'])
    gui = Radiobar(root,['Win', 'x11', 'mac' ],side=tk.TOP,anchor=tk.NW)
    tg1 = Checkbar(root,['ALL'])

    gui.pack(side=tk.LEFT,fill=tk.Y)
    lng.pack(side=tk.TOP,fill=tk.X)
    tg1.pack(side=tk.LEFT)

    lng.config(relief=tk.GROOVE,bd=2)
    gui.config(relief=tk.RIDGE,bd=2)

    def all_states():
        print(gui.state(),lng.state(),tg1.state())
    tk.Button(root,text='all state',command=all_states).pack()
    root.mainloop()
