dict = {"name": "jayanth", "age": 21}

# Accessing the values of a dictionary
print(dict["name"])

# Adding a new key-value pair to a dictionary
dict["gender"] = "male"

# Updating the value of a key in a dictionary
dict["age"] = 22


# Deleting a key-value pair from a dictionary
popped = dict.pop("name")
popitem = dict.popitem() # removes the last key-value pair
print(dict)

for key in dict:
    print(key, dict[key])

value = "jayanth" in dict.values()
print(value)
print(dict.values())

print(dict.get("names"))


