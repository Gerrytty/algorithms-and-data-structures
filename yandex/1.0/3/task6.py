def create_pairs(input_text):
	d = {}

	for i in range(len(input_text) - 1):
		s = f"{input_text[i]}{input_text[i+1]}"
		if s not in d.keys():
			d[s] = 1
		else:
			d[s] += 1

	return d

gen1 = input()
gen2 = input()

dict1 = create_pairs(gen1)
dict2 = create_pairs(gen2)

set1 = set(list(dict1.keys()))
set2 = set(list(dict2.keys()))
intersection = list(set1.intersection(set2))

ans = 0

for gen in intersection:
	ans += dict1[gen]

print(ans)