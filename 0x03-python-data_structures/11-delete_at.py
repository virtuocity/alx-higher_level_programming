#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx > len_list - 1 or idx is None or not my_list:
        return my_list
    new_list = []
    for i in range(0, len_list):
        if i != idx:
            new_list.append(my_list[i])
    return (new_list)
