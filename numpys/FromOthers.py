import numpy as num

hai=[["hello","java"],["python","be"],["as","brothers"]]
var=num.asarray(hai)
print(var.shape)
var=var.reshape(2,3)
print(var)

var=num.append(var,[["Zealous","Tech","Corp"]],0)

var=num.insert(var,[1],[["Candidate"],["Salem"],["Tamilnadu"]],1)

print(var)