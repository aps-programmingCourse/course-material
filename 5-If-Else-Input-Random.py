# import random

## If/Else Statements, Boolean Operators and Indentation
# Python uses indentation to determine a block of code. 
# If you don't indent, Python will give you an error.

# When you want to check if something is true, you use
# an if statement. Else is used if you want to do an 
# action if the if statement isn't true. Elif is the
# same thing as else if. 

# x = 10

# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")

# drinks = ["Coffee", "Tea", "Water", "Juice", "Soda"]
# if "coffee" in drinks:
#     print("Yay!")
# else:
#     print("How sad")

## Getting User Input
# To get the input of user, we use the input function 
# built into Python. Let's take the example of the last
# if statement we created. Let's say we want to ask them 
# what their favorite drink was and compare it to our list. 

# favDrink = input("What's your favorite drink? ")

# if favDrink in drinks:
#     print("Yay!")
# else:
#     print("How sad")

## Random Library
# Python has a built-in library called random that can 
# be used to make random numbers
# print(random.randrange(1, 10))

# food = ["pizza", "burger", "fries", "salad", "sushi"]
# print(random.choice(food))