def is_multiple(n, m):
	 if isinstance(n, int) is False or isinstance(m, int) is False:
	 	print("两个参数都要是整数")

	 else:
	 	return n % m == 0

print(is_multiple(15, 14))

