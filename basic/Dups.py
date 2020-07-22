hey = [12, 45, 90, 12, 34, 45]
temp = []

# finding dup and adding to temp list
for say in range(len(hey)):
    for kay in range(say + 1, len(hey)):
        if hey[say] == hey[kay]:
            temp.append(hey[say])

# perform xor between temp list elements
xor = temp[0]
for xen in range(1, len(temp)):
    xor ^= xen

# removing all duplicates until 0 count found
for h in temp:
    while hey.count(h) != 0:
        hey.remove(h)

# append xor result in actual list
hey.append(xor)
# verifying the actual list as expected
print(hey)

'''num=int(input("Tell us number to check: "))
for say in range(len(hey)):
    for kay in range(say+1,len(hey)):
        if hey[say]==hey[kay]:
            if hey[say]%num==0:
                print(hey[say],"okay")
            else:print(hey[say],"failed")'''
