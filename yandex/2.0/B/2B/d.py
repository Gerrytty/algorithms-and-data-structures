import math

length, n = map(int, input().split())
arr = list(map(int, input().split()))

def get_ans(arr, n):
	ans = []
	if n % 2 == 1:
		for a in arr:
			if a == n // 2:
				return [a]

	for a in arr:
		if a < n // 2:
			ans.append(a)
			break
	for a in arr:
		if a > n // 2:
			ans.append(a)
			break
	return ans

print(*get_ans(arr, length))