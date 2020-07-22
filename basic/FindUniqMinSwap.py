yet=[4,9,2,4,2,12,89,11,77]
print(yet)
fmin,smin=max(yet),max(yet)
for say in yet:
    if yet.count(say)==1:
        if say < fmin : smin = fmin;fmin = say
        elif say < smin and smin != fmin: smin = say
print(fmin,smin)
#swapping
one=yet.index(fmin)
two=yet.index(smin)
yet[one]*=yet[two]
yet[two]=yet[one]//yet[two]
yet[one]//=yet[two]
print(yet)