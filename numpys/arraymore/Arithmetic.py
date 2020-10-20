import numpy as num

cabinA=num.arange(11,31).reshape(5,4)
cabinB=num.arange(66,86).reshape(5,4)

print(cabinA,"\n",cabinB)

added=num.add(cabinA,cabinB)

print("Added \n",added)

subtracted=num.subtract(cabinB,cabinA)
print("Subtracted \n",subtracted)

multiplied=num.multiply(cabinA,cabinB)
print("Multiplied \n",multiplied)

divided=num.divide(cabinB,cabinA)
print("Divided \n",divided)