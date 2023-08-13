try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

try:
    num = int(input("Enter a Number: "))
except ValueError as e:
    print("Fine I'll choose for you.. as you have entered", e)
    num = 8
except EOFError as e:
    print(e)
