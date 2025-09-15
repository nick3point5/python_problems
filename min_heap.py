from typing import List

from testing_utils.utils import test_runner


class min_heap:
	"""
	Min heap implementation
	"""
	def __init__(self, array: List[int] = []):
		"""
		Initializes the min heap
		"""
		# your code goes here
		pass

	def insert(self, value: int):
		"""
		Inserts a value into the min heap
		"""
		# your code goes here
		pass

	def pop(self) -> int:
		"""
		Returns the min value from the min heap and removes it
		"""
		# your code goes here
		pass

	def peek(self) -> int:
		"""
		Returns the min value from the min heap
		"""
		# your code goes here
		pass

	def size(self) -> int:
		"""
		Returns the size of the min heap
		"""
		# your code goes here
		pass


if __name__ == "__main__":
	h = min_heap([10, 6, 3, 5, 2, 1, 9, 8, 7, 4])

	test_peek = test_runner(lambda h: h.peek())
	test_insert = test_runner(lambda h, value: h.insert(value))
	test_pop = test_runner(lambda h: h.pop())
	test_size = test_runner(lambda h: h.size())

	test_size(10, h)
	test_peek(1, h)
	test_size(10, h)
	test_pop(1, h)
	test_pop(2, h)
	test_pop(3, h)
	test_pop(4, h)
	test_pop(5, h)
	test_size(5, h)
	test_insert(None, h, 2)
	test_size(6, h)
	test_peek(2, h)
	test_insert(None, h, 3)
	test_size(7, h)
	test_peek(2, h)
