"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730408061"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    future_string = future_date(days)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + future_string)


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Function to find number of days until target percent of population is vaccinated."""
    amount_to_vaccinate = (target / 100) * (population)
    people_vaccinated = (doses) / 2
    people_vaccinated_per_day = (doses_per_day) / 2
    people_left = amount_to_vaccinate - (people_vaccinated)
    days_left = round(people_left / people_vaccinated_per_day)

    return days_left


# TODO 3: Define future_date function
def future_date(days: int) -> str:
    """Function to convert the number of days left into a written out date string."""
    today: datetime = datetime.today()

    fortnight: timedelta = timedelta(days)

    future: datetime = (today + fortnight)

    future_date = future.strftime("%B %d, %Y")

    return future_date
    

if __name__ == "__main__":
    main()
