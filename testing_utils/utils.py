import concurrent.futures

def test_runner(func, timeout_seconds=1.0):
	def test(expected, *args, **kwargs):
		print(f"Testing {func.__name__}{args} and expecting {expected}")
		with concurrent.futures.ThreadPoolExecutor() as executor:
			future = executor.submit(func, *args)
			try:
				result = future.result(timeout=timeout_seconds)
				if result != expected:
					print(f"❌ Failed: Expected {expected} but got {result}")
				else:
					print("✅ Passed")
			except concurrent.futures.TimeoutError:
				print("❌ Failed: TimeoutError")
	return test
