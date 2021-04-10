"""Utility functions for wrangling data."""

__author__ = "730408061"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []

    # TODO 0.1) Complete the implementation of this function here.

    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        rows.append(row)

    file_handle.close()

    return rows


# TODO: Define the other functions here.

def column_values(rows_list: list[dict[str, str]], string: str) -> list[str]:
    """A function that produces all values in a list into a single column."""
    columns = []

    for row in rows_list:
        columns.append(row[string])

    return columns


def columnar(list_of_dict: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function that transfroms a table of rows into a dict of columns."""
    return_dict = {}
    for row in list_of_dict:
        for column in row:
            return_dict[column] = column_values(list_of_dict, column)
        
    return return_dict


def head(dictionary: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Prodcues new column-based table with only first N rows of data."""
    return_dictionary = {}
    for column in dictionary:
        empty_list = []
        if number == 0:
            return_dictionary[column] = empty_list
        if number > len(dictionary[column]):
            return_dictionary[column] = dictionary[column]
        else:
            for i in range(number):
                empty_list.append(dictionary[column][i])
                return_dictionary[column] = empty_list

    return return_dictionary
            

def select(dictionary: dict[str, list[str]], list_columns: list[str]) -> dict[str, list[str]]:
    """A function that produces a new column based table with specific subsets."""
    return_dictionary = {}
    for column in list_columns:
        return_dictionary[column] = dictionary[column]

    return return_dictionary


def count(list_of_strings: list[str]) -> dict[str, int]:
    """Given a list function produces a dictionary and counts amount of times unique values appear."""
    return_dictionary = {}
    count = 0
    for item in list_of_strings:
        if item in return_dictionary:
            count += 1
        else:
            count = 1
        return_dictionary[item] = count
    
    return return_dictionary
