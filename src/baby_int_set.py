# baby_int_set.py
class UnsupportedTypeError(Exception):
    """Custom Exception"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 


class BabyIntegerSet:
	"""A class the mimics the behavior of python's built in 
	Set class. Implemented as a list. Can only store integers."""

	def __init__(self, d=[]):
		"""A BabyIntegerSet can be initialized with a list."""
		self.__data = []
		self.addSeq(d)

	def __repr__(self):
		"""Returns a string representation of the set."""

		s = ', '.join([str(i) for i in self.__data])
		return s

	def dump_data(self):
		return self.__data

	def add(self, elem):
		"""Add element elem to the set only if it is 
		unique to the set. 

		Raises UnsupportedTypeError if elem is not type int.
		"""
		if type(elem) != int:
			raise UnsupportedTypeError(str(elem) + ' is not a valid integer.')
		
		for i in self.__data:
			if i == elem:
				return # Nothing to add, elem already exists
		
		self.__data.append(elem)

	def addSeq(self, seq):
		"""Add contents of seq to the set where each item in contents 
		is unique to the set."""
		for i in seq:
			self.add(i)

	def remove(self, elem):
		"""Removes and returns the element elem from the set. 

		Raises KeyError if elem is not contained in the set.
		"""
		pass

	def get(self, elem):
		"""Returns element elem from the set. 

		Raises KeyError if elem is not contained in the set.
		"""
		pass
	
	def clear(self):
		"""Remove all elements from the set."""
		pass

	def size(self):
		"""Returns the size of the set."""
		pass

	def sum_all(self):
		"""Returns the sum of all integers in the set."""
		pass

	def product_all(self):
		"""Returns the product of all integers in the set."""
		pass

	def get_min(self):
		"""Returns the smallest integer in the set."""
		pass

	def get_max(self):
		"""Returns the largest integer in the set."""
		pass

	def sortme(self):
		"""Returns a copy of the set sorted. See python's sorted method."""
		pass

	def remove_seq(self, seq):
		#"""Removes each item in seq from set. Make sure to enclose
		#each removal in try/except block."""

		try:
			self._data.remove()
		except ValueError:
			pass 
			

	def remove_all_odds(self):
		"""Removes all odd numbers from the set."""
		pass

# End of class BabyIntegerSet



