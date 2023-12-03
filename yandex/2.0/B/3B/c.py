arr = list(map(int, input().split()))

d = dict.fromkeys(set(arr), 0)

for a in arr:
	d[a] += 1

ans = []

for a in arr:
	if d[a] == 1:
		ans.append(a)

print(*ans)