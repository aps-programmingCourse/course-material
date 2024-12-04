import random

def rockPaperScissors(user_score, computer_score):

    user_input = input("Type 'rock', 'paper', or 'scissors' to play or 'close' to close: ").lower()
    possible_moves = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_moves)

    if user_input == computer_choice:
        print("Draw!\nYou chose " + user_input + " and the computer chose " + computer_choice)
        playAgain(user_score, computer_score)
    elif ((user_input == "rock" and computer_choice == "scissors") or 
        (user_input == "paper" and computer_choice == "rock") or
        (user_input == "scissors" and computer_choice == "paper")):
        print("You win!\nYou chose " + user_input + " and the computer chose " + computer_choice)
        user_score += 1
        playAgain(user_score, computer_score)
    elif ((user_input == "rock" and computer_choice == "paper") or
        (user_input == "paper" and computer_choice == "scissors") or
        (user_input == "scissors" and computer_choice == "rock")):
        print("You lose!\nYou chose " + user_input + " and the computer chose " + computer_choice)
        computer_score += 1
        playAgain(user_score, computer_score)
    elif user_input == "close":
        quit()
    else:
        print("Please type either 'rock', 'paper', or 'scissors' to play or 'close' to close: ")

def playAgain(user_score, computer_score):

    print("User: " + str(user_score) + "     Computer: " + str(computer_score))
    if input("Do you want to play again? y or n? ") == "y":
        print()
        rockPaperScissors(user_score, computer_score)

rockPaperScissors(0,0)