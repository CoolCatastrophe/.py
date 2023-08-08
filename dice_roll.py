from random import randint

dices=int(input("Enter the number of dice you want to roll (1 to 10): "))
sides=int(input("Enter the number of sides on the dice:(1 to n) "))
choice = '';

while choice != 'q':
    result="|"
    if(dices<=10):
        for i in range(dices):
            r = randint(1,sides)
            result+=f"{r}|"
        print(result)
        choice=input("Press enter to continue or 'q' to quit: ")
    else:
        print("The entered number of dices is greater than 10")
        break    