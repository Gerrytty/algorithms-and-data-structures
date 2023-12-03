arr = list(map(int, input().split()))
s = set()

for a in arr:
	if a in s:
		print("YES")
	else:
		s.add(a)
		print("NO")