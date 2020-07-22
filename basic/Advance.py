'''
filling fibo
        0
      1 1
   2  3 5
8 13 21 34


num1,num2=0,1
sum=num1+num2
limit=int(input("Enter limit: "))
print(num1)
print(num2)
for hai in range(limit-2):
    sum = num1 + num2
    num1=num2;num2=sum;
    print(sum)
'''
# pattern with fibonacci
'''
              0
            1 1
         2  3 5
     8  13  21 34
  55 89 144 233 377
'''
num1,num2=0,1
limit=int(input("Tell us limit: "))
for row in range(limit,0,-1):
    for col in range(1,limit+1):
        if col>=row:
            if row==limit: print(num1,end=" ")
            elif row==limit-1 and col==limit-1:print(num2,end=" ")
            else:
                sum = num1 + num2
                num1 = num2;
                num2 = sum;
                print(sum,end=" ")
            #print("#",end="")
        else:print(end=" ")
    print()