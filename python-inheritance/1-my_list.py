#!/usr/bin/python3
"""
This module defines a class `MyList` that inherits from
the built-in list class.
It includes a public instance method `print_sorted` to print
the list elements in ascending sorted order.
"""


class MyList(list):
    """
A subclass of list with an additional method to print the list in sorted order.
"""
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        Assumes that all elements in the list are type int.
        """
        print(f"{sorted(self)}")
