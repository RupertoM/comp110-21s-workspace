"""The very first and most special self created project in my programming career."""

__author__ = "730408061"

from random import randint

player: str
points: int 
DIE_EMOJI = "\U0001F3B2"
PAINT_EMOJI = "\U0001F3A8"
MONEY_EMOJI = "\U0001F4B8"
CHECKMARK_EMOJI = "\U00002705"


def main() -> None:
    """The entrypoint for user interaction with the program."""
    global points
    points = 0
    greet()
    games()


def greet() -> None:
    """The greeting function that will ask the user for an input."""
    print("Welcome to the COMP 110 programming game.")

    global player
    player = input("What is your name? - ")


def games() -> None:
    """The function that will allow the user to choose an adventure path. *Continously looped with 3 options."""
    global points
    option = int(input(f"""

You have {points} point(s).

Please select one of the following using the integer provided before each option.
1- Dice rolling game. {DIE_EMOJI}
2- Color guessing game. {PAINT_EMOJI}
3- Coinflip game. (Bet Points) {MONEY_EMOJI}
4- End gaming experience. {CHECKMARK_EMOJI}

Answer: """))

    if option == 1:
        dice()
    
    if option == 2:
        colorguess()
    
    if option == 3:
        new_points = coinflip(points)
        points = new_points
        games()
    
    if option == 4:
        print(f"Thank you for playing! You earned {points} point(s)!! Congratulations! Have a great day {player}!")


def dice() -> None:
    """The function for the dice rolling game option."""
    dice_roll = randint(1, 6)

    global points

    ready = input(f"""
Welcome to the dice rolling game. 
If you guess correctly on your first try you will win 10 points.
If you guess correctly within the first 3 tries you will gain 5 points.
If you fail to guess correctly within 3 tries you will not gain any points.
Do you want to play, {player}? Y/N: """)

    if ready == "Y":
        dice_count = 1

        while int(input("Pick a number 1-6. If you guessed incorrectly try again. ")) != dice_roll:
            dice_count += 1

        if dice_count == 1:
            print("Wow! You're psychic! Way to get 10 points!")
            points += 10
            games()

        if dice_count <= 3:
            print("You must be a really good guesser. Enjoy those 5 points!")
            points += 5
            games()

        if dice_count > 3:
            print("Sorry you weren't able to get it in 3 tries. You gained no points.")
            games()

    else:
        games()


def colorguess() -> None:
    """The function for the number guessing game option."""
    global points
    offset = randint(0, 3)
    color_list = ["Black", "Red", "Blue", "White"]
    color = color_list[offset]

    ready = input(f"""
Welcome to the color guessing game.
If you guess correctly on your first try you will win 10 points.
If you guess correctly within the first 2 tries you will gain 5 points.
If you fail to guess correctly within 2 tries you will not gain any points.
Do you want to play, {player}? Y/N: """)

    if ready == "Y":
        color_count = 1
        while input("Pick a color: Blue, White, Red, or Black. If you guessed incorrectly try again. ") != color:
            color_count += 1

        if color_count == 1:
            print("Yes! You're insane! That's 10 points for you!!")
            points += 10
            games()

        if color_count == 2:
            print("Wow that is so impressive! You got 5 points!")
            points += 5
            games()

        if color_count > 2:
            print("Sorry! You didn't it in two tries. You gained 0 points.")
            games() 

    else:
        games() 


def coinflip(points: int) -> int:
    """The function for coin flip game option."""
    ready = input(f"""
Welcome to the coin flipping game where you can gamble your points.
If you are able to correctly guess the coin toss you may double your points.
If you incorrectly guess the coin toss you will lose 5 points.
Do you want to play? {player} Y/N: """)

    if ready == "Y":
        
        heads_or_tails = ["Heads", "Tails"]

        if (input("Pick Heads or Tails: ")) == heads_or_tails[randint(0, 1)]:
            print("That's right! You have doubled your points!")
            return(int(points * 2))

        else:
            print("Sorry that was incorrect. You have lost five points.")
            return(int(points - 5))

    else:
        return(int(points))


if __name__ == "__main__":
    main()