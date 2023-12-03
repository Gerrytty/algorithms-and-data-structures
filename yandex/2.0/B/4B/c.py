d = {}
d_n_freq = {}

with open("input.txt") as file:
	for line in file:
		words = line.split()
		for word in words:
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1

arr = []

for key, value in d.items():
	if value not in d_n_freq:
		d_n_freq[value] = 1
	else:
		d_n_freq[value] += 1
	arr.append((value, key))

arr.sort(reverse=True)

curr_freq = -1

c = 0
while c < len(arr):
	word = arr[c]
	if d_n_freq[word[0]] != 1:
		for j in range(c + d_n_freq[word[0]]-1, c-1, -1):
			print(arr[j][1])
		c += d_n_freq[word[0]]
	else:
		print(word[1])
		c += 1