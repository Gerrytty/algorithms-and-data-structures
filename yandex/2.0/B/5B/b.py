n = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0]
prefix_sum2 = [0]

s = 0
s2 = 0
max_min = float("-inf")

for i in range(len(arr)):
	if arr[i] <= 0:
		s = 0
		max_min = max(max_min, arr[i])
		arr[i] = 0
	s += arr[i]
	prefix_sum.append(s)
	prefix_sum2.append(s2)

print(prefix_sum)

if max(prefix_sum) == 0:
	print(max_min)
else:
	print(max(prefix_sum))