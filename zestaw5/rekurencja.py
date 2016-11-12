#!/usr/bin/python

def factorial(n):
	value = 1
	for i in range(1, n + 1):
		value = value * i
	return value

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
