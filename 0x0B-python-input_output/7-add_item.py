#!/usr/bin/python3
"""  a script that adds all arguments to a Python list,~
and then save them to a file
"""
import sys
import json


my_list = []
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # try to load arguments from JSON file if it exists
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    # if not found, arguments list remains empty
    my_list = []
# get command line arguments
for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, "add_item.json")
