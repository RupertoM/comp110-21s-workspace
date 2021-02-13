"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730408061"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Fortune Cookie Spitting Function."""
    random_number = randint(0, 100)

    if random_number <= 50:
        if random_number <= 25:
            return("You will be joyful and successful.")

        else:
            return("Your life will be prosperous and full of love.")

    else:
        if random_number <= 75:
            return("You will find fulfillment in the small things in life.")

        else:
            return("You will have the most amazing life in the universe!")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
