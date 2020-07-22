# Multithread behave
import threading
from threading import Thread


class Calaway(Thread):
    data=[12,8,9,1,0,3,4,7,9,1,2,4,0,7,2,6,4,9,12,8]
    def __init__(self, nm,ind):
        Thread.__init__(self)
        self.name = nm
        self.pos=ind

    def run(self):
        print(threading.currentThread().name, "came inside")
        print("Required data by given position",self.pos,"=",self.data[self.pos])


c = Calaway("Raji",0)
d=Calaway("Meguraj",11)
e=Calaway("Aravind",9)
c.start()
print(c.isAlive())
c.join()
d.start()
d.join()
print(c.isAlive());e.start()
