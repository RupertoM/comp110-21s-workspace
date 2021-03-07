"""EX03 - prime functions."""

__author__: str = "730408061"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(873))
    print(list_primes(10, 20))


def is_prime(number: int) -> bool:
    """Function that determines if a number is prime."""
    if number > 1:
        if number != 2:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            else:
                return True
    else:
        if number == 1 or (number < 0):
            return False
    
    if number == 0:
        return False
    
    if number == 2:
        return True
    
    return True


def list_primes(number1: int, number2: int) -> list[int]:
    """A function that finds prime numbers between two numbers including the first but not second."""
    prime_list = []
    for number in range(number1, number2):
        if is_prime(number) is True:
            prime_list.append(number)
    
    return prime_list


if __name__ == "__main__":
    main()