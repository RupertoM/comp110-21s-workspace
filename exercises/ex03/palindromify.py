"""EX03 - palindromify function."""

__author__: str = "730408061"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(string: str, boolean: bool) -> str:
    """The function that palindromifies a string differently based on if it's even or odd."""
    new_string = ""
    if boolean is False:
        reverse_string = string[::-1]
        new_string = string + reverse_string[1:]
    
    if boolean is True:
        reverse_string = string[::-1]
        new_string = string + reverse_string
    
    return new_string


if __name__ == "__main__":
    main()