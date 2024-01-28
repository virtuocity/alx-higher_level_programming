#!/usr/bin/python3
""" Singly linked list node"""


class Node:
    """ class Node"""
    def __init__(self, data=0, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
         return (self.__data)

    @data.setter
    def data(self, value):
         if type(value) != int:
            raise TypeError("data must be an integer")
         self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    
    class SinglyLinkedList:
        """ class to initialize node """
        