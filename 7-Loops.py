## Loops
# Loops are used to repeat a block of code multiple times. There are two types of loops in Python: while loops and for loops. We'll look at for loops first.

# To force stop a loop, press Ctrl + C

## For loops

# A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other range. This first loop will print numbers 1 through 100 as it iterates through the range.

# for i in range(1, 101):
#   print(i)
# 
# for letter in ("hello"):
#   print(letter)


## While loops
# A while loop is used to iterate over a block of code as long as the condition is true. This loop will keep printing the number 1 until the condition is false.

# while True:
#   print(1)

# x = 0
# while x <= 10:
#   print(x) 
#   x += 1 # This is the same as x = x + 1

  
# Fibonacci Sequence
# The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding numbers. The first two numbers in the sequence are 0 and 1, and each subsequent number is the sum of the two.

# import time
# 
# a,b = 0,1# These variables are the first two numbers in the sequence. They are assigned simultaniously.
# 
# while True:
#     print(a)
#     a,b = b,a+b# Again, we are assigning these variables in parallel.
#     time.sleep(.25)# This will make the program wait for .25 seconds before printing the next number in the sequence.