# linear algiebra: dot, vdot, matmul, det, inner

import numpy as num
import numpy.linalg

alpha=num.array([(2,5),(1,2)])
beta=num.array([(10,20),(30,10)])
cosmo=num.array([1,2])
delta=num.array([10,20])
print("Alpha\n",alpha)
print("Beta\n",beta)
print("Cosmo\n",cosmo)
print("Delta\n",delta)
# dot
#print(num.dot(alpha,beta))

#vdot
#print(num.vdot(alpha,beta))

#matmul
#print("alpha*cosmo\n",num.matmul(alpha,cosmo))
#print("alpha*beta\n",num.matmul(alpha,beta))

#inner
#print("Comso inner delta\n",num.inner(cosmo,delta))
#print("Alpha inner beta\n",num.inner(alpha,beta))


eclairs=num.array([(1,2,3),(4,5,6),(7,8,9)])
froyo=num.array([(2,4,6),(1,3,5),(8,6,4)])

#det
print(eclairs)
print(int(num.linalg.det(eclairs)))

print(froyo)
print(int(num.linalg.det(froyo)))

print(beta)
print(int(num.linalg.det(beta)))