class Person:
    age = 24
    name = "John Doe"
    location = "Toronto, Ontario"

john = Person()
print(john.age)
print(john.name)
print(john.location)

####################################################

# class Salesperson:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     sales = 0

#     def makeSale(self, saleValue):
#         self.sales += saleValue

#     def salesReport(self):
#         print(f"My total in sales is ${self.sales}!")

# salesperson1 = Salesperson("Nick", "McCullum")
# salesperson1.makeSale(600)
# salesperson1.salesReport()

#####################################################

# class Character:
#     def __init__(self, health, damage, speed):
#         self.health = health
#         self.damage = damage
#         self.speed = speed

# warrior = Character(100, 50, 10)
# ninja = Character(80, 40, 40)

# print(f"Warrior Speed: {warrior.speed}")