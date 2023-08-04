# Rock Paper Scissors Game
import random
from asci_art import rock, paper, scissors

choice = ["rock", "paper", "scissors"]


print("What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors")
user_choice = int(input())
computer_choice = random.randint(0, 2)
game_result = ""
user_asci = ""
computer_asci = ""


if user_choice == 0:
    user_asci = rock
    if computer_choice == 0:
        computer_asci = rock
        game_result = "draw"
    elif computer_choice == 1:
        computer_asci = paper
        game_result = "lose"
    elif computer_choice == 2:
        computer_asci = scissors
        game_result = "win"
elif user_choice == 1:
    user_asci = paper
    if computer_choice == 0:
        computer_asci = rock
        game_result = "win"
    elif computer_choice == 1:
        computer_asci = paper
        game_result = "draw"
    elif computer_choice == 2:
        computer_asci = scissors
        game_result = "lose"
elif user_choice == 2:
    user_asci = scissors
    if computer_choice == 0:
        computer_asci = rock
        game_result = "lose"
    elif computer_choice == 1:
        computer_asci = paper
        game_result = "win"
    elif computer_choice == 2:
        computer_asci = scissors
        game_result = "draw"

x = choice[computer_choice]
print("Computer chose : " + computer_asci)
y = choice[user_choice]
print("You chose : " + user_asci)
print(f"Result is:  you {game_result}")
