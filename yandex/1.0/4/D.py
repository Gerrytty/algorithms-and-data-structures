n = int(input())

keyboard = list(map(int, input().split()))

m = int(input())

press = list(map(int, input().split()))


d = {}

for i, val in enumerate(keyboard):
	d[i + 1] = val

for i in range(m):
	d[press[i]] -= 1

for i in range(n):
	if d[i + 1] < 0:
		print("YES")
	else:
		print("NO")