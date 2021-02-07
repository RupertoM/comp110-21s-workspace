"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730408061"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

random_number = randint(0,100)

print("Your fortune cookie says...")

if random_number <= 50:
    if random_number <= 25:
        print("You will be joyful and successful.")

    else:
        print("Your life will be prosperous and full of love.")

else:
    if random_number <= 75:
        print("You will find fulfillment in the small things in life.")

    else:
        print("You will have the most amazing life in the universe!")

print("Now, go spread positive vibes!")
    
