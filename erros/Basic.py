# swap two data
data1=input("Tell us data one: ")
data2=input("Tell us data two:" )

try:
    data1 *= data2
    data2 = data1 / data2
    data1 /= data2
except TypeError as tp:
    print(tp)
    data1=int(data1)
    data2=int(data2)
    data1 += data2
    data2 = data1 - data2
    data1 -= data2
finally:
    print("Swap done")

print(data1,data2)
