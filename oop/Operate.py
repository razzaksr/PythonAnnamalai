# performing search over the Deal
from oop.Encaps import Deal

d1=Deal("Razak","Mohamed",1000000)
d2=Deal("Razak","Rasheedha",100897)
d3=Deal("Mohamed","Sabari",10009800)

class Search:
    one = []
    def find(self,s="",b="",v=0):
        if s=="" and b=="":
            print(v," transaction based search")
            for x in self.one:
                if x.getValue()>=v:print(x)
        elif s=="" and v==0:
            print(b, " buyer based search")
            for x in self.one:
                if x.getBuyer()== b: print(x)
        elif b=="" and v==0:
            print(s, " seller based search")
            for x in self.one:
                if x.getSeller()== s: print(x)
sh1=Search()
sh1.one.append(d1)
sh1.one.append(d2)
sh1.one.append(d3)

sh1.find(s="Razak")
sh1.find(b="Mohamed")
sh1.find(v=1000000)