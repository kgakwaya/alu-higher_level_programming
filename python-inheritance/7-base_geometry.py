#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    This module defines a BaseGeometry class.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer and greater than 0.
        """

        if type(value

