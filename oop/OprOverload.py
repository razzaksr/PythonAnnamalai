# Operator overloading
from oop.Encaps import Deal

d1=Deal("Razak","Mohamed",1000000)
d2=Deal("Razak","Rasheedha",100897)
d3=Deal("Mohamed","Sabari",10009800)

class Active:
    def __init__(self):self.total=[]
    def __add__(self, other):
        for x in self.total:
            for y in other.total:
                if x.getBuyer()==y.getBuyer() or x.getSeller()==y.getSeller() \
                        or x.getBuyer()==y.getSeller() \
                        or y.getBuyer()==x.getSeller()==y.getBuyer():
                    print(x,y)
    def __mul__(self, other):
        suma=0
        for x in self.total:
            #print(x)
            suma+=x.getValue()
        sumb=0
        for y in other.total:
            #print(y)
            sumb+=y.getValue()
        print(suma,sumb)


a=Active()
a.total.append(d1)
a.total.append(d2)
a.total.append(d3)


d4=Deal("Lilavathi","Sabari",1717000)
d5=Deal("Annamalai","Razak",3500000)
d6=Deal("Jayanthi","Rasheedha",1700)
b=Active()
b.total.append(d4)
b.total.append(d5)
b.total.append(d6)
a+b
#a*b
