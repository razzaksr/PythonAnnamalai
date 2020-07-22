# adding combobox
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
def say():
    messagebox.showinfo("Combobox action","Choosen Dish is: "+comb.get())
win=Tk()
win.title("Combox demo")
win.geometry("400x200")
comb=Combobox(win)
comb['values']=('Mutton Biriyani','Chicken Biriyani','Butter naan','Chicken Tikka', 'Paneer tikka')
comb.grid(row=0,column=0)
bt=Button(win,text="Show choosen",command=say)
bt.grid(row=0,column=1)
win.mainloop()