#!/usr/bin/python3
"""CountedIterator - Keeps track of the iterations."""


class CountedIterator:
    """Class to mimic iter."""
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def __next__(self):
        """Overrides __next__, stops once no more items are found."""
        try:
            item = next(self.iterable)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the current count."""
        return self.count
