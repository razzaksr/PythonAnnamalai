# Getting records

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *

class record(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Getting records")
        self.geometry("500x400")
        p1 = PhotoImage(file="C:\\Users\\DOLL\\PycharmProjects\\MorningBatch\\eventmanage\\bday.ico")
        self.iconphoto(False, p1)
        self.head=Label(self,text="Fetch by following options")#,font=('Times New Roman',30))
        self.head.grid(row=0,column=0)

        self.spec = Combobox(self)
        self.spec['values'] = ['edate', 'eid', 'ename', 'edept', 'eorg', 'prize', 'winner',
                                'participants']
        self.spec.grid(row=2, column=0)
        self.men=Entry(self)
        self.men.grid(row=2,column=1)
        self.bt = Button(self, text="GetOne", command=self.read)
        self.bt.grid(row=2, column=2)

    def read(self):
        self.f1=font=('Times New Roman',12,'bold')
        self.f2 = font = ('Times New Roman', 11, 'italic')
        self.h1=Entry(self,font=self.f1);self.h1.insert(END,"Event Id");self.h1.grid(row=5,column=0)
        self.h2 = Entry(self, font=self.f1);self.h2.insert(END, "Event Name");self.h2.grid(row=5, column=1)
        self.h3 = Entry(self, font=self.f1);self.h3.insert(END, "Event Date");self.h3.grid(row=5, column=2)
        self.h4 = Entry(self, font=self.f1);self.h4.insert(END, "Event Department");self.h4.grid(row=5, column=3)
        self.h5 = Entry(self, font=self.f1);self.h5.insert(END, "Event Organizer");self.h5.grid(row=5, column=4)
        self.h6 = Entry(self, font=self.f1);self.h6.insert(END, "Event Participants");self.h6.grid(row=5, column=5)
        self.h7 = Entry(self, font=self.f1);self.h7.insert(END, "Event Winner");self.h7.grid(row=5, column=6)
        self.h8 = Entry(self, font=self.f1);self.h8.insert(END, "Event Prize");self.h8.grid(row=5, column=7)
        try:
            con = connect("localhost", "root", "", "avscollege")
            cur = con.cursor()
            if self.spec.get()!='participants':qry="select * from events where "+self.spec.get()+"='"+self.men.get()+"'"
            else:qry="select * from events where "+self.spec.get()+" like'%"+self.men.get()+"%'"
            cur.execute(qry)
            ware = cur.fetchall()
            lin=6
            for rows in range(len(ware)):
                for each in range(len(ware[rows])):
                    self.data=Entry(self,font=self.f2)
                    self.data.insert(END,ware[rows][each])
                    self.data.grid(row=lin,column=each)
                lin+=1
            con.close()
        except Exception as e:messagebox.showinfo("Error",e)

rec=record()
rec.mainloop()