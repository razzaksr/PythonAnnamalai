# Multiple Inheritance

class Finance:
    loans={"HL":5.5,"PL":3,"EL":5,"BL":8}
    def __str__(self):
        return str(self.loans)
class Eligible:
    def check(self):
        if self.ctc>= 2 and self.ctc<4:
            return "PL"
        elif self.ctc>= 4 and self.ctc<8:
            return "EL"
        elif self.ctc>= 8 and self.ctc<=10:
            return "HL"
        elif self.ctc>=10:
            return "BL"
        else:print("Not eligible for any loan"); return ""
# multiple inheritance
class Bajaj(Finance,Eligible):
    def addNew(self):
        loanName=input("Tell us new loan scheme : ")
        loanValue=float(input("Tell us loan value: "))
        self.loans[loanName]=loanValue
        print("New loan added by Bajaj")
    def display(self):
        self.ctc=int(input("Tell us your monthly salary: "))
        temp=self.check()
        print("possible to provide is: ",temp,"Value is",self.loans[temp])

b=Bajaj()
b.display()
b.addNew()
print(b.loans)
