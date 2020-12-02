# Slice and Selection:iloc,loc,ix

import pandas as pan
import numpy as num

'''frame=pan.DataFrame({"Dell":pan.Series([32800,43900,31080],index=["Middle","High","Low"]),
                     "Acer":pan.Series([21490,39800,18900],index=["Middle","High","Low"]),
                     "Sony":pan.Series([65400,98700,62900],index=["Middle","High","Low"]),
                     "HP":pan.Series([47800,78900,31900],index=["Middle","High","Low"])})
#print(frame)

print(frame.loc[:])

print(frame.loc[:,'Sony'])
#print(frame['Sony'])
print(frame.loc[:,['Dell','HP']])
print(frame.loc['High'])
print(frame.loc['High',['HP','Acer']])
print(frame.loc[['Middle','Low']])
print(frame.loc[['Middle','Low'],['Acer','Sony']])
print(frame.loc['Low']<25000)'''

'''tmp={"0":pan.Series([5.6,1.2,9.1,8.9,4.5]),
     "1":pan.Series([8.9,2.1,4.5,2.1,9.1]),
     "2":pan.Series([8.9,2.1,9.1,4.5,4.5])}

frame=pan.DataFrame(tmp)
print(frame)

print(frame.iloc[0])
print(frame.iloc[0:2])
print(frame.iloc[:,0])
print(frame.iloc[[0,4,2]])
print(frame.iloc[[0,4,2],[0,2]])'''

frame=pan.DataFrame(num.random.randn(5,3),columns=["team1","team2","team3"])
print(frame)