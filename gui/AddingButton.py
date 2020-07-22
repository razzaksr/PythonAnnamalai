# Adding new label and button

from tkinter import *
from tkinter import messagebox


def hai():
    lbl.configure(text="Button Clicked")
    messagebox.showinfo("information","Button Clicked by user")

win=Tk()
win.title("Label and Button")
win.geometry("500x300")
win.configure(bg="blue")
lbl=Label(win,text="Hello there..",font=("Times New Roman",19),bg="yellow",fg="red")
lbl.grid(row=0,column=0)
bt=Button(win,text="Press Here",fg="yellow",bg="maroon",command=hai)
bt.grid(row=0,column=1)
win.mainloop()