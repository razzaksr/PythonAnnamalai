# manually forward to the except: raise
check = [2.1, 4.3, 8.8, 9, 2.1, 0, 7.9]
try:
    one = int(input("Tell the index one: "))
    two = int(input("Tell the index two: "))
    if check[two] == 0:
        raise IndexError
    print(check[one] / check[two])
except ZeroDivisionError as zero:
    print(zero)
    two = int(input("Tell the index two: "))
    print(check[one] / check[two])
except IndexError as ind:
    print("Occured Index error")
