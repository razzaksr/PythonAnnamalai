# amax, amin, median, percentile, ptp, average

# axis=0>> column wise, axis=1 >> row wise

import numpy as num

data=num.arange(65,90).reshape(5,5)

print(data)

'''# amax, amin
print(num.amax(data))
print(num.amin(data))

print(num.amax(data,axis=0))
print(num.amax(data,axis=1))'''

# peek to peek
print(num.ptp(data))
print(num.ptp(data,axis=0))
print(num.ptp(data,axis=1))

'''#average
print(num.average(data))
print(num.average(data,axis=1))
print(num.average(data,axis=0))'''

'''#median
print(num.median(data))
print(num.median(data,axis=1))
print(num.median(data,axis=0))'''

'''#percentile: for example 5X5 row of 0th row 0th col is 0 row 4th col is 100% asp er axis 1

  0  25 50 75 100
0  [[65 66 67 68 69]
25 [70 71 72 73 74]
50 [75 76 77 78 79]
75 [80 81 82 83 84]
100[85 86 87 88 89]]

print(num.percentile(data,50))
print(num.percentile(data,35,axis=0))
print(num.percentile(data,60,axis=1))'''
