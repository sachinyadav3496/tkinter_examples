from tkinter import *
from random import shuffle
colors = [ 'red', 'green', 'yellow', 'purple', 'gray', 'magenta', 'cyan',
        'blue', 'orange', 'black', ]
last_color = None
score = 0
timeout = 30
root = Tk()

start = False

frame = Frame(root, bg="#333333")

l = Label(root, text=", ".join(map(str.upper,colors)))
l.config(bg="#333333",fg="#eeeeee",font=("Times",15,"bold"))
l.pack(side=TOP,fill=X,expand=YES)
t = Label(root, text=f"Time Left : {timeout}", font=("Courier",15,"bold"),
         width=25, bg="#333333", fg="#eeeeee")
t.pack(side=TOP, fill=X, expand=YES)
l1 = Label(root, text="", fg="red", font=("courier", 50 , "bold"))
l1.config(width=10, bg="#c0c0c0", relief=RAISED, borderwidth=5)
l1.pack(side=TOP, expand=YES)

s = Label(root,text=f"Your Score : {score}")
s.config(font=("Courier", 20, "bold"), height=3, width=25, bg="#333333",
        fg="#eeeeee")
s.pack(side=TOP, fill=X, expand=YES)

quit = Button(root, text="Exit", command=root.quit)
quit.config(width=10, bg="#dddddd", relief=RAISED, fg="#333333", font=("Times", 15))
quit.pack(side=BOTTOM, expand=True)
e = Entry(root)
e.config(font=("courier",25,"bold"), bg="#555555", fg="#eeeeee")
e.pack(side=BOTTOM, expand=YES)

frame.pack(fill=BOTH, expand=YES)

def choose_color():
    global last_color
    shuffle(colors)
    if last_color == colors[0]:
        choose_color()
    else :
        last_color = colors[0]

def change_color(event):
    global  score, start
    start = True
    if e.get().lower().strip() == colors[0]:
        score += 1
        s.config(text=f"Your Score : {score}")

    e.focus_set()
    e.delete(0,END)
    choose_color()
    l1.config(text=colors[1].upper(), fg=colors[0])

def start_timer():
    global timeout, start,score
    if start:
        if timeout:
            timeout -= 1
            t.config(text=f"Time Left : {timeout}")
            t.update()
            t.after(1000,start_timer)

        else :
            l1.config(text="")
            win = Toplevel(root)
            win.focus()
            win.grab_set()
            lab = Label(win,text=f"Your Final Score is : {score}",
                fg="#dddddd", bg="#333333")
            lab.config(font=("courier", 25, "bold"),
                height=5,
                width=25)
            lab.pack(fill=BOTH, expand=YES)
            b = Button(win, text="Exit", command=win.destroy, font=("times",15))
            b.pack(side=BOTTOM, fill=X, expand=YES)
            b.config(fg="#333333", bg="#dddddd")
            timeout = 30
            start = False
            score = 0
            start_timer()
    else:
        t.after(1000,start_timer)


e.focus()

prompt = Label(root,text="Type in Your Guess Color Here",bg="#333333", fg="#eeeeee",
    font=('Times',15,"bold"))
prompt.pack(side=BOTTOM,expand=YES)

start_timer()
root.bind("<Return>", change_color)
root.config(bg="#333333")
root.wm_minsize(600, 400)
#root.wm_maxsize(600, 400)
root.title("Color Game")

im = PhotoImage(file="images/color_game.png")
root.wm_iconphoto(root,im)

root.mainloop()
