# demonstration of LIST
prop=['Meguraj',5.6,72,'M']
# adding new element in end of the list
prop.append('Application Developer')
print(len(prop))
print(prop)
# adding new element by position
prop.insert(4,13.7)
print(prop)
# replace the data in respective position
prop[5]='Senior Programmer'
print(prop)

monthly=[7000,12000,6000,5000,3000]
print(max(monthly))
print(sum(monthly))
monthly.remove(6000)
print(monthly)
print(monthly.pop())
print(monthly.pop(1))
print(monthly)
monthly.append(8900)
monthly.append(7000)
monthly.append(7999)
print(monthly)
print(monthly.count(7000))
print(monthly.index(5000))