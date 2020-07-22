'''
     1
    246
   89101112
'''
num=1;limit=1
fix=int(input("Tell us bound:  "))
for row in range(1,fix+1):
    for space in range(fix-1,row-1,-1):print(" ",end="")
    for data in range(1,limit+1):
        print(num, end="")
        if row%2==0:num+=2
        else:num+=1
    limit+=2;print()

