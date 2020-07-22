# deleting items from dict based on given range
drives={1000:['sony','hp'],500:['transcend','sandisk'],2000:['Hp','toshiba','iBall'],
        700:'Sony',2100:['Hp','micromax']}

start=int(input("Starting range: "))
end=int(input("Maximum range: "))
temp=[]

for key,val in drives.items():
    print(key,val)
    if start<=key<=end:temp.append(key)

for key in temp:
    del drives[key]

print("After poped items from given range",start,"and",end)
print(drives)