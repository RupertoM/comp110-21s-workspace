"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730408061"

# TODO: Your constructor and methods will go here.


class Simpy:
    """The Simpy Class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor for the Simpy class."""
        self.values = values

    def __repr__(self) -> str:
        """Makes any call on Simpy a string."""
        return (f"Simpy({self.values})")
    
    def fill(self, float_value: float, reps: int) -> None:
        """Fills Simpy with one integer a repititous amount of times."""
        self.values = []
        for index in range(reps):
            self.values.append(float_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Serves the same function as the range() function."""
        assert step != 0.0
        self.values = []
        value = start
        while abs(value) < abs(stop):
            self.values.append(value)
            value += step

    def sum(self) -> float:
        """Returns the sum of all components in a Simpy."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload of the + function for Simpy."""
        new_simpy = Simpy([])
        if type(rhs) == float:
            for value in self.values:
                new_simpy.values.append(value + rhs)

        else:
            for index in range(len(self.values)):
                new_simpy.values.append(self.values[index] + rhs.values[index])

        return new_simpy

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload of to the power for Simpy."""
        new_simpy = Simpy([])
        if type(rhs) == float:
            for value in self.values:
                new_simpy.values.append(value ** rhs)

        else:
            for index in range(len(self.values)):
                new_simpy.values.append(self.values[index] ** rhs.values[index])

        return new_simpy    

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload of modulo operator for Simpy."""
        new_simpy = Simpy([])
        if type(rhs) == float:
            for value in self.values:
                new_simpy.values.append(value % rhs)

        else:
            for index in range(len(self.values)):
                new_simpy.values.append(self.values[index] % rhs.values[index])

        return new_simpy

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload of == for Simpy."""
        return_list = []
        if type(rhs) == float:
            for value in self.values:
                return_list.append(value == rhs)

        else:
            for index in range(len(self.values)):
                return_list.append(self.values[index] == rhs.values[index])

        return return_list     

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload of == for Simpy."""
        return_list = []
        if type(rhs) == float:
            for value in self.values:
                return_list.append(value > rhs)

        else:
            for index in range(len(self.values)):
                return_list.append(self.values[index] > rhs.values[index])

        return return_list 

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload of subscription operator with two methods."""
        if type(rhs) == int:
            for index in range(len(self.values)):
                if index == rhs:
                    return self.values[index]

        else:
            return_simpy = Simpy([])
            for index in range(len(rhs)):
                if rhs[index]:
                    return_simpy.values.append(self.values[index])
        
        return return_simpy