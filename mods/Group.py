# array module
from array import *
grp1=array('i',[12,89,-1,-31,-1])
print(grp1)
#appending
grp1.append(34);print(grp1)
#add by index
grp1.insert(2,987)
print(grp1)
#read
print(grp1.index(-31))
#duplicates
print(grp1.count(-1))
#delete by pop
print(grp1.pop())
#delete by remove
grp1.remove(-1)
print(grp1)
# delete bt del
del grp1[0]
print(grp1[0])
#slicing
print(grp1[1:3])
#iterating
for x in grp1:print(x)