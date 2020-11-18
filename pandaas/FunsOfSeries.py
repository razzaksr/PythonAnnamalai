# size, empty, values, head, tail, ndim, axes

import numpy as num
import pandas as pan

line=pan.Series()
print(line.empty)
line=pan.Series(num.random.randn(5))
print(line.empty)
print(line)
print(line.ndim)
print(line.values)
print(line.axes)
print(line.head(2))
print(line.tail(2))