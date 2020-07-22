# my own class window

from tkinter import *
from tkinter import messagebox


class Zealous(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("MyOwnWindow")
        self.geometry("500x300")
        self.textbox=Entry(self,width=10,fg="blue",bg="red")
        self.textbox.pack(padx=0,pady=0,side=TOP)
        self.bt=Button(self,text="Click",command=self.hey)
        self.bt.pack(padx=0, pady=0, side=BOTTOM)
    def hey(self):
        messagebox.showinfo("Information",self.textbox.get())

z=Zealous()
z.mainloop()