from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog subclass derived from the Animal class."""
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """Cat subclass derived from the Animal class."""
    def sound(self):
        return ("Meow")
