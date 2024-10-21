## Classes
# Classes are like a blueprint for constructing objects. Objects
# are everywhere in python. Objects can have variables called attributes
# and functions called methods. 

# This is a basic class with some attributes. 

# class Person:
#     age = 24
#     name = "John Doe"
#     location = "Toronto, Ontario"

# the variable person becomes an object. We can print out the attributes 
# as we need them. We can also redefine attributes as well. 

# person = Person()
# print(person.age)
# print(person.name)
# print(person.location)

# person.name = "Jackson Pollock"
# print(person.name)

###########################################################################

# Let's look at another example. Let's say we're making
# a game and we have a Character class that we can use
# as a template. In this case, we have a special
# function or method that gets run whenever we reference 
# the class.  

# When using a method inside a class, you need to declare
# the variables as self.variable. Also, when python creates
# the object, it passes it as the first argument, which is why 
# self is the first argument in the __init__ method. Any other
# arguments can be placed after that.

# You'll notice these attributes are set to whatever the arguments
# are in the __init__ method

# class Character:
#     def __init__(self, h, d, s):
#         self.health = h
#         self.damage = d
#         self.speed = s

# warrior = Character(100, 50, 10)
# ninja = Character(80, 40, 40)

# This is printing an "f-string." This is another way of formatting
# text. With f-strings, you can put expressions directly in the 
# string. This is the same as printing "Warrior Speed: " + warrior.speed

# print(f"Warrior Speed: {warrior.speed}")
# print(f"Ninja Damage: {ninja.damage}")

#######################################################################

# Here's another example

# class Salesperson:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     sales = 0

#     def makeSale(self, saleValue):
#         self.sales += saleValue

#     def salesReport(self):
#         print(f"My total in sales is ${self.sales}!")

# john = Salesperson("John", "Doe")
# john.makeSale(600)
# john.salesReport()