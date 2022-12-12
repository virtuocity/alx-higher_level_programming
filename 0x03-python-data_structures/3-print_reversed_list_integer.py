#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    sizeoflist = len(my_list)
    idx = 0
    sizeoflist -= 1
    for x in my_list:
        my_list[idx] = my_list[sizeoflist]
	idx += 1
        sizeoflist -= 1
    print(my_list)	
