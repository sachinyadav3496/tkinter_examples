from tkinter import * 
root = Tk()


cn = Canvas(root)
cn.config(height=300,width=300)
fr = Frame(cn)
sc = Scrollbar(cn)
sc.config(command=cn.yview)
cn.config(yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y,expand=YES)
cn.pack(side=LEFT,fill=BOTH,expand=YES)
fr.bind("<Configure>",lambda event:cn.configure(y


root.mainloop()
