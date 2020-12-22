'''
Groupby:
filter
aggregate>> numpy
'''

import pandas as pan
import numpy as num

stats={
    "Company":['Cognizant','Wipro','Infoview','MindTree','Accenture','Wipro','TCS','Infoview','MindTree'],
    "Year":[2012,2012,2020,2019,2006,2002,2018,2016,2012],
    "Count":[56,12,89,120,67,10,6,32,19],
    "Day":[3,2,4,8,1,4,2,1,2]
}

frame=pan.DataFrame(stats)
print(frame)

'''for x,y in frame.groupby('Year'):
    print(x)
    print(y)'''

'''for x,y in frame.groupby(['Count','Day']):
    print(x)
    print(y)'''

'''for x in frame.groupby('Company')['Year']:
    print(x)'''

'''print(frame.groupby('Year').agg(num.sum))
print(frame.groupby('Day').agg(num.max))'''

print(frame.groupby('Company').filter(lambda x:len(x)>=2))