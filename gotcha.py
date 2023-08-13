def add_twice(val , list=None):
    if list is None:
        list = []
    list.append(val)
    list.append(val)
    return list
print(add_twice(5))
