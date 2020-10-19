import numpy as num

alpha=num.array([(1,2,3,4),(6,9,10,45),(88,45,11,90)])

for x in alpha:print(x)
print("C style")
for x in num.nditer(alpha):print(x) #C style
print(alpha)
print("Fortran style")
for x in num.nditer(alpha,order="F"):print(x)