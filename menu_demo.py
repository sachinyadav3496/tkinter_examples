from tkinter import *
from tkinter.messagebox import *
import os

class NewMenuDemo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack(expand=YES,fill=BOTH)
        self.createWidgets()
        self.master.title("Toolbars and Menus")
        self.master.iconname('tkpython')

    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        L = Label(self,text="Menu and Toolbar Demo")
        L.config(relief=SUNKEN,width=40,height=10,bg='white')
        L.pack(expand=YES,fill=BOTH)
    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Quit', command=self.quit ).pack(side=RIGHT)
        Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)
    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label="Open...",command=self.notdone)
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)
    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)
    def imageMenu(self):
        photoFiles = [ os.path.join(os.path.abspath("./images"),fname)
                                for fname in os.listdir('images') if 'jpg' not in fname ]
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        for file in photoFiles:
            img = PhotoImage(file=file)
            pulldown.add_command(image=img, command=self.notdone)
            self.photoObjs.append(img) # keep a reference
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)
    def greeting(self):
        showinfo('greeting', 'Greetings')
    def notdone(self):
        showerror('Not implemented', 'Not yet available')
    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)
if __name__ == '__main__':
        NewMenuDemo().mainloop() # if I'm run as a script
