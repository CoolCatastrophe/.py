def is_even(n):
    return (abs(n)%2==0)

print(is_even(2))
print(is_even(0))

print(is_even(1))
print(is_even(-1))


def slugify(string):
    return string.lower().strip().replace(" ", "-")

print(slugify("    hello world    "))

count=0
def vowels(s="   hello world   "):
    global count
    for i in s:
        if(i in "aeiouAEIOU"):
           count+=1
    return count
print(vowels("hello world"))