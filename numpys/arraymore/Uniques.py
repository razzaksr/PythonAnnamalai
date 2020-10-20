# Finding uniques

import numpy as num

alpha=num.arange(90,120).reshape(5,6)

print("Before Insertion: \n",alpha)

#insertion
alpha=num.insert(alpha,[2],[[93],[97],[105],[110],[116]],1);

print(alpha)

beta=num.unique(alpha)

print(beta)

cosmo,positions=num.unique(alpha,return_index=True)

print(positions)