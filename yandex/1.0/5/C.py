n = int(input())

arr = []

for i in range(n):
	arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

prefix_sums1 = [0 for i in range(n)]
prefix_sums2 = [0 for i in range(n)]

s1 = 0
s2 = 0
for i in range(n-1):
	diff = arr[i+1][1] - arr[i][1]

	if diff > 0:
		s1 += diff

	if diff < 0:
		s2 += diff

	prefix_sums1[i+1] = s1
	prefix_sums2[i+1] = s2

def get_diff(prefix_sum_array, start, end):
	return prefix_sum_array[end] - prefix_sum_array[start]

m = int(input())

for i in range(m):
	start, end = map(int, input().split())

	if start < end:
		print(get_diff(prefix_sums1, start-1, end-1))

	elif start == end:
		print(0)

	else:
		print(abs(get_diff(prefix_sums2, end-1, start-1)))