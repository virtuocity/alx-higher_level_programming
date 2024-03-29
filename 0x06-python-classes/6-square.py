#!/usr/bin/python3
'''
square class
'''


class Square:
    '''
    class square with private instance attribute size
    '''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) != int or type(position[1]) != int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """ return area of swuare"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ return the value of position"""
        return self.__position

    @position.setter
    def position(self, position):
        """ position setter """
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) != int or type(position[1]) != int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("{}". format(" "), end="")
                for j in range(self.__size):
                    print("{}". format("#"), end="")
                print()
