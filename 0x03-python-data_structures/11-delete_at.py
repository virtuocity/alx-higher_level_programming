#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx < 0 or idx is None or idx > len_list - 1:
        return my_list
    new_list = []
    for i in range(0, len_list):
        if i != idx:
            new_list.append(my_list[i])
    return (new_list)
