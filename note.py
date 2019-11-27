from tkinter import * 
root = Tk()
e = Entry(root,font=('times',15),fg="#333333")
e.pack(side=BOTTOM,fill=X,expand=YES)
canvas = Canvas(root,height=400, width=400, borderwidth=0)
frame = Frame(canvas)

hsc = Scrollbar(root)
hsc.pack(side=BOTTOM,fill=X)
hsc.config(command=canvas.xview,orient='horizontal')
canvas.config(xscrollcommand=hsc.set)

vsc = Scrollbar(root)
vsc.pack(side=RIGHT,fill=Y)
vsc.config(command=canvas.yview)
canvas.config(yscrollcommand=vsc.set)

canvas.pack(side=LEFT,fill=BOTH,expand=YES)
labels = []

canvas.create_window((0,0), window=frame, anchor='nw', tags="frame")
#canvas.config(scrollregion=canvas.bbox('all'))
frame.bind("<Configure>",lambda event:canvas.config(scrollregion=canvas.bbox('all')))
def on_entry(l):
    l.configure(fg='green', font=('times', 15, 'bold'))
def on_leave(l):
    l.configure(fg='#333333', font=("times", 15, 'bold'))
flag = False
def add_note(event):
    global flag
    data = e.get()
    if flag:
        data = data.rjust(50)
        flag = False
    else : 
        flag = True
    e.delete('0', END)
    l = Label(frame,text=data,fg='#333333', font=("times", 15, 'bold'))
    l.bind('<Enter>',lambda event:on_entry(l))
    l.bind('<Leave>',lambda event:on_leave(l))
    l.pack(anchor=NW)
    
e.bind("<Return>",add_note)
e.focus()
root.mainloop()
