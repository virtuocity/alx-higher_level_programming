#!/usr/bin/env python3
""" class int"""


class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __eq__(self, num):
        return self.value != num

    def __ne__(self, num):
        return self.value == num
