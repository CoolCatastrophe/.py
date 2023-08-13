def contains_pickle(*args):
    return "pickle" in args


print(contains_pickle("red", "pickle"))
print(contains_pickle("red", "pick"))


def count_fails(*args):
    count = 0
    for arg in args:
        if arg <= 50:
            count += 1
    return count


print(count_fails(99, 480, 79, 369))


def get_top_students(**kwargs):
    top_list = []
    for student, score in kwargs.items():
        if score >= 90:
            top_list.append(student)
    return top_list


print(get_top_students())
