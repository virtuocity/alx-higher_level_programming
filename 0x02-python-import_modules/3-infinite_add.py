#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv)
    args_list = sys.argv
    sum = 0
    if len_args == 1:
        print("0")
    elif len_args == 2:
        print("{}".format(args_list[1]))
    else:
        for i in range(1, len_args):
            sum = int(args_list[i]) + sum
        print("{}".format(sum))
