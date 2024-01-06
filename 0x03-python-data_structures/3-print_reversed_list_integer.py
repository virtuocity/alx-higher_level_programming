#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        print("{}".format(my_list))
    len_list = len(my_list)
    my_list.reverse()
    for i in range(0, len_list):
        print("{:d}".format(my_list[i]))
