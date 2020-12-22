# Merging/ Joins

import pandas as pan

stats1={
    "Company":['Accenture','Wipro','TCS','Infoview','MindTree'],
    "Year":[2006,2002,2018,2016,2012],
    "Count":[67,10,6,32,19],
    "Day":[1,4,2,1,2]
}
frame1=pan.DataFrame(stats1)
stats2={
    "Company":['Cognizant','Wipro','Infoview','MindTree'],
    "Year":[2012,2012,2020,2019],
    "Count":[56,12,89,120],
    "Day":[3,2,4,8]
}
frame2=pan.DataFrame(stats2)
print(frame1)
print(frame2)

print(pan.merge(frame1,frame2,on='Company'))
#print(pan.merge(frame1,frame2,on=['Day','Year']))

#print(pan.merge(frame1,frame2,on='Company',how='left'))
#print(pan.merge(frame1,frame2,on='Company',how='right'))
#print(pan.merge(frame1,frame2,on='Company',how='outer'))
