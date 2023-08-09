print("*" * 35)
print("\tWelcome to The Game!")
print("*" * 35)
player_1 = input("Enter the name of player 1: ")
player_2 = input("Enter the name of player 2: ")
i = 13
current_player = player_1
while True:
    print("|" * i)
    print(f"There are {i} toothpicks left")
    if i >= 1:
        choice = int(input(f"How many do you take, {current_player}: "))
        while choice != 1 and choice!=2 and choice!=3:
            choice = int(input("You can only chose between 1,2,3!\nPlease try again: "))
        i -= choice
        print(f"There are {i} toothpicks left")
        if i <= 0:
            print(f"{current_player.upper()} WINS!!")
            break
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
print("*" * 25)
print("\tGAME OVER!")
print("*" * 25)
