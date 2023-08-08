from random import randint
count=0
num = 1
while num > 0:
    num = randint(1, 6)
    if num == 6:
        roll = randint(1, 6)
        if roll == 6:
                print(f"You rolled a 6 and a 6 with {count} moves")
                num=-1
        else:
            count+=1
            print("You rolled a 6 and a", roll)