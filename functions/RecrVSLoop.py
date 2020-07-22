# time complexity:
#index 0
mobPrice=[9700,15600,89000,2000,45000,15000,60000]
# Iteration through recursive
def iterate(index=0):
    if index==len(mobPrice):return
    else:
        print(mobPrice[index])
        index+=1
        iterate(index)
iterate()
# Iteration through loop
for temp in range(2,len(mobPrice)-1):
    print(mobPrice[temp])
