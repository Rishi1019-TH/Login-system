from tkinter import *
from tkinter import messagebox
import random


def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")


    elif(uname == "Rishi" and password == "1019"):

        messagebox.showinfo("RISHI","Login Success")
        root.destroy()
    elif(uname == "Krishiv" and password == "2019"):

        messagebox.showinfo("KRISHIV","Login Success")
        root.destroy()  
    else :
        messagebox.showinfo("","Incorrent Username and Password")


root = Tk()
root.title("Login")
root.geometry("300x200")
root.configure(bg="black")


global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")


Button(root, text="Login", command=Ok ,height = 3, width = 13,cursor = "hand2",bg="black",fg="white").place(x=10, y=100)

root.mainloop()
