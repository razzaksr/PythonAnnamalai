from array import *

import numpy as num

var=array('i',[])
var.append(12)
var.append(45)
var.insert(0,77)
print(var[0])
var[1]+=40
var.pop(0)
var.remove(45)
print(var)

numvar=num.array([(12,45,90),(98,45,45),(77,10,9),(1,25,7)])
print(numvar.shape)
print(numvar)
numvar=numvar.reshape(3,4)
print(numvar)
print(numvar.size)
print(numvar.itemsize)

#adding new row
numvar=num.append(numvar,[[66,55,44,33]],0)
print(numvar)

#adding new column
numvar=num.append(numvar,[[1],[2],[3],[4]],1)
print(numvar)

#inserting one row @ position
numvar=num.insert(numvar,[2],[[2,4,6,8,10]],0)
print("After insertion @ 2:\n",numvar)

#inserting new columns @ position
numvar=num.insert(numvar,[1],[[7],[14],[21],[28],[35]],1)
print("After insertion @ 1th columns\n",numvar)