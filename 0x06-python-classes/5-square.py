#!/usr/bin/python3
# 5-square.py by Kelvin KIpkemboi
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
        self.size = size

    @property
    def size(self):
        """Retrieves size of the square"""
        
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """
        
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
