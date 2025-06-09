#!/usr/bin/python3
"""
This module defines a CustomObject class for demonstrating
basic serialization and deserialization using Python's pickle module.

The pickle module is used to serialize (save) and deserialize (load)
instances of the CustomObject class to/from files.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with attributes for name,
    age, and student status.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): A boolean representing if the person is a student.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject with name, age, and student status.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student (True/False).
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject in a formatted string.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to
        the provided filename.

        Args:
            filename (str): The name of the file where the object
            will be serialized and saved.
        """
        try:
            with open(filename, 'wb') as pklfile:
                pickle.dump(self, pklfile)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes and loads an instance of CustomObject from
        the provided filename.

        Args:
            filename (str): The name of the file from which to
            load the object.

        Returns:
            CustomObject: The deserialized instance of
            the CustomObject.
        """
        try:
            with open(filename, 'rb') as pklfile:
                return pickle.load(pklfile)
        except Exception:
            return None
