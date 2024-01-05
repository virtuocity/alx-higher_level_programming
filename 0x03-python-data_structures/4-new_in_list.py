#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1 or idx is None or idx < 0 or my_list is None:
        return None
    new_list[idx] = element
    return (new_list)
