#!/usr/bin/python3
def element_at(my_list, idx):
    sizeoflist = len(my_list)
    if idx < 0:
        return None
    if idx > sizeoflist - 1 or idx is None or my_list is None:
        return None
    return (my_list[idx])
