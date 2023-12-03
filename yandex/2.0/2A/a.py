n, k = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(k):
	s = sum(arr)
	for j in range(n):
		arr[j] = s - arr[j]

print(max(arr) - min(arr))