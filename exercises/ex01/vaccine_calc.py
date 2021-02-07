"""A vaccination calculator."""

__author__ = "730408061"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta

# Begin your solution here...

population = int(input("Enter the total number of people under consideration:"))
doses_adminestered = int(input("Enter the total number of vaccine doses already given to the population:"))
doses_per_day = int(input("Enter the total number of vaccine doses given each calendar day:"))
percent_vaccinated = int(input("Enter what percent of the population you wish to know will be vaccinated:"))

amount_to_vaccinate = (percent_vaccinated)/100 * (population)
#print(amount_to_vaccinate)
people_vaccinated = (doses_adminestered)/2
#print(people_vaccinated)
people_vaccinated_per_day = (doses_per_day)/2
#print(people_vaccinated_per_day)
people_left = amount_to_vaccinate - (people_vaccinated)
#print(people_left)
days_left = round(people_left / people_vaccinated_per_day)

today: datetime = datetime.today()
fortnight: timedelta = timedelta(days_left)

future: datetime = (today + fortnight)

future_date = future.strftime("%B %d, %Y")

print("We will reach " + str(percent_vaccinated) + "% vaccination in " + str(days_left) + " days, which falls on ", end="")
print(future_date)