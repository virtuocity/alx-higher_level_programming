#!/usr/bin/python3
"""class mylist"""


class MyList(list):
    """Implement lists"""
    def print_sorted(self):
        """Sort a list
        Args:
        list object
        Return:
        Sorted list
        """
        print(sorted(self))
