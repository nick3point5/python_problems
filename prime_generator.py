from typing import List

from testing_utils.utils import test_runner


def prime_generator(n: int)-> List[int]:
	"""
	Returns a list of prime numbers with length n.

	Example 1:
	Input: n = 5
	Output: [2, 3, 5, 7, 11]

	Example 2:
	Input: n = 10
	Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

	Example 3:
	Input: n = 0
	Output: []

	"""

	# your code goes here
	pass

if __name__ == "__main__":
		prime_generator_test = test_runner(prime_generator)

		prime_generator_test([2, 3, 5, 7, 11], 5)
		prime_generator_test([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 10)
		prime_generator_test([], 0)

		def prime_checksum(n: int) -> int:
				return sum(prime_generator(n))
		
		big_prime_test = test_runner(prime_checksum, timeout_seconds=10.0)
		big_prime_test(7472966967499, 1000000)
