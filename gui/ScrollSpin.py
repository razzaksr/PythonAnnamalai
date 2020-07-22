# ScrolledText and spin box demo

from tkinter import *
from tkinter import scrolledtext, messagebox


def hai():
    messagebox.showinfo("Detail got", scrol.get(1.0, END))
    messagebox.showinfo("Details from SpinBox", spin.get())


win = Tk()
win.title("Spin box and ScrolledText")
win.geometry("600x300")
scrol = scrolledtext.ScrolledText(win, width=30, height=10)
scrol.grid(row=0, column=0)
spin = Spinbox(win, from_=1, to=100)
spin.grid(row=0, column=1)
bt = Button(win, text="Get Detail", command=hai)
bt.grid(row=0, column=2)
win.mainloop()
