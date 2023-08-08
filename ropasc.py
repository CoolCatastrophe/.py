from random import randint

rock = """
    _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
      _______
----'    ____)____
            ______)
          __________)
         ______)
---.__________)
"""


print("Welcome to Rock, Paper, Scissors")
print("What do you choose(Enter choice number)?")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

choice = int(input("Enter your choice: "))
print("Your move:")
if choice == 1:
    move="rock"
    print(rock)
elif choice == 2:
    move="paper"
    print(paper)
else:
    move="scissors"
    print(scissors)

print("Computer move:")
num = randint(1,3)
if num == 1:
    RPS="rock"
    print(rock)
elif num == 2:
    RPS="paper"
    print(paper)
elif num==3:
    RPS="scissors"
    print(scissors)
print("\n")
if move == RPS:
    print("Its a draw🫰")
elif choice == 1 and RPS == "paper":
    print("You lose🙂")
elif choice == 1 and RPS == "scissors":
    print("You win🎉")
elif choice == 2 and RPS == "rock":
    print("You win🎉")
elif choice == 2 and RPS == "scissors":
    print("You lose🙂")
elif choice == 3 and RPS == "rock":
    print("You lose🙂")
elif choice == 3 and RPS == "paper":
    print("You win🎉")
else:
    print("Invalid choice!!") 