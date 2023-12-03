d = {}

with open("input.txt") as f:
	for line in f:
		a, b = line.split()
		b = int(b)

		if a not in d:
			d[a] = b
		else:
			d[a] += b

d = dict(sorted(d.items()))

for key, value in d.items():
	print(key, value)