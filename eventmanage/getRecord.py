# Getting records

from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox

from pymysql import *

class recordRead(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Getting records")
        self.geometry("500x400")
        p1 = PhotoImage(file="C:\\Users\\DOLL\\PycharmProjects\\MorningBatch\\eventmanage\\bday.ico")
        self.iconphoto(False, p1)
        self.head=Label(self,text="Fetch by following options",font=('Times New Roman',30))
        self.head.grid(row=0,column=10)
        self.combo=Combobox(self)
        self.combo['values']=['Everything','edate','eid','ename','edept','eorg','prize','winner','participants']
        self.combo.grid(row=1,column=6)
        self.bt=Button(self,text="GetData",command=self.fetch)
        self.bt.grid(row=2,column=30)

        self.spec = Combobox(self)
        self.spec['values'] = ['edate', 'eid', 'ename', 'edept', 'eorg', 'prize', 'winner',
                                'participants']
        self.spec.grid(row=3, column=6)
        self.men=Entry(self,width=20)
        self.men.grid(row=3,column=30)
        self.bt = Button(self, text="GetOne", command=self.read)
        self.bt.grid(row=3, column=60)
        self.hai = scrolledtext.ScrolledText(self, width=100, height=10)
        self.hai.grid(row=4, column=10)
        self.bs = Button(self, text="BAck", command=self.back)
        self.bs.grid(row=0, column=30)

    def back(self):
        self.destroy()
        #from eventmanage.eventsHome import home
        import eventmanage.eventsHome as hm
        hm.home().mainloop()
    def read(self):
        self.hai.insert(0.1, "")
        temp="Event id\tEventName\tEventDate\tEventDepartment\tEventOrganizer\tEventParticipants\tEventWinner\tPrize\n"
        try:
            con = connect("localhost", "root", "", "avscollege")
            cur = con.cursor()
            if self.spec.get()!='participants':qry="select * from events where "+self.spec.get()+"='"+self.men.get()+"'"
            else:qry="select * from events where "+self.spec.get()+" like'%"+self.men.get()+"%'"
            cur.execute(qry)
            ware = cur.fetchall()
            for x in ware:
                temp+=str(x[0])+"\t"+x[1]+"\t"+str(x[2])+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+str(x[7])+"\n"
            self.hai.delete(0.1,END)
            self.hai.insert(0.1,temp)
            con.close()
        except Exception as e:print(e)
    def fetch(self):
        self.hai.insert(0.1,"")
        temp="Event id\tEventName\tEventDate\tEventDepartment\tEventOrganizer\tEventParticipants\tEventWinner\tPrize\n"
        try:
            con = connect("localhost", "root", "", "avscollege")
            cur = con.cursor()
            if self.combo.get() == 'Everything':
                qry = "select * from events"
                cur.execute(qry)
                ware = cur.fetchall()
                for x in ware:
                    temp+=str(x[0])+"\t"+x[1]+"\t"+str(x[2])+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+str(x[7])+"\n"
            elif self.combo.get()!='Everything':
                qry="select %s from events"%(self.combo.get())
                cur.execute(qry)
                ware = cur.fetchall()
                for x in ware:
                    temp += str(x[0]) + "\n"
            self.hai.delete(0.1,END)
            self.hai.insert(0.1,temp)
            con.close()
        except Exception as e:print(e)

'''
rec=recordRead()
rec.mainloop()'''
