def test_runner(func):
	def test(expected, *args):
		print(f"Testing {func.__name__}{args} and expecting {expected}")
		result = func(*args)
		if result != expected:
			print(f"❌ Failed: Expected {expected} but got {result}")
		else:
			print("✅ Passed")

	return test
	