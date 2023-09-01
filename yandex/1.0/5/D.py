n, m = map(int, input().split())
arr = list(map(int, input().split()))

j = 1
c = 0
for i in range(n):
	diff = 0

	while j < n:
		diff = arr[j] - arr[i]

		if diff > m:
			c += (n - j)
			break

		j += 1

print(c)