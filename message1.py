import tkinter as tk

root = tk.Tk()

msg = tk.Message(text="Oh why the way which one is pink ?")
msg.config(bg="pink",font=('times', 20, 'italic'))
msg.pack(fill=tk.X,expand=tk.YES)

root.mainloop()
