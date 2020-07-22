# Multi level inheritance
from oop.Encaps import Deal

class Enroll(Deal):
    def __init__(self,s,b,v):
        print("Constructor of Enroll called")
        super().__init__(s,b,v)
    def __mod__(self, other):
        print(self.getValue()+other.getValue())
class Scored(Enroll):
    def __init__(self,a,b,c):
        print("Scored initiated")
        super().__init__(a,b,c)

s=Scored("Meguraj","Annamalai",98000000)
print(s)
t=Scored("Mani","Visu",6788756)
print(t)
t%s