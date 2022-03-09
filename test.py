from itertools import product

options = {0: [0, 10, 15], 1: [0, 10, 10], 2: [0, 12, 6]}
counter= 0
for x in product(*options.values()):
	print(x)