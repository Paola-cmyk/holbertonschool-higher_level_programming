#!/usr/bin/python3
"""Duck typing"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class representing a generic shape.

    Methods:
        area: Abstract method to calculate the area of the shape.
        perimeter: Abstract method to calculate the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize the Circle instance with a radius.

        Args:
            radius (float): The radius of the circle.
        """
        if type(radius) in [int, float]:
            self.radius = abs(radius)

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (pi * (self.radius ** 2))

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return (2 * pi * self.radius)


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle instance with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if type(width) in [int, float]:
            self.width = width

        if type(height) in [int, float]:
            self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return (2 * self.height) + (2 * self.width)


def shape_info(shape):
    """
    Display the area and perimeter of a shape.

    Args:
        shape (Shape): An instance of a class that implements
        the Shape interface.
    """

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
