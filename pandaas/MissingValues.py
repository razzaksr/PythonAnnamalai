# Missing values: na: find, fill, pad,backfill, replace

import numpy as num
import pandas as pan

frame=pan.DataFrame(num.random.randn(5,3),columns=["team3","team1","team2"],index=["IRCTC","PassportSeva","TNePass","Flipkart","GPay"])
print(frame)

frame=frame.reindex(['IRCTC','ELECTROL','PassportSeva','TNePass','TNPWD','Flipkart','GPay','PhonePe'])
print(frame)

print(frame.isnull())
print(frame.notnull())

frame=frame.fillna(2.3)
print(frame)

'''frame=frame.pad()
print(frame)'''

'''frame=frame.backfill()
print(frame)'''

tmp={"team1":pan.Series([5.6,1.2,9.1,8.9,4.5]),
     "team2":pan.Series([8.9,2.1,4.5,2.1,9.1]),
     "team3":pan.Series([8.9,2.1,9.1,4.5,4.5])}

frame=pan.DataFrame(tmp)

print(frame)

print(frame.replace({2.1:8,4.5:9.6}))

print(frame.sum())


