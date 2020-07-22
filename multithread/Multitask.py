# multi task multi thread
from threading import Thread


class CDM(Thread):
    money=1000
    def __init__(self,nm):
        Thread.__init__(self)
        self.name=nm
    def run(self):
        amt=int(input("Tell us amount to deposite "+self.name+": "))
        self.money+=amt
        print(amt," deposited by: ",self.name)
class ATM(Thread):
    balance=40000
    def __init__(self,nm):
        Thread.__init__(self)
        self.name=nm
    def run(self):
        amt = int(input("Tell us amount to withdraw " + self.name + ": "))
        if self.balance>=amt:self.balance -= amt;print(amt , " debited by: ", self.name)
        else: print("Can't withdraw")

a=CDM("Hari")
a1=CDM("Victor")
b=ATM("Annamalai")
b1=ATM("Raji")
a.start();a.join()
a1.start()
b.start();b.join()
b1.start()


