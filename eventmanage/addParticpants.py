# adding participants to the event

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *

class partAdd(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Adding particpants")
        self.geometry("500x300")
        self.head=Label(self,text="Adding new particpants",font=('Times New Roman',20))
        self.head.grid(row=0,column=10)
        self.selectId=Label(self,text="Select Event id to add particpants")
        self.selectId.grid(row=1,column=8)
        self.ids=Combobox(self)
        try:
            con = connect('localhost', 'root', '', 'avscollege')
            qry = "select eid from events where winner=''"
            cur = con.cursor()
            cur.execute(qry)
            pack=cur.fetchall()
            self.ids['values']=pack
            con.close()
        except Exception as e: print(e)
        self.ids.grid(row=1, column=30)
        self.bt = Button(self, text="Read", command=self.show)
        self.bt.grid(row=1, column=50)
        self.one = Label(self, text="")
        self.one.grid(row=2, column=6)
        self.typepart=Label(self,text="Adding new particpant here")
        self.typepart.grid(row=3,column=6)
        self.part=Entry(self)
        self.part.grid(row=3,column=30)
        self.en=Button(self,text="Add",command=self.update)
        self.en.grid(row=4,column=10)
    def show(self):
        con = connect('localhost', 'root', '', 'avscollege')
        qry = "select edate,ename,edept from events where eid=%d" % (int(self.ids.get()))
        cur = con.cursor()
        cur.execute(qry)
        pack = cur.fetchone()
        con.close()
        self.one.configure(text="Choosen events is: "+str(pack[0])+" "+str(pack[1])+" "+str(pack[2]))
    def update(self):
        self.temp = ""
        con = connect('localhost', 'root', '', 'avscollege')
        read = "select participants from events where eid=%d" % (int(self.ids.get()))
        cur=con.cursor()
        cur.execute(read)
        exists = cur.fetchall()
        for x in exists[0]:
            self.temp += x  # +"/"
        self.temp += self.part.get() + "/"
        con.autocommit(True)
        qry = "update events set participants='%s' where eid=%d" % (self.temp, int(self.ids.get()))
        res=cur.execute(qry)
        if res!=0:messagebox.showinfo("Status","Participant "+self.part.get()+" added")
        else:messagebox.showinfo("Status","Participant "+self.part.get()+" not added")
        con.close()

'''p=partAdd()
p.mainloop()'''