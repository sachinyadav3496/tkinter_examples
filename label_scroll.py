from tkinter import * 
data = """
This module can be run standalone to experiment with these widgets, but it is also
designed to be useful as a library object. By passing in different selection lists to the
options argument and redefining the runCommand method in a subclass, the Scrolled
List component class defined here can be reused anytime you need to display a scrollable list. In fact, we will be reusing it this way in Chapter  PyEdit program. With just
a little forethought, it is  easy to extend the tkinter library with Python classes this way.
When run standalone, this script generates the window in Figure 9-14, shown here
with Windows 7 look-and-feel. It is a Frame, with a Listbox on its left containing 20
generated entries (the fifth has been clicked), along with an associated Scrollbar on its
right for moving through the list. If you move the scroll, the list moves, and vice versa

"""

import tkinter as tk
root = Tk()

fr = tk.Listbox(root)
sc  = Scrollbar(fr)
pos = 0 
for line in data.split():
    fr.insert(pos,line)
    pos += 1
sc.config(command=fr.yview)
fr.config(yscrollcommand=sc.set)

sc.pack(side=LEFT,fill=Y)
fr.pack(side=RIGHT,fill=BOTH,expand=YES)
root.mainloop()
