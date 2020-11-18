# Panel: 3D: axis=0: items, major, minor: Pan(el) Da(ta)

import pandas as pan
import numpy as num

some=num.random.rand(4,3,2)
p=pan.Panel(some)
print(p)