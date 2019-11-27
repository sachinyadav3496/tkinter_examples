import tkinter as tk

root = tk.Tk()

s = """Hello world
how are you
let's go to the party
        python is awesome

    hey hi bye bye bye
go to the world to say the chances

    you are my world to take chances

i can see you smile
    i can see you sad
you such a guy
    don't let anyone play

be  be be be let be honest

    ha ha aha ha ah
you such a guy
    not let you do directory

    by by by

    """

m = tk.Text(root,text=s,font=('times',30,'bold'))
m.pack()
root.mainloop()
