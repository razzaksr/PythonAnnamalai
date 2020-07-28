# adding Login

from tkinter import *
from tkinter import messagebox

from eventmanage.eventsHome import home

'''def log():
    if user.get()=='annamalai' and pas.get()=='salem':
        win.destroy()
        hm=home()
        hm.mainloop()
    else:messagebox.showinfo("error","Invalid login")

win=Tk()
win.title("Login")
win.geometry("500x400")
p1=PhotoImage(file="C:\\Users\\DOLL\\PycharmProjects\\MorningBatch\\eventmanage\\bday.ico")
win.iconphoto(False,p1)
head=Label(win,text="Login to Event home")
head.pack(side=TOP,padx=10,pady=20)
user=Entry(win)
user.pack(side=TOP,padx=10,pady=40)
pas=Entry(win,show="*")
pas.pack(side=TOP,padx=10,pady=60)
bt=Button(win,text="Login",command=log)
bt.pack(side=TOP, padx=10, pady=80)

mainloop()'''

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
        self.pas=Entry(self,show="*")
        self.pas.pack(side=TOP,padx=10,pady=60)
        self.bt=Button(self,text="Login",command=self.log)
        self.bt.pack(side=TOP, padx=10, pady=80)
    def log(self):
        if self.user.get()=='annamalai' and self.pas.get()=='salem':
            self.destroy()
            hm=home()
            hm.mainloop()
        else:messagebox.showinfo("error","Invalid login")

log=enter()
log.mainloop()