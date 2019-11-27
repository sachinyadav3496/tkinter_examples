from tkinter import * 

root = Tk()
def hello(row,col):
    print(f"Helllo World Button {row}{col}")
for row in range(5):
    for col in range(4):
        t = f"{row}.{col}"
        Button(root,text=t,relief=RIDGE,height=2,width=5,command=lambda row=row,col=col:hello(row,col)).grid(row=row,column=col, sticky=NSEW)
    root.rowconfigure(row,weight=1)
    
for c in range(4):
    root.columnconfigure(c,weight=1)


root.mainloop()
