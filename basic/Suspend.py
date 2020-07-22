from threading import Thread, Lock


class ATM(Thread):
    balance=[500000]
    def __init__(self,name):
        super().__init__()
        self.name=name
    def debit(self):
        required = int(input("Tell us required amount to debit:" + self.name))
        if self.balance[0] >= required:
            self.balance[0] -= required
            print(required, " debited by", self.name)
        else:
            print(self.name, "Going to suspend")
            return 0
        print(self.balance[0])
    def run(self):
        stable.acquire()
        if self.debit()==0:del self
        stable.release()

stable=Lock()

a1=ATM("Annamalai")
a2=ATM("Meguraj")
a3=ATM("Raji")
a4=ATM("Aravind")
a1.start()
a2.start()
a3.start()
a4.start()