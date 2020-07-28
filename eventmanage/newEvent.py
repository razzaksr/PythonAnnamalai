# Adding new event

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *

class neweve(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Adding New Event")
        self.geometry("500x300")
        p1 = PhotoImage(file="C:\\Users\\DOLL\\PycharmProjects\\MorningBatch\\eventmanage\\bday.ico")
        self.iconphoto(False, p1)
        f = font = ('Times New Roman', 15)
        self.head = Label(self, text="Adding New event", font=('Times New Roman', 20))
        self.head.grid(row=0, column=10)
        self.typedate = Label(self, text="Enter the date of event", font=f)
        self.typedate.grid(row=1, column=8)
        self.date = Entry(self)
        self.date.grid(row=1, column=30)
        self.typename = Label(self, text="Enter the name of event", font=f)
        self.typename.grid(row=2, column=8)
        self.name = Entry(self)
        self.name.grid(row=2, column=30)
        self.typedept = Label(self, text="Enter the department who conducts the event", font=f)
        self.typedept.grid(row=3, column=8)
        self.dept = Combobox(self)
        self.dept['values'] = ('Select department', 'CSE', 'EEE', 'ECE', 'IT', 'Mech')
        self.dept.grid(row=3, column=30)
        self.typeorg = Label(self, text="Enter the name of event organiser", font=f)
        self.typeorg.grid(row=4, column=8)
        self.org = Entry(self)
        self.org.grid(row=4, column=30)
        self.typeprize = Label(self, text="Enter the prize of event", font=f)
        self.typeprize.grid(row=5, column=8)
        self.prize = Entry(self)
        self.prize.grid(row=5, column=30)
        self.bt = Button(self, text="Add to Base", command=self.enroll)
        self.bt.grid(row=6, column=30)
        self.bs = Button(self, text="BAck", command=self.back)
        self.bs.grid(row=0, column=30)

    def back(self):
        self.destroy()
        '''from eventmanage.eventsHome import home
        #Toplevel(home).mainloop()
        #home().mainloop()'''
        import eventmanage.eventsHome as hm
        hm.home().mainloop()

    def enroll(self):
        try:
            con = connect('localhost', 'root', '', 'avscollege')
            qry = """insert into events(edate,ename,edept,eorg,prize) values('%s','%s','%s','%s',%d)""" % (
                self.date.get(), self.name.get(), self.dept.get(), self.org.get(), int(self.prize.get()))
            cur = con.cursor()
            out = cur.execute(qry)
            if out != 0:
                messagebox.showinfo("Status", "Event added to base")
            else:
                messagebox.showinfo("Status", "Event not added to base")
        except Exception as e:
            con.rollback();print(e)
        finally:
            con.close()

'''
n = neweve()
n.mainloop()'''
