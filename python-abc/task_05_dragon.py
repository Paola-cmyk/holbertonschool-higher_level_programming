#!/usr/bin/python3
"""Dragon class that represents a dragon."""


class SwimMixin:
    """SwimMixin class created for the Dragon class to inherit from."""
    def swim(self):
        """Swimming method created for the Dragon class to inherit from."""
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class created for the Dragon class to inherit from."""
    def fly(self):
        """Flying method created for the Dragon class to inherit from."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class to represent a dragon, inherits from both
    the FlyMixin and SwimMixin classes."""
    def roar(self):
        """Roar method added inside the Dragon class."""
        print("The dragon roars!")
