# Adding new Element label in window

from tkinter import *

obj=Tk()
obj.title("Second window with label")
obj.geometry("500x300")
lbl=Label(obj,text="Welcome to Sona College")
lbl.grid(row=0,column=0)# position
obj.mainloop()
