# adding text box
from tkinter import *


def saySome():
    lbl.configure(text="Mr/Miss/Mrs." + box.get())


win = Tk()
win.title("Text box")
win.geometry("700x300")
lbl = Label(win, text="Mr/Miss/Mrs..")
lbl.grid(row=0, column=0)
box = Entry(win, width=20, bg="black", fg="white")
box.grid(row=0, column=1)
bt = Button(win, text="Adding name", command=saySome)
bt.grid(row=0, column=2)
win.mainloop()
