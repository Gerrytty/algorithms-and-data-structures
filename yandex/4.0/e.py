n = int(input())

arr = list(map(int, input().split()))

ans = []
for i in range(n):
	mark = arr[i]
	s = 0
	for j in range(n):
		s += abs(arr[i] - arr[j])

	ans.append(s)

print(*ans)