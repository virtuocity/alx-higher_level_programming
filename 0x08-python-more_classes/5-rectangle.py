#!/usr/bin/python3
"""Define the Rectangle class"""


class Rectangle:
    """class rectangule with area, perimeter"""

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        str_one = ""
        if self.__width == 0 or self.__height == 0:
            return str_one
        for i in range(0, self.__height):
            for j in range(self.__width):
                str_one += "#"
            if i is not (self.__height - 1):
                str_one += '\n'
        return str_one

    def __repr__(self):
        str_two = "Rectangle(" + str(self.__width) + ", " +\
            str(self.__height) + ")"
        return str_two

    def __del__(self):
        print("Bye rectangle...")
