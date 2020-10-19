import numpy as num

# flat,flatten>> single

box1=num.arange(50,66).reshape(4,4)

print(box1)

print(box1[0][1])
print(box1[0])

print(box1.flat[0])

print(box1.flat[13])

# flatten

box2=box1.flatten("C")

print(box2)

box3=box1.flatten("F")

print(box3)