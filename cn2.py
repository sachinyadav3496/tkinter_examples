from tkinter import * 

root = Tk()

canvas = Canvas(root)
canvas.config(height=400,width=400)
canvas.pack(fill=BOTH,expand=YES)


def draw_rectangle(event):
	for var in range(5):
		canvas.create_oval(event.x,event.y,event.x+var,event.y+var)
	#print(event)
canvas.bind("<B1-Motion>",draw_rectangle)

root.mainloop()
