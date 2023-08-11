list1 = [1, 2, 3, 4, 5]
list2 = list1

print(id(list1))
print(id(list2))

list2.append(6)

print(id(list1))
print(id(list2))

print(list1)

list3 = list1.copy()

print(id(list1))
print(id(list3))

list3.append(7)

print((list1))

print(list1 == list2)
print(list1 is list2)

print(list1 == list3)
print(list1 is list3) 
