## Functions
# import random

# Functions are a way to reuse and organize code. Let's say 
# we have some code and we want to use it multiple times. 
# In this instance, we have to run the script multiple times 
# if we want to play the game multiple times.

# guess = int(input("Guess a number between 1 and 10: "))
# computerNumber = random.randint(1, 10)
# 
# if guess == computerNumber:
#     print("You guessed the number!")
# else:
#     print("Nope, the number was " + str(computerNumber))
# 
# Let's fix that.

# def guess_number():
#     guess = int(input("Guess a number between 1 and 10: "))
#     computerNumber = random.randint(1, 10)

#     if guess == computerNumber:
#         print("You guessed the number!")
#         if input("Would you like to play again? y/n: "):
#             guess_number()
#     elif input("Nope, the number was " + str(computerNumber) + ". Do you want to try again? ") == "y":
#         guess_number()

# guess_number()

# One thing about functions is that they can take in parameters. These are handy if you want to pass in some data to the function from outside the function.

# def add_numbers(a, b):
#     sum = a + b
#     print('Sum: ', sum)

# add_numbers(2 + 243, 3 + 4)