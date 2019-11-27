from tkinter import *
all_objects = []
root = Tk()

old_event = None
drawn = None 

def start(event):
    global old_event,drawn
    old_event = event
    drawn = None

def draw(event):
    global drawn,allobjects
    canvas = event.widget
    if drawn:
        all_objects.remove(drawn)
        canvas.delete(drawn)
    objectID = canvas.create_rectangle(old_event.x,old_event.y,event.x,event.y)
    drawn = objectID
    all_objects.append(objectID)


canvas = Canvas(root,bd=0)
canvas.pack(fill=BOTH,expand=YES)
canvas.config(height=400,width=400,bg='#123456',borderwidth=0)

canvas.bind("<Button-1>",start)
canvas.bind("<B1-Motion>",draw)
def move(event):
    if all_objects:
        diff_x,diff_y = (event.x-old_event.x,event.y-old_event.y)
        canvas.move(all_objects[-1],diff_x,diff_y)
canvas.bind("<Button-3>",move)
def undo(event):
    if all_objects:
        canvas.delete(all_objects[-1])
        all_objects.pop()
canvas.bind('<Control-z>',undo)
Button(root,text='undo',command=lambda x='hi':undo(x)).pack()
root.mainloop()
