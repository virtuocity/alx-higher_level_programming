#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_of_args = len(sys.argv)
    if num_of_args == 1:
	    print("{} arguments.".format(numofargs - 1))
    elif num_of_args == 2:
	    print("{} argument.".format(numofargs - 1))
		print("{}: {}".format(1, args[1]))
	else:
		print("{} arguments.".format(numofargs - 1))
		for i in range(1, num_of_args):
		    print("{}: {}".format(i, args[i]))
