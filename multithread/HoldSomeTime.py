# Perform something over specific thread
import threading
import time
from threading import Thread, Lock


class Operate(Thread):
    _option={"Cognizant":4.5,"Wipro":3.9,"Infosys":3.5,
             "Amazon":8.2,"Capegemini":5.1,
             "Accenture":3.8,"InfoView":6.5}
    def __init__(self,nm):
        Thread.__init__(self)
        self.name=nm
    def check(self):
        try:
            comp = input("Tell us company name:" + self.name)
            self._option[comp]
            print(self._option[comp])
        except KeyError as key:
            if self.name == "Satheesh": return 0
            if self.name == "Vikas":
                print(self.name,"has to wait some time");time.sleep(5)
            expected=float(input("Tell us expected salary: "+comp))
            self._option[comp]=expected
            print(self.name+" added new company in the campus")
    def run(self):
        hold.acquire()# lock gonna activate
        if self.check()==0:del self
        hold.release()# lock deactivate

hold=Lock()

op1=Operate("Vikas")
op2=Operate("Satheesh")
op3=Operate("Vinayak")
op4=Operate("Mohamed")
op1.start()
op2.start()
op3.start()
op4.start()
