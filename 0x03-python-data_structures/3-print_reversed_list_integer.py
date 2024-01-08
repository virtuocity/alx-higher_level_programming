<<<<<<< HEAD
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
=======
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        print("{}".format(my_list))
    len_list = len(my_list)
    my_list.reverse()
    for i in range(0, len_list):
        print("{:d}".format(my_list[i]))
>>>>>>> 1ea47daa1366acd9a9c252c6057df225e2494be7
