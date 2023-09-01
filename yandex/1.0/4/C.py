d = {}

with open("input.txt") as f:
	for line in f:
		words = line.split()
		for word in words:
			if word not in d.keys():
				d[word] = 1
			else:
				d[word] += 1


max_freq = -1

for key in d.keys():
	if d[key] > max_freq:
		max_freq = d[key]

ans = []
for key in d.keys():
	if d[key] == max_freq:
		ans.append(key)

ans.sort()

print(ans[0])