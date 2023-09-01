n = int(input())

d = {}

for i in range(n):
	w, h = map(int, input().split())

	if w not in d.keys():
		d[w] = h
	else:
		if h > d[w]:
			d[w] = h
ans = 0

for key in d.keys():
	ans += d[key]

print(ans)