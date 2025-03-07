#!/usr/bin/python3
"""
Module: 11-square
Contains a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Calculate the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
