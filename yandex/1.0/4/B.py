d = {}

out = []
with open("input.txt") as f:
	for line in f:
		words = line.split()
		for word in words:
			if word not in d.keys():
				out.append(0)
				d[word] = 1
			else:
				out.append(d[word])
				d[word] += 1

print(*out)