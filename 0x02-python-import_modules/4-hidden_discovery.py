#!/usr/bin/python3
import hidden_4
hidden_names = dir(hidden_4)
for i in hidden_names:
    if i[:2] != '__':
        print("{}".format(i))
