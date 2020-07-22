# Synchronization
from threading import Thread, Lock


class Theatre(Thread):
    def __init__(self,nm):
        Thread.__init__(self)
        self.name=nm
    def run(self):
        print(self.name+" to get a ticket")
        hold.acquire()
        price=int(input("Tell us Price: "))
        if price>=250:print(self.name,"got ticket")
        else:print(self.name," doesn't get the ticket")
        hold.release()
        print(self.name+" has left the counter")

hold=Lock()

t1=Theatre("Abinav")
t2=Theatre("Bindiya")
t3=Theatre("Cavin")
t4=Theatre("Danny")
t1.start()
t2.start()
t3.start()
t4.start()
