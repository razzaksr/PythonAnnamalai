# load, save, loadtxt,savetxt

import numpy as num

#data=input("Enter plain text: ")
data=num.arange(11,27).reshape(4,4)
'''check=num.save("basicnio",data)
print("File has saved")

print("Actual content in file: \n",num.load("basicnio.npy"))'''
num.savetxt("Maximizing",data)
print("File has saved")
print("Actual data in normal file: \n",num.loadtxt("Maximizing"))