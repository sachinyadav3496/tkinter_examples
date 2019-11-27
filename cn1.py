from tkinter import * 

r = Tk()

c = Canvas(r,width=400,height=400,bg="#cccccc")
c.pack(fill=BOTH,expand=YES)
#c.create_line(0,0,400,400)

#c.create_rectangle(0,0,300,150,fill='red')

for i in range(1,20,2):
    c.create_line(0,i,50,i)

c.create_oval(200,200,400,300)
    
r.mainloop()
