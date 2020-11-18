import pandas as pan

res={
    "Expert Name":pan.Series(["Razak","Mahesh","Murali","Sobin","Venkat"]),
    "Expert domain":pan.Series(["Java","C","C++","Data Scientist","Dot Net"]),
    "Expert Experience":pan.Series([9,15,4,3,12]),
    "Expert Commercial":pan.Series([14.5,10.9,10.3,18.5,9.3])
};

zeal=pan.DataFrame(res)
print(zeal)
print(zeal.shape)
new=zeal.T
print(new.shape)
print(zeal.axes[1])
print(zeal.ndim)
print(zeal.values)
print(zeal.head(3))