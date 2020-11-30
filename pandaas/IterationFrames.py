# Iteration:

import pandas as pan
import numpy as num

tmp={"team1":pan.Series([5.6,1.2,9.1,8.9,4.5]),
     "team2":pan.Series([8.9,2.1,4.5,2.1,9.1]),
     "team3":pan.Series([8.9,2.1,9.1,4.5,4.5])}

frame=pan.DataFrame(tmp)
#print(frame)

#for x in frame:print(x)

# iterate by columns
for x,y in frame.iteritems():print(x,y)

# iterate by rows
#for x in frame.iterrows():print(x)

# iterate by tuple
for x in frame.itertuples():print(x)