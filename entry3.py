import tkinter as tk
fields = ("Name","Job","Pay")

def fetch(variables):
    for variable in variables:
        print("Input=>",variable.get())

def makeform(root,fields):
    form = tk.Frame(root)
    left = tk.Frame(root)
    right = tk.Frame(root)

    form.pack(side=tk.TOP,fill=tk.X)
    left.pack(side=tk.LEFT)
    right.pack(side=tk.RIGHT,fill=tk.X)

    variables = []
    for field in fields :
        lab = tk.Label(left, width=5, text=field)
        ent = tk.Entry(right)
        lab.pack(side=tk.TOP)
        ent.pack(side=tk.TOP,fill=tk.X)
        var = tk.StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        variables.append(var)

    return variables

if __name__ == "__main__":
    root = tk.Tk()
    vars  = makeform(root,fields)
    tk.Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=tk.LEFT)
    tk.Button(root, text="Quit!", command=root.destroy).pack(side=tk.RIGHT)

    root.bind("<Return>",(lambda event: fetch(vars)))
    root.mainloop()
