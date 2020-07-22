# Hybrid: Combination of any two inheritance
from oop.Hierarchy import Reliance, Jaysurya

class Retail(Jaysurya,Reliance):
    def __init__(self,hai):
        print("Dealer gonna deliver the items")
        super(Jaysurya,self).__init__(hai)
        print("Dealer has sent items to Jaysurya")

r=Retail([800,100,300,500,1200,78000,45000,1000,1900,900,409])
r.getByPosition(0,4)
r.search()