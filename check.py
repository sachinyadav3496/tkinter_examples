import tkinter as tk
states = []
def onPress(i):
    states[i]= not states[i]
    print(*states)

root = tk.Tk()

for i in range(10):
    chk = tk.Checkbutton(root, text=str(i), command=(lambda i=i:onPress(i)))
    chk.pack(side=tk.LEFT)
    states.append(False)

root.mainloop()
print(*states)
