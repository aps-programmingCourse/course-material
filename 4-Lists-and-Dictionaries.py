## Lists

# drinks = ["Coffee", "Tea", "Milk", "Orange Juice"]
# 
# print(drinks)
# print(drinks[0] + " is the king of all drinks")
# print(len(drinks))
# 
# # Lists are mutable, so you can change them after you've declared them.
# drinks.append(input("What is your favorite drink? "))
# print(drinks)

# You can get the sum of all the numbers in a list.
# listOfNumbers= [1,2,3,4,5.5]
# print(sum(listOfNumbers))
# 
# # You can also add lists together
# 
# listOfNumbers2= [6,7,8,9,10]
# 
# newListOfNumbers = listOfNumbers + listOfNumbers2
# 
# print(newListOfNumbers)
# print(listOfNumbers[3])

## Tuples
# Tuples are very similar to lists, but they are immutable,
# so you can't change them after they're made.

myTuple = ("Spiderman", 18, "Spidey Sense")
anotherTuple = "Iron Man", 39, "Iron Man Suit"

# Notice that the first example uses parentheses and the
# second one doesn't, but they're both considered tuples.

# Tuples are faster to calculate than lists, so might be
# a better choice in some scenarios.

## Dictionaries
# Dictionaries contain data that is stored in key-value pairs.

# bills = {"Rent": 1000, "Electricity": 100, "Water": 50, "Internet": 100}
# 
# print(bills)
# print(bills["Rent"])
# 
# # You can add new key-value pairs to a dictionary by using the following syntax:
# bills["Phone"] = 100
# 
# print(bills)