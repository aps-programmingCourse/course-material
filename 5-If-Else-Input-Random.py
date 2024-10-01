# import random

## If/Else Statements and Indentation
# Python uses indentation to determine a block of code. 
# If you don't indent, Python will give you an error.

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

# if input("What's your favorite drink? ") in drinks:
#     print("Yay!")
# else:
#     print("How sad")

## Random Library
# Python has a built-in library called random that can 
# be used to make random numbers
# print(random.randrange(1, 10))

# food = ["pizza", "burger", "fries", "salad", "sushi"]
# print(random.choice(food))