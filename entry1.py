import tkinter as tk

def fetch():
  print(f"Input => {ent.get()}")
  ent.delete(0,tk.END)
root = tk.Tk()


ent = tk.Entry(root)
ent.insert(0,'Type words here')
ent.pack(side=tk.TOP,fill=tk.X)

ent.focus()
ent.bind("<Return>",(lambda event:fetch()))

btn=tk.Button(root,text='Fetch',command=fetch)
btn.pack(side=tk.LEFT)

root.mainloop()

"""
In later examples, we’ll also see the Entry widget’s state='disabled' option, which
makes it read only, as well as its show='*' option, which makes it display each character
as a * (useful for password-type inputs). Try this out on your own by changing and
running this script for a quick look. Entry supports other options we’ll skip here, too;
"""
