class Deal:
    __seller=""
    __buyer=""
    __value=0
    def __init__(self,s="",b="",v=0):
        print("Deal called")
        self.__seller=s;self.__buyer=b;self.__value=v
    def __str__(self):return self.__seller+" "+self.__buyer+" "+str(self.__value)+"\n"
    def setSeller(self,sel):self.__seller=sel
    def getSeller(self):return self.__seller
    def setBuyer(self,buy):self.__buyer=buy
    def getBuyer(self):return self.__buyer
    def setValue(self,val):self.__value=val
    def getValue(self):return self.__value

'''d1=Deal()
d1.setSeller("Lilavathi")
d1.setBuyer("Muthhu")
d1.setValue(1717000)
print(d1.getSeller(),d1.getBuyer(),d1.getValue())
d2=Deal("Annamalai","Mani",3500000)
print(d2)
d3=Deal(s="Jayanthi",b="Monika")
d3.setValue(1700)
print(d3.getSeller(),d3.getValue())'''