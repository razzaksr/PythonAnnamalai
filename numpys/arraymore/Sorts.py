# sort:quick(1),heap(3),merge(2), nonzero, where, extract

import numpy as num

data=num.array([(12,45,1),(98,11,45),(19,9,34)])

print(data)

#sorting
print(num.sort(data))
print(num.sort(data,axis=0))
print(num.sort(data,axis=1))

#non zero
#print(num.nonzero(data))

#cond=(data%5==0)
#where
print(num.where(data%5==0))

#extract
print(num.extract(data,data%2==0))