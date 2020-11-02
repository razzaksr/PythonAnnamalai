# Matrix Library: empty, zeros, ones, eye, identity, rand

import numpy.matlib
import numpy as num

matEmt=num.matlib.empty((3,2))
print(matEmt)

matOne=num.matlib.ones((4,2))
print(matOne)

matZero=num.matlib.zeros((6,3))
print(matZero)

matIden=num.matlib.identity(5,dtype=float)
print(matIden)

matRand=num.matlib.rand((10,3))
print(matRand)

matEye=num.matlib.eye(n=5,M=4,k=0,dtype=int)
print(matEye)

arr=num.asarray(matEye)
print(arr)

arr=num.arange(1,10).reshape(3,3)
mat=num.asmatrix(arr)
print(mat)