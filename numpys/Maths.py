# sin, cos, tan arcsin, arccos, arctan, floor, ceil, around

import numpy as num

ran=num.array([0,30,45,60,90])

sinRes=num.sin(ran*num.pi/180)
cosRes=num.cos(ran*num.pi/180)
tanRes=num.tan(ran*num.pi/180)

'''revSin=num.arcsin(sinRes)
print(sinRes)
print(num.degrees(revSin))

revCos=num.arccos(cosRes)
print(cosRes)
print(num.degrees(revCos))

revTan=num.arctan(tanRes)
print(tanRes)
print(num.degrees(revTan))'''

hai=num.array([0.02,3.3,4.59,6.96563,-0.9])
print(hai)

print(num.around(hai))
print(num.floor(hai))
print(num.ceil(hai))