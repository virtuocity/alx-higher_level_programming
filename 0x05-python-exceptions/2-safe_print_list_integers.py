#!/usr/bin/python3
""" print integers in list"""


def safe_print_list_integers(my_list=[], x=0):
    """ safe_print_list_integers - safe print list of integers
        Args:
            my_list: list
            x: number of elements to print
    """
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return n
