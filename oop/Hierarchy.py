# Hierarchy inheritance:
from array import *

class Stocks:
    products=array('i')
    def show(self):print("Products are: ",self.products)

class Jaysurya(Stocks):
    def __init__(self,hey):
        self.products=array('i')
        self.products.extend(hey)
    def search(self):
        budget=int(input("Enter the price you wish to search:"))
        for x in self.products:
            if x<=budget:print(x)
class Reliance(Stocks):
    def __init__(self,hai):
        self.products = array('i')
        self.products.extend(hai)
    def getByPosition(self,start,stop):
        print(self.products[start:stop])

'''j=Jaysurya([12000,4500,600,300,1000,500])
r=Reliance([1400,5600,1200,500,300,400,1000,5000,8000,900,13000])

j.search()
r.getByPosition(0,5)

j.show()
r.show()'''