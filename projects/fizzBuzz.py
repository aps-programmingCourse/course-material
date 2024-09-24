## FizzBuzz

# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz" instead of the number and for the multiples of five print “Buzz". For numbers which are multiples of both three and five print “FizzBuzz".

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

## Another solution
# https://aghilissen.medium.com/fizz-buzz-fizzbuzz-715e1f5bda60
# fizzbuzz = {"Fizz": 3, "Buzz": 5, "Whiz": 7, "Bang": 11}
#
# for i in range(1, 101):
#   output = ""
#   for key, value in fizzbuzz.items():
#     if i % value == 0:
#       output += key
#   print(output or i) # The print statement will ensure only a non-empty object will be printed:
