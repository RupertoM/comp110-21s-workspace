"""The very first and most special self created project in my programming career."""

__author__ = "730408061"

from random import randint

player = ""
points = 0

def main() -> None:
    """The entrypoint for user interaction with the program."""
    global points
    points = 0
    greet()
    games()

def greet() -> None:
    """The greeting function that will ask the user for an input."""

    global player

    player = input("Welcome to the COMP 110 programming game. What is your name? - ")

def games() -> None:
    """The function that will allow the user to choose an adventure path. (Continously looped with 3 options.)"""

    option = int(input(f"You now have {points} point(s). \nPlease select one of the following using the integer provided before each option. \n1- Dice rolling game.\U0001F3B2 \n2- Color guessing game.\U0001F3A8 \n3- Coinflip game.\U0001F4B8 \n4- End gaming experience.\U00002705 \nAnswer: "))

    if option == 1:
        dice()
    
    if option == 2:
        colorguess()
    
    if option == 3:
        coinflip()
    
    if option == 4:
        print(f"Thank you so much for playing! You earned {points} point(s)!! Congratulations, have a great day {player}!")

def dice() -> None:
    """The function for the dice rolling game option."""

    dice_roll = randint(1,6)

    ready = input("Welcome to the dice rolling game. If you guess correctly on your first try you will win 10 points. If you guess correctly within the first 3 tries you will gain 5 points. If you fail to guess correctly within 3 tries you will not gain any points. Want to play? Y/N: ")

    if ready == "Y":
        dice_count = 1

        while int(input("Pick a number 1-6. If you guessed incorrectly try again. ")) != dice_roll:
            dice_count += 1

        if dice_count == 1:
            global points
            points += 10
            games()

        if dice_count <= 3:
            points += 5
            games()

        if dice_count > 3:
           games()

    else:
        games()

def colorguess() -> None:
    """The function for the number guessing game option."""

    offset = randint(0,3)
    color_list = ["Black", "Red", "Tarheel Blue", "White"]
    color = color_list[offset]
    ready = input("Welcome to the color guessing game. If you guess correctly on your first try you will win 10 points. If you guess correctly within the first 2 tries you will gain 5 points. If you fail to guess correctly within 2 tries you will not gain any points. Want to play? Y/N: ")

    if ready == "Y":
        color_count = 1
        while input("Pick a color: Tarheel Blue, White, Red, or Black. If you guessed incorrectly try again. ") != color:
            color_count += 1

        if color_count == 1:
            global points
            points += 10
            games()

        if color_count == 2:
            points += 5
            games()

        if color_count > 2:
            games() 


    else:
        games() 

def coinflip() -> None:
    """The function for coin flip game option."""

    ready = input("Welcome to the coin flipping game. For every time you correctly guess the coin flip you will earn 1 point. Want to play? Y/N: ")

    if ready == "Y":
        
        heads_or_tails = ["Heads", "Tails"]

        while (input("Pick Heads or Tails: ")) == heads_or_tails[randint(0,1)]:
            global points
            points += 1
        
        games()

    else:
        games()


if __name__ == "__main__":
  main()