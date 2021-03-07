"""EX03 - avoid_fifth function."""

__author__: str = "730408061"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("taaar heeeelse"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(string: str) -> str:
    """Function that will return a string without the letter E."""
    new_string = ""
    
    for letter in string:
        if letter != "e":
            if letter != "E":
                new_string += letter

    return new_string


if __name__ == "__main__":
    main()