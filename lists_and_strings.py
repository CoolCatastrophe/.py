import copy
birthday = (input("What is your birthday? "))
print(birthday.split("/"))

fruits= ["apple", "banana",["gauva","pear" ], "cherry", "kiwi", "mango"]
# print(" ".join(fruits))

new_fruits = fruits.copy()
new_new_fruits = copy.deepcopy(fruits)
print(id(fruits))
print(id(new_fruits))
print((new_new_fruits))