# adding Login

from tkinter import *
from tkinter import messagebox

from eventmanage.eventsHome import home


class enter(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")
        self.geometry("500x400")
        p1=PhotoImage(file="C:\\Users\\DOLL\\PycharmProjects\\MorningBatch\\eventmanage\\bday.ico")
        self.iconphoto(False,p1)
        self.head=Label(self,text="Login to Event home")
        self.head.pack(side=TOP,padx=10,pady=20)
        self.user=Entry(self)
        self.user.pack(side=TOP,padx=10,pady=40)
        self.pas=Entry(self)
        self.pas.pack(side=TOP,padx=10,pady=60)
        self.bt=Button(self,text="Login",command=self.log)
        self.bt.pack(side=TOP, padx=10, pady=80)
    def log(self):
        if self.user.get()=='annamalai' and self.pas.get()=='salem':
            hm=home()
            hm.mainloop()
        else:messagebox.showinfo("error","Invalid login")

log=enter()
log.mainloop()