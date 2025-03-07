#!/usr/bin/python3
"""
Module containing the Rectangle class inheriting from BaseGeometry.
"""

class BaseGeometry:
    """BaseGeometry class with integer validation."""
    def integer_validator(self, name, value):
        """Validates that a given value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize width and height with validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __dir__(self):
        """Return list of attributes for dir(Rectangle)."""
        return super().__dir__()

    def __str__(self):
        """Return string representation of Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
