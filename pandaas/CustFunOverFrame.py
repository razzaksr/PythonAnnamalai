# Custom function over the data frame
'''
pipe
apply
applymap
'''

import pandas as pan
import numpy as num

def yet(seg1,seg2):
    return seg1+seg2

def diff(seg1,seg2):
    seg1-=(seg1*seg2)/100
    return seg1

frame=pan.DataFrame(num.random.randn(5,3),columns=["team1","team2","team3"],index=["IRCTC","PassportSeva","TNePass","Flipkart","GPay"])
print(frame)

tabWise=frame.pipe(yet,2)
print(tabWise)

tabWiseMod=frame.pipe(diff,10)
print(tabWiseMod)

print(frame.apply(num.mean))
print(frame.apply(num.mean,axis=1))

tmp={"team1":pan.Series([5.6,1.2,9.1,8.9,4.5]),
     "team2":pan.Series([8.9,2.1,4.5,2.1,9.1]),
     "team3":pan.Series([8.9,2.1,9.1,4.5,4.5])}

frame=pan.DataFrame(tmp)

print(frame)

def hell(one):
    dup=[]
    h=tuple(one)
    for o in h:
        p=[]
        if h.count(o) >1:
            p.append(o)
        dup.append(p)
    return dup

print("Duplicates as column wise: \n",frame.apply(hell))
print("Duplicates as row wise: \n",frame.apply(hell,axis=1))

print(frame)

def show(each):
    print(each)
    #for x in each:print(x,end=" ")

def hike(ind):
    if ind >=2 and ind<=7:ind+=(ind*0.10)
    return ind

#frame.applymap(show)
print(frame)
rate=frame.applymap(hike)
print(rate)

frame.applymap(lambda x:print(x))