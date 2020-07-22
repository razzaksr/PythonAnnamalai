'''
functions with parameter and return type
parameter without return
no parameter with return
no parameter without return
'''

#list
# index always starts with 0,1,2,3,......
balance=[200000,19000,3400,10999]

def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money, "debited")
        return balance[pos]
    else:print("Can't debit")

hai=debit(10000,3)
print(hai)

def simple(single=0):
    return single*single

def demo():
    exp=int(input("Tell us experience: "))
    skill=input("Tell us skill: ")
    if exp>=4 and exp<6 and skill == 'python' or skill=='java':
         return "Promoted as Team Lead"
    elif exp>=6 and exp<10 and skill == 'agile' or skill == 'devops':
        return "Promoted as Project Manager"
    return "Be as associate"

yet=simple(12)
print(yet)

desig=demo()
print(desig)