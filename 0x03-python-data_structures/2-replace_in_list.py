#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1 or idx is None or idx < 0 or not my_list:
        return (my_list)
    my_list[idx] = element
    return (my_list)
