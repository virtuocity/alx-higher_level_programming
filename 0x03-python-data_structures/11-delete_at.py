#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx > len_list - 1 or idx < 0 or not my_list:
        return my_list
    del my_list[idx]
    return (my_list)
