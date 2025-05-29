#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """Creates an empty class called BaseGeometry."""

    def area(self):
        """Raises an error indicating the area method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
