n = int(input())

sets = []
for i in range(n):
	s = set()
	count_languages = int(input())
	for j in range(count_languages):
		s.add(input())
	sets.append(s)

every_know = sets[0]
even_one_know = sets[0]

for i in range(1, len(sets)):
	every_know = every_know.intersection(sets[i])
	even_one_know = even_one_know.union(sets[i])

every_know = list(every_know)
even_one_know = list(even_one_know)

print(len(every_know))
for lang in every_know:
	print(lang)

print(len(even_one_know))
for lang in even_one_know:
	print(lang)