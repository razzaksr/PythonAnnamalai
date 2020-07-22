# announce winner

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *


class winDec(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Declaring winner")
        self.geometry("500x300")
        self.head = Label(self, text="Announcement of winner", font=('Times New Roman', 20))
        self.head.grid(row=0, column=10)
        self.selectId = Label(self, text="Select Event id to see the details")
        self.selectId.grid(row=1, column=8)
        self.ids = Combobox(self)
        try:
            con = connect('localhost', 'root', '', 'avscollege')
            qry = "select eid from events where winner='' and participants !=''"
            cur = con.cursor()
            cur.execute(qry)
            pack = cur.fetchall()
            self.ids['values'] = pack
            con.close()
        except Exception as e:
            print(e)
        self.ids.grid(row=1, column=30)
        self.bt = Button(self, text="Read", command=self.show)
        self.bt.grid(row=1, column=50)
        self.one = Label(self, text="")
        self.one.grid(row=2, column=6)

    def show(self):
        con = connect('localhost', 'root', '', 'avscollege')
        qry = "select edate,ename,edept,participants from events where eid=%d" % (int(self.ids.get()))
        cur = con.cursor()
        cur.execute(qry)
        pack = cur.fetchone()
        self.one.configure(text="Choosen events is: " + str(pack[0]) + " " + str(pack[1]) + " " + str(pack[2]))
        hai=pack[3]
        hello=hai.split("/")
        pos=10
        self.result=StringVar();self.result.set("")
        for x in (hello):
            if x!="":
                each=Radiobutton(self,text=x,value=x,var=self.result,command=self.declare)
                each.grid(row=pos,column=30)
                pos+=1

    def declare(self):
        try:
            con = connect("localhost", "root", "", "avscollege")
            cur = con.cursor()
            qry = "update events set winner='"+self.result.get()+"' where eid="+self.ids.get()
            yet=cur.execute(qry)
            con.commit()
            print(yet)
            if yet!=0:
                messagebox.showinfo("Status", "Winner declared")
            else:messagebox.showinfo("Error","Not declared")
            con.close()
        except Exception as e:
            messagebox.showinfo("Error",e)


'''w = winDec()
w.mainloop()'''
