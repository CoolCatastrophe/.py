def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)


print(average(10, 1, 2, 3))
num = [10, 1, 2, 3]
print(average(*num))


def fun(arg1, *args):
    print(arg1)
    print(args)


fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def silly(arg1, *args, arg2):
    print(arg1)
    for arg in args:
        print(arg)
    print(arg2)


silly("hello", 1, 2, 3, arg2="goodbye")


def count_stuff(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


count_stuff(apples=3, bananas=4, oranges=1)
