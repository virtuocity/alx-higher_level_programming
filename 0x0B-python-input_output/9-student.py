#!/usr/bin/python3
""" class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        obj_dict = {}
        if hasattr(self, '__dict__'):
            return (self.__dict__)
        return (obj_dict)
