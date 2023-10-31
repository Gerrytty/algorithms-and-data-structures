n = int(input())

arr = list(map(int, input().split()))

s = 0

for i in range(len(arr)):
	s += abs(arr[i] - arr[0])

count_minus = len(arr) - 2
count_plus = 0

ans = [s]
for i in range(1, n):
	ans.append(ans[-1] - abs(arr[i] - arr[i-1]) * count_minus + abs(arr[i] - arr[i-1]) * count_plus)
	count_plus += 1
	count_minus -= 1

print(*ans)