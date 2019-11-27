from tkinter import *

class ScrolledCanvas(Frame):
    def __init__(self,parent=None,color='brown'):
        Frame.__init__(self,parent)
        self.pack(expand=YES,fill=BOTH)
        canv = Canvas(self,bg=color,relief=SUNKEN)
        canv.config(width=300,height=200)
        canv.config(scrollregion=(0,0,300,10000))
        canv.config(highlightthickness=0)

        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT,fill=Y)
        canv.pack(side=LEFT,fill=BOTH,expand=YES)

        self.fillContent(canv)
        canv.bind("<Double-1>",self.onDoubleClick)
        self.canvas = canv
    def fillContent(self,canv):
        for i in range(10):
            canv.create_text(150,50+(i*100),text='spam'+str(i), fill='beige')

    def onDoubleClick(self,event):
        print(event.x,event.y)
        print(self.canvas.canvasx(event.x),self.canvas.canvasy(event.y))

if __name__ == "__main__" :
    ScrolledCanvas().mainloop()
