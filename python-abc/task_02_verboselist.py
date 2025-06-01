#!/usr/bin/python3
"""Extending the Python List with notifications for adding and removing"""
__import__("sys")


class VerboseList(list):
    """Class used to modify the Python List."""
    def append(self, append):
        print(f"Added [{append}] to the list.")
        return super().append(append)

    def extend(self, extend):
        print(f"Extended the list with [{len(extend)}] items.")
        return super().extend(extend)

    def remove(self, remove):
        print(f"Removed [{remove}] from the list.")
        return super().remove(remove)

    def pop(self, pop=-1):
        print(f"Popped [{self[pop]}] from the list.")
        return super().pop(pop)
