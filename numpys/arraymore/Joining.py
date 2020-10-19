# joining array:

import numpy as num

box1=num.arange(50,66).reshape(4,4)

box2=num.arange(125,141).reshape(4,4)

print(box1,"\n",box2)

# Concat
conJoin=num.concatenate((box1,box2))

print(conJoin.shape)

conJoinV=num.concatenate((box1,box2),1)

print(conJoinV)


#stack
stkJoin=num.stack((box1,box2))

print(stkJoin)

stkJoin2=num.stack((box1,box2),1)
print(stkJoin2)

#hstack
hstkJoin=num.hstack((box1,box2))
print(hstkJoin)

#vstack
vstkJoin=num.vstack((box1,box2))
print(vstkJoin)