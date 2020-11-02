# Copies and views

import numpy as num

arr=num.arange(97,117).reshape(5,4)

print(arr)

bar=arr # typical copy
print("Copied array\n",bar)

#bar[0][3]*=2
bar.shape=4,5

print("Copied array\n",bar)
print("Original array\n",arr)

print(id(arr),id(bar))

# view : keep original shape as it is
car=arr.view()

print("Second Copy by View\n",car)

car.shape=5,4

print("Second Copy by View after reshape\n",car)
print("Original array\n",arr)
print("ID\n",id(arr),id(car))

dare=arr.copy()
print("Original array\n",arr)
print("Third Copy by View\n",dare)

dare[0][3]*=2
print("Third Copy by View\n",dare)
print("Original array\n",arr)
print("ID\n",id(arr),id(dare))