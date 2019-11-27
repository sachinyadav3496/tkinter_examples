import tkinter as tk

root = tk.Tk()
states = []
for i in range(10):
    var = tk.IntVar()
    chk = tk.Checkbutton(root, text=str(i), variable=var)
    chk.pack(side=tk.LEFT)
    states.append(var)

root.mainloop()
print(*[var.get() for var in states ])
