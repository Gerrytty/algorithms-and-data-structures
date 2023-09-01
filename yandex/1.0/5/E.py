def add_to_d(d, num):
	if num not in d:
		d[num] = 1
	else:
		d[num] += 1

def remove(d, num):
	if d[num] > 1:
		d[num] -= 1
	else:
		del d[num]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# print(*range(n))

if m == 1:
	print(1, 1)
else:

	left = 0
	right = 1

	trees = {}

	trees[arr[left]] = 1

	min_dist = float("inf")
	pair = (0, n-1)

	prev_left = -1
	prev_right = -1
	c = 0

	last_added_right = -1

	while left < n:
		k = 0
		while right < n and len(trees) < m:
			# print("add ", arr[right])

			if last_added_right != right:
				add_to_d(trees, arr[right])
				last_added_right = right
			if len(trees) < m:
				right += 1

		# right -= 1
		# print(trees, left, right)

		if len(trees) == m:
			if m - 1 <= right - left < min_dist:
				min_dist = right - left
				pair = (left, right)
				# if right + 1 < n:
				# 	right += 1
				# print(pair)

		remove(trees, arr[left])
		# print("remove", arr[left])
		left += 1

	print(pair[0]+1, pair[1]+1)