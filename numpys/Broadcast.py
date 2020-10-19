import numpy as num

alpha=num.array([(1,2,3,4),(6,9,10,45),(88,45,11,90)])
print(alpha,alpha.shape)
beta=num.array([(10,20,30,40)])
print(beta,beta.shape)

cosmo=alpha+beta;

print(cosmo)

delta=num.array([(100,200,300)])
delta=delta.T
print(delta,delta.shape)

eclipse=cosmo+delta
print(eclipse)