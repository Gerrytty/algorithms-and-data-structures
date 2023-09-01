n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

def compare(arr1, arr2):
	min_diff = float("inf")
	min_arr = None

	start = 0

	for i in range(len(arr1)):
		local_min_diff = float("inf")
		for j in range(start, len(arr2)):
			diff = abs(arr1[i] - arr2[j])

			if diff > local_min_diff:
				break

			if diff < local_min_diff:
				local_min_diff = diff

			# print(start, (i, j), (arr1[i], arr2[j]), min_diff, diff)
			if diff < min_diff:
				min_diff = diff
				min_arr = [arr1[i], arr2[j]]

			if diff > min_diff:
				start = j

			if diff == 0:
				return min_arr

	return min_arr



if n >= m:
	print(*compare(arr1, arr2))
else:
	print(*compare(arr2, arr1)[::-1])