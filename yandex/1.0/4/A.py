with open("input.txt") as file:
	n = 0
	d1 = {}
	d2 = {}

	for i, line in enumerate(file):
		if i == 0:
			n = int(line)
		elif i <= n:
			word1, word2 = line.split()
			d1[word1] = word2
			d2[word2] = word1
		else:
			line = line.replace("\n", "")
			if line in d1:
				print(d1[line])
			else:
				print(d2[line])