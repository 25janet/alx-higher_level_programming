#!/usr/bin/python3
# 6-square.py by Kelvin KIpkemboi
"""Defines a square """

class Square:
    """Defines a square"""
    
    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of a Square
            position: where the square is (coordinates)
        """
        
        self.size = size
        self.position = position

    @property
    def size(self):
        """"The property of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """print the square in position"""
        
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
