#!/usr/bin/python3
"""Rectangle class that inherits from the BaseGeometry class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using the BaseGeometry class."""

    def __init__(self, width, height):
        """Initializes the width and height with validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return (f"[Rectangle] {self.__width}/{self.__height}")
