# Operator overloading based credit/ debit

class Bank:
    def __init__(self,num=0,bal=0.0,trans=0):
        self.__accNo=num
        self.__accBal=bal
        self.__trans_count=trans
    def __str__(self):
        return str(self.__accNo)+" "+str(self.__accBal)+" "+str(self.__trans_count)+"\n"
    def __add__(self, other):
        self.__accBal+=other
        self.__trans_count+=1
        print("Amount",other,"credited to ",self.__accNo)
    def __sub__(self, other):
        self.__trans_count += 1
        if other<=self.__accBal:
            self.__accBal-=other
            print("Amount", other, "debited from ", self.__accNo)
        else:print("Insufficient balance in ",self.__accNo)


vikas=Bank(987656745,35000.8)
print(vikas)
vikas+10000
vikas-2000
print(vikas)
vinay=Bank(456789789,1876.7)
print(vinay)
vinay-1000
vinay-900
print(vinay)
