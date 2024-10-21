### String Manipulation ###

## Input
# color = input("What is your favorite color? ")
# print(color)
# print("Really? " + color.capitalize() + " is my favorite color too!")#

## Line Breaks
# print("Hello World")
# print("Hello World")
# print("Hello World\nHow are you today?")

## Length of a String
sayHi = "Hello World"
# len(sayHi)
# print(len(sayHi))

## Strings as Lists

# sayHi[0]

# print(sayHi[0])

# print(sayHi[-1])

# print(sayHi[0:5])
# When printing a range, the last number is not included, 
# so you'll need to add 1 to the end of the range.
# In cases where you are starting from the beginning of 
# the string, you can leave the first number blank.
# print(sayHi[:5])
# print(sayHi[6:])
# print(sayHi[-5:])

## Finding a String
# print(sayHi.find("World"))
# firstO = sayHi.find("o")
# print(sayHi.find("o", firstO + 1))

## Replacing a String
# print(sayHi.replace("World", "Universe"))
# Strings are immutable, so you can't change the 
# original string. You can only create a new string 
# with parts of an existing string. 

## Split Strings
# print(sayHi.split(" "))