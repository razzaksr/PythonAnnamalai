# overview of pandas

import pandas as pan
import numpy as num

data=num.array([14,15,16])
print("Numpy representaion:\n",data)
print(data[1])

check=pan.Series(data,index=['alpha','beta','cosmo'])

print("Pandas representation:\n",check)
print(check['cosmo'])

map={"or1":3.5,"or2":4.2,"or3":2.8}
check=pan.Series(map)
print(check)

delta=[[636001,"Razak Mohamed"],[636006,"Annamalai"],[624408,"Meharaj"]]
frame=pan.DataFrame(delta,columns=["PinCode","Person Name"],index=["resource1","resource2","resource3"])
print(frame)

eclairs={"Models":["CT100","Vikrant","Platina","Avenger"],"Prices":[69000,89000,72000,108000]}
frame=pan.DataFrame(eclairs)
print(frame)