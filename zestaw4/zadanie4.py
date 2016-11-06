def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

for i in range(10):
    print(str(fibonacci(i)) + " " + str(i) )
