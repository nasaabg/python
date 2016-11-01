def flatten_sequence(sequence):
	for el in sequence:
		if isinstance(el,(list, tuple)):
			yield from flatten_sequence(el)
		else:
			yield el

print(list(flatten_sequence([1,2,3,[4,5],[[6],[7],8,9], 10])))
