#!/usr/bin/python3
""" Append to a file"""

def append_write(filename="", text=""):
	"""
	append_write - append data/text to file
	Args: 
		@filename: file to be appended
		@text: text to append
	Return:
		number of characters appended
	"""
	n = 0
	with open(filename, "a", encoding="utf-8") as f:
		n = f.write(text)
	return (n)
