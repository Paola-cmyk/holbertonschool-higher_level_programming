#!/usr/bin/python3
"""Basic serialization module from Python to JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes and saves the data to a JSON file.

    Args:
        data (any): The data to be serialized (must be JSON serializable).
        filename (str): The name of the file where the data will be saved.
    """
    with open(filename, 'w', encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


def load_and_deserialize(filename):
    """
    Deserializes and loads the data from a JSON file.

    Args:
        filename (str): The name of the file from which to load the data.

    Returns:
        any: The data deserialized from the JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as jsonfile:
        return json.load(jsonfile)
