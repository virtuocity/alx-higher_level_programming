#!/usr/bin/python3
""" Class Rectangle that inherits from Base Geometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ empty class BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
