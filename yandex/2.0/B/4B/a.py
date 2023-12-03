n = int(input())

d = {}

for i in range(n):
	a, b = map(int, input().split())

	if a not in d:
		d[a] = b
	else:
		d[a] += b

d = dict(sorted(d.items()))

for key, value in d.items():
	print(key, value)