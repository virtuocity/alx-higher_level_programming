#!/usr/bin/python3
import hidden_4
hidden_names = dir(hidden_4)
if __name__ == "__main__":
    for i in hidden_names:
        if i[:2] != '__':
            print("{}".format(i))
