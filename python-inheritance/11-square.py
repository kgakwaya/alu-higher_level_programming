#!/usr/bin/python3
from rectangle import Rectangle  # Adjust the import statement based on your project structure

class Square(Rectangle):
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)  # Call the Rectangle constructor

    def area(self):
        return self.__size ** 2  # Calculate area

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"  # String representation

    # Assuming integer_validator is defined in the Rectangle class

