#!/usr/bin/python3
"""FlyingFish - Inherits from both Fish and Bird classes."""


class Fish:
    """Class to represent a fish."""

    def swim(self):
        """Swimming method for the Fish class."""
        print("The fish is swimming")

    def habitat(self):
        """Habitat method for the Fish class."""
        print("The fish lives in water")


class Bird:
    """Class to represent a bird."""

    def fly(self):
        """Flying method for the Bird class."""
        print("The bird is flying")

    def habitat(self):
        """Habitat method for the Bird class."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class to represent a flying fish, that inherits from both
    the Fish and Bird classes."""

    def fly(self):
        """Flying method for the FlyingFish class."""
        print("The flying fish is soaring!")

    def swim(self):
        """Swimming method for the FlyingFish class."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat method for the FlyingFish class."""
        print("The flying fish lives both in water and the sky!")
