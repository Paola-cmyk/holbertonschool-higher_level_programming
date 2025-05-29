#!/usr/bin/python3
"""Inheriting from the Rectangle class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the Square class inheriting from the Rectangle class."""

    def __init__(self, size):
        """Initializing width and height with validation."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return super().area()

    def __str__(self):
        """Returns a string representation of the square."""
        return (f"[Square] {self.__size}/{self.__size}")
