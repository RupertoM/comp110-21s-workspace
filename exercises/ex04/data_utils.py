"""Utility functions for wrangling data."""

__author__ = "730408061"


from csv import DictReader


def read_csv_rows(csv_file: str):
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

def column_values(rows_list, string):
    """A function that produces all values in a list into a single column"""
    columns = []

    for row in rows_list:
        columns.append(row[string])

    return columns