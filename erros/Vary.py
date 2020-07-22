# multiple at one
from array import *
simple=array('i',[12,90,34,78,11])
maps={'Sobin':10,'Aasai':7,'Sridhar':15,'Razak':8,'Titus':11}

try:
    point = input("Tell us name to update: ")
    print(maps[point])
    pos = int(input("Tell us index in array from where copying the data: "))
    maps[point] = simple[pos]
except KeyError as key:
    print(key)
    try:
        point = input("Tell us name to update: ")
        print(maps[point])
        pos = int(input("Tell us index in array from where copying the data: "))
        maps[point] = simple[pos]
    except IndexError as ind:
        try:
            print(ind, "index should be within ", len(simple))
            pos = int(input("Tell us index in array from where copying the data: "))
            maps[point] = simple[pos]
        except Exception as e:print(e)
finally:print("Updation done")

print(maps)

