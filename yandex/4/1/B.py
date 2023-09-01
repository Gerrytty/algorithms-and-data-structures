path = input()

splitted = path.split("/")
ok = [0] * len(splitted)

for i, split in enumerate(splitted):
	if split != '' and split != '.':
		ok[i] = 1
	if split == '..':
		c = 1
		while ok[i - c] != 1 and i - c >= 0: 
			c += 1
		
		ok[i - c] = 0
		ok[i] = 0

result = []

for i, is_ok in enumerate(ok):
	if is_ok == 1:
		result.append(splitted[i])

print("/" + "/".join(result))