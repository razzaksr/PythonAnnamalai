# Sorting: sort_index(row,column), sort_values(column,kind)

import pandas as pan
import numpy as num
from matplotlib.axes._base import _axis_method_wrapper

frame=pan.DataFrame(num.random.randn(5,3),columns=["team3","team1","team2"],index=["IRCTC","PassportSeva","TNePass","Flipkart","GPay"])
print(frame)

inWise=frame.sort_index()
#print(inWise)

clWise=frame.sort_index(axis=1)
#print(clWise)

valWise=frame.sort_values(by='team1',ascending=False)
#print(valWise)

valsWise=frame.sort_values(by='team3',ascending=False)
print(valsWise)