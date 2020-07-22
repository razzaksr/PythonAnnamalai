# Tuple:()
check=(12,'Annamalai',8000,2.4)
#check[0]=40

#listing all elements
print(check)
print(check[2])
#del check[0]
print(check.count(2.4))
print(check.index('Annamalai'))

ran=(34000,67000,1900,3400,6000)
print('Using in range')
for x in range(0,len(ran)):
    print(ran[x])
print('Using in')
for x in ran:
    print(x)
