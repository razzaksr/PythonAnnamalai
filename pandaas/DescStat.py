# descriptive statistics: describe: mean, sum,min,max,size
import pandas as pan
res={
    "Expert Name":pan.Series(["Razak","Mahesh","Murali","Sobin","Venkat"]),
    "Expert domain":pan.Series(["Java","C","C++","Data Scientist","Dot Net"]),
    "Expert Experience":pan.Series([9,15,4,3,12]),
    "Expert Commercial":pan.Series([14.5,10.9,10.3,18.5,9.3])
};

zeal=pan.DataFrame(res)
print(zeal)
print(zeal.describe())
print(zeal.describe(include='object'))

print(zeal.sum(1))