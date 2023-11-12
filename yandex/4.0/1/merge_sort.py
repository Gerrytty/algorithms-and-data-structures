import math

def merge(arr1, arr2, res_arr):

	left = right = i = 0

	while i < len(arr1) + len(arr2):
		
		if left == len(arr1) or right == len(arr2):
			break

		if arr1[left] <= arr2[right]:
			res_arr[i] = arr1[left]
			left += 1
		else:
			res_arr[i] = arr2[right]
			right += 1

		i += 1

	while left < len(arr1):
		res_arr[i] = arr1[left]
		i += 1
		left += 1
	while right < len(arr2):
		res_arr[i] = arr2[right]
		i += 1
		right += 1

	return res_arr


def merge_sort(arr):
	if len(arr) <= 1:
		return

	m = math.ceil(len(arr) / 2)
	left = arr[:m]
	right = arr[m:]

	merge_sort(left)
	merge_sort(right)
	arr = merge(left, right, arr)

	return arr

n = int(input())
arr1 = list(map(int, input().split()))
res = merge_sort(arr1)

if n < 2:
	print(*arr1)
else:
	print(*res)