import numpy as num

from matplotlib import pyplot as pyp

'''base=num.arange(101,111)# 10 x>> rows
cable=base*2+5
pyp.title("Megu graph")
pyp.xlabel("Row")
pyp.ylabel("Column")
pyp.plot(base,cable)
pyp.show()'''



'''overs=num.arange(1,21)
runs=[10,0,1,4,17,12,20,10,3,5,3,6,7,10,5,2,1,9,12,0]
pyp.title("CSK Innings")
pyp.xlabel("Overs")
pyp.ylabel("Score taken")
pyp.plot(overs,runs,"or")
pyp.show()'''


'''wave=num.arange(0,3*num.pi,0.1)
depth=num.sin(wave)
pyp.title("Sign wave")
pyp.xlabel("Rows")
pyp.ylabel("Columns")
pyp.plot(wave,depth)
pyp.show()

wave=num.arange(0,3*num.pi,0.1)
depth=num.cos(wave)
pyp.title("Cos wave")
pyp.xlabel("Rows")
pyp.ylabel("Columns")
pyp.plot(wave,depth)
pyp.show()


wave=num.arange(0,3*num.pi,0.1)
depth=num.tan(wave)
pyp.title("Tan wave")
pyp.xlabel("Rows")
pyp.ylabel("Columns")
pyp.plot(wave,depth)
pyp.show()'''

'''wave=num.arange(0,3*num.pi,0.1)
depth=num.sin(wave)

# first half
pyp.subplot(2,1,1)
pyp.title("Sin wave")
pyp.plot(wave,depth)

# second half
pyp.subplot(2,1,2)
depth=num.tan(wave)
pyp.title("Tan wave")
pyp.plot(wave,depth)

pyp.show()'''

# election of US
trumpx=[1,3,5,7,9]
bidenx=[2,4,6,8,10]

trumpy=[10,50,30,10,100]
bideny=[60,100,20,100,10]
pyp.title("Us results")
pyp.xlabel("Candidates")
pyp.ylabel("Leading")
pyp.bar(trumpx,trumpy,color='r',align='center')
pyp.bar(bidenx,bideny,color='c',align='center')

pyp.show()

