#!/usr/bin/python3
# 3-square.py by Kelvin KIpkemboi
"""Defines a square """

class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if the size is not an integer
            ValueError: if size is less than zero
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate the area of the square
        Returns: The square of the size
        """
        return self.__size ** 2
