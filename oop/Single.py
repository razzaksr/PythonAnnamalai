# Single Inheritance with overriding
from oop.Encaps import Deal


class Enroll(Deal):
    def __init__(self,s,b,v):
        print("Constructor of Enroll called")
        super().__init__(s,b,v)
    def __str__(self):
        print(super().__str__())
        return self.getBuyer()

e=Enroll("Razak","Sabari",100)
print(e)