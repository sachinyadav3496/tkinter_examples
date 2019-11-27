from tkinter import * 

root = Tk()

l = Label(root,text='hello world',bg='red',font=('times',20),height=5,width=20)
def enter(event):
    l.config(bg='green',fg='white',font=('courier',20,'bold'))
def ex(event):
    l.config(bg='red',font=('times',20),fg='black')

l.bind('<Enter>',enter)
l.bind('<Leave>',ex)
l.pack(fill=BOTH,expand=YES)

root.mainloop()
