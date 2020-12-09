# statisticks over series and frame:  covariance, percent_change, correlation, rank, min, max

import pandas as pan

line=pan.Series([5.6,1.2,9.1,8.9,4.5])
dots=pan.Series([8.9,2.1,9.1,4.5,4.5])

print(line)

print(line.pct_change())

print(line.cov(dots))

frame=pan.DataFrame({"Dell":pan.Series([32800,43900,31080]),
                     "Acer":pan.Series([21490,18900,39800]),
                     "Sony":pan.Series([98700,62900,65400]),
                     "HP":pan.Series([47800,78900,31900])})
'''print(frame)
print(frame.cov())
print(frame['Dell'].cov(frame['Sony']))
print(sum(frame['Dell']))
print(sum(frame['Sony']))'''

print(line,dots)
print(line.corr(dots))
print(frame)
print(frame.rank())

print("In Series Based")
print("max:",line.max(),"min",line.min())
print("max:",dots.max(),"min",dots.min())