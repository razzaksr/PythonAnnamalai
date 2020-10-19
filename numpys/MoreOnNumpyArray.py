import numpy as num

numvar=num.array([(12,45,90,120),(9,98,45,93),(77,12,10,9),(78,1,25,7)])

print(numvar[0])
#[start:end,column]
print(numvar[:,2])

print(numvar[0,1])

print(numvar[0:2,0:2])

for x in numvar[0]:print(x)

#Update
inp1=int(input("Tell us first range: "))
inp2=int(input("Tell us second range: "))

for each in range(len(numvar)):
    for data in range(len(numvar[each])):
        if numvar[each,data]>=inp1 and numvar[each,data]<=inp2:
            numvar[each,data]*=numvar[each,data]
        print(numvar[each,data])