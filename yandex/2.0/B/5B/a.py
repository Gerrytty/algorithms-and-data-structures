n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]

s = 0

for i in range(n):
	s += arr[i]
	prefix_sum.append(s)

for i in range(m):
	start, end = map(int, input().split())

	print(prefix_sum[end] - prefix_sum[start-1])