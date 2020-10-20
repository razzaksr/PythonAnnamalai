import numpy as num

'''
64 32 16 8 4 2 1
0  0  0  1 0 1 1 >> 11
1  0  0  0 0 1 0 >> 66
0  0  0  0 0 1 0 >> 2
'''

cabinA=num.arange(11,31).reshape(5,4)
cabinB=num.arange(66,86).reshape(5,4)


#print("Binaries of cabin A\n",num.binary_repr(cabinA,width=8))
#print("Binaries of cabin B\n",num.binary_repr(cabinB,width=8))

# binary &

And=num.bitwise_and(cabinA,cabinB)
print("& result\n",And)

Or=num.bitwise_or(cabinA,cabinB)
print("| result\n",Or)

Xor=num.bitwise_xor(cabinA,cabinB)
print("^ result\n",Xor)

left=num.left_shift(cabinA,4)
print("Left shift result\n",left)

right=num.right_shift(cabinB,4)
print("Right shift result\n",right)