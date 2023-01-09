#!/usr/bin/python3
"""
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    l = len(my_list) - 1
    if idx < 0 or idx > l or idx is None or my_list is None:
        return (my_list)
    else:
        new_list[idx] = element
    return (new_list)
"""
#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1 or idx < 0 or my_list is None or idx is None:
        return (my_list)
    new_list[idx] = element
    return (new_list)

