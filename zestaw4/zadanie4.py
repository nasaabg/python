def fibonacci(n):
	x, y, z = [0, 0, 1]
	for i in range(n-1):
		x = y
		y = z
		z = x + y
	return z

print(fibonacci(8))
