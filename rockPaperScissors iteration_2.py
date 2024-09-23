import random

user_input = input("Type rock, paper, or scissors to play: ").lower()
possible_moves = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_moves)

if user_input == computer_choice:
    print("Draw!\nYou chose " + user_input + " and the computer chose " + computer_choice)
elif ((user_input == "rock" and computer_choice == "scissors") or 
    (user_input == "paper" and computer_choice == "rock") or
    (user_input == "scissors" and computer_choice == "paper")):
    print("You win!\nYou chose " + user_input + " and the computer chose " + computer_choice)
elif ((user_input == "rock" and computer_choice == "paper") or
    (user_input == "paper" and computer_choice == "scissors") or
    (user_input == "scissors" and computer_choice == "rock")):
    print("You lose!\nYou chose " + user_input + " and the computer chose " + computer_choice)