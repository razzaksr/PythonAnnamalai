# Dictionary

stu={'annamalai':'python','meguraj':11000,7000:'Core Python',8000:'java',7000:'JavaEE'}
print(stu)

# adding new object
stu[18000]='Spring'
print(stu)

# replace
stu['annamalai']='Django'
print(stu)

# remove
print(stu.pop('annamalai'))
print(stu.popitem())

# read
print(stu.keys())
print(stu.values())
print(stu.items())

# listing
for x,y in stu.items():
    print(x,y)

for x in stu.keys():print(x)