#!/usr/bin/python3
'''
square class
'''


class Square:
    '''
    class square with private instance attribute size
    '''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
