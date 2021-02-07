"""An exercise in remainders and boolean logic."""

__author__ = "730408061"

# Begin your solution here...

number_string = input("Enter a number:")

number_integer = int(number_string)

if number_integer % 2 == 0 and number_integer % 7 == 0:
    print("TAR HEELS")

else:
    if number_integer % 2 == 0:
        print("TAR")
        
    if number_integer % 7 == 0:
        print("HEELS")

if number_integer % 2 != 0 and number_integer % 7 != 0:
    print("CAROLINA")