# splits: split,hsplit,vsplit

import numpy as num

circle=num.arange(250,300)

print(circle)

normalSplit=num.split(circle,5)
for x in normalSplit:print(x)

# split with specified between start and end
normalSplitSpecific=num.split(circle,(5,7))
for x in normalSplitSpecific:print(x)

#hsplit
horiSplit=num.hsplit(circle,10)
for x in horiSplit:print(x)

#vsplit
veriSplit=num.hsplit(circle,5)
for x in veriSplit:print(x)
