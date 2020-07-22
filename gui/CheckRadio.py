# Check box and radio button

from tkinter import *
from tkinter import messagebox

win=Tk()
win.title("Items Options")
win.geometry("500x300")

c1=BooleanVar();c1.set(False);check1=Checkbutton(win,var=c1,text="Kabab Chicken")
check1.grid(row=0,column=0)
c2=BooleanVar();c2.set(False);check2=Checkbutton(win,var=c2,text="Chicken Tikka")
check2.grid(row=0,column=1)
c3=BooleanVar();c3.set(False);check3=Checkbutton(win,var=c3,text="Paneer Tikka")
check3.grid(row=0,column=2)
c4=BooleanVar();c4.set(False);check4=Checkbutton(win,var=c4,text="Butter Masala")
check4.grid(row=0,column=3)

def order():
    messagebox.showinfo("Summary",format(c1.get())+" "+format(c2.get())+" "+
                        format(c3.get())+" "+format(c4.get()))
def pay():
    messagebox.showinfo("Payment choosen is:",str(radiovar.get()))

b1=Button(win,text="Place Order",command=order)
b1.grid(row=1,column=0)

lbl=Label(win,text="Payment mode")
lbl.grid(row=2,column=0)

radiovar=StringVar();radiovar.set("")
radio1=Radiobutton(win,var=radiovar,value="Card",text="Credit/Debit card",command=pay)
radio1.grid(row=3,column=0)
radio2=Radiobutton(win,var=radiovar,value="UPI",text="Bhim Upi mode",command=pay)
radio2.grid(row=3,column=1)
radio3=Radiobutton(win,var=radiovar,value="Wallet",text="Google pay/ Amazon pay",command=pay)
radio3.grid(row=3,column=2)
radio4=Radiobutton(win,var=radiovar,value="Cod",text="Cash on delivery",command=pay)
radio4.grid(row=3,column=3)

win.mainloop()
