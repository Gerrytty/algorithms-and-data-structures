
arr = []
with open("input.txt") as f:
	for line in f:
		arr.extend(line.split())

print(len(set(arr)))