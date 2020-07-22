# Recursive function: function calling itself
# usage: quit like a loop
def nums(start=1):
    if start > 10:
        return
    else:
        print("Hai")
        start += 1
        nums(start)  # recursive
nums()
def factorial(num=0, res=1):
    if num == 0:
        print(res);return
    else:
        res *= num
        num -= 1
        factorial(num,res)
factorial(5)
