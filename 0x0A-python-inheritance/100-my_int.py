#!/usr/bin/env python3
""" modified class int"""


class MyInt(int):
	"""
	MyInt - class to modify int
	class from qhich it inherits
	"""
	def __init__(self, value):
		"""
		init - constructor
		Args:
			self- the object
			value - int 
		"""
		  self.value = value

	def __eq__(self, num):
		"""eq - modify from == to !=
		   Args:
				self- instance of class
				num-value to check
		"""
		   return self.value != num

	def __ne__(self, numb):
		"""
			ne - modify from != to ==
			Args:
			   self- instance of class
			   num-value to check
		"""
		 return self.value == num
