import tkinter as tk 
from tkinter import * 
import socket 
import threading 

ip,port = input("Enter Ip address : "),int(input("Enter port : "))
server = socket.socket()
server.bind((ip,port))
server.listen(10)
client,addr = server.accept()
print(f"Got a connection from client : {addr[0]}:{addr[1]} ")



root = tk.Tk()


def send(client):
        data = e1.get()
        if data : 
            client.send(data.encode())
            data = "server-->" + data
            lst.insert('end',data)
            e1.delete(0,'end')

e1 = Entry(root,font=("courier",15,'bold'),fg='#333333')
e1.pack(side=tk.BOTTOM, fill=tk.X,expand=YES)
e1.bind("<Return>",lambda event,client=client: send(client))

lst = Listbox(root,height=10,width=100)
sc = Scrollbar(root)
sc.config(command=lst.yview)
lst.config(yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y,expand=YES)
lst.pack(side=LEFT,fill=BOTH,expand=YES)


def recv(client):
    try:
        while True:
            data = client.recv(60).decode()
            data = ("client-->"+data).rjust(60)
            if data : 
                lst.insert('end',data)

    except : 
        server.close()

th = threading.Thread(target=recv,args=(client,))
th.start()
root.title("SERVER")
root.mainloop()
