n = int(input())
arr = list(map(int, input().split()))

max_sum = float("-inf")
curr_sum = 0

for a in arr:
	if curr_sum < 0:
		curr_sum = a
	else:
		curr_sum += a

	max_sum = max(max_sum, curr_sum)

print(max_sum)