## Opening files for reading
# There are a couple ways to open a file for reading.

# The first way is to use the open() function.
# The open() function takes two arguments:
# The first argument is the name of the file to open.
# The second argument is the mode in which the file should be opened. In this example, we are opening the file for reading, so we use the 'r' mode.
# openGroceriesFile = open("groceries", "r")

# All we've done is open the file. We haven't read anything from it yet. To do that, we need to use the read() method.
# The read() method returns the contents of the file as a string.
# readGroceriesText = openGroceriesFile.read()

# Next, in this particular case, it would be helpful to break this string up into a list.
# We can do that by using the split() method.
# groceryList = readGroceriesText.split()

# print(groceryList)

# After doing what we need to, we can close the file. 

# openGroceriesFile.close()

# Another way we could open a file is to use the with statement. 
# The with statement is a way to open a file and automatically close it when we're done with it.
# It is generally a good idea to use the with statement when working with files because it ensures that the file is closed even if an exception occurs
# The with statement sort of works like an if statement.
# We are using "a+" to open the file for appending and reading.
# This is because we want to add to the file, not overwrite it.
# If you want more information on the modes you can open a file in, you can look here: https://www.w3schools.com/python/python_file
# with open("groceries", "a+") as openGroceryList1:
#   openGroceryList1.seek(0) # This is to move the cursor to the beginning of the file, because append mode automatically puts it at the end of the file.
#   groceryList1 = openGroceryList1.read().split()
#   print(groceryList1)
#   if "Milk" not in groceryList1:
#     openGroceryList1.write("\nMilk")

# We can also use the with statement to open a file for writing.
# When writing with the "w" mode, the file will be overwritten if it already exists.
# with open("fandoms", "w") as openFandoms:
#   openFandoms.write("Lord of the Rings\nChronicles of Narnia\nHarry Potter")