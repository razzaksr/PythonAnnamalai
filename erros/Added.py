# value error
alpha=[12,9.7,3,4,"Razak",8.9,4.5]
try:
    hike = int(input("Tell us hike percent: "))
except ValueError as v:
    print(v)
    hike = int(input("Tell us hike percent in numeric: "))
for hai in range(len(alpha)):
    try:
        alpha[hai] += (alpha[hai] * hike) / 100
        print(alpha[hai])
    except TypeError as tp:
        print(tp)
        continue