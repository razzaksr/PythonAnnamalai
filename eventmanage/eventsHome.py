# Home module

from tkinter import *

from eventmanage.addParticpants import partAdd
from eventmanage.declareWinner import winDec
from eventmanage.getRecord import recordRead
from eventmanage.newEvent import neweve


class home(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Home for Event management")
        self.geometry("500x400")
        self.head = Label(text="Home for Events", font=('Monotype Cursiva', 30))
        self.head.pack(expand=True, fill=BOTH)
        self.bar = Menu(self)
        self.menu1 = Menu(self.bar, tearoff=0)
        self.menu1.add_command(label="New Event", command=self.newone)
        self.menu1.add_command(label="Add Participants", command=self.contribute)
        self.menu1.add_command(label="Declare Winner", command=self.announce)
        self.menu1.add_command(label="GetReports", command=self.reports)
        self.menu1.add_command(label="Exit",command=self.shut)
        self.bar.add_cascade(label="Organize", menu=self.menu1)
        self.config(menu=self.bar)

    def shut(self):
        self.destroy()

    def newone(self):
        self.new = neweve()
        self.new.mainloop()

    def contribute(self):
        self.add = partAdd()
        self.add.mainloop()

    def announce(self):
        self.win = winDec()
        self.win.mainloop()

    def reports(self):
        self.rec = recordRead()
        self.rec.mainloop()

'''hm=home()
hm.mainloop()'''
