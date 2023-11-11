def partition3(arr, x, left, right):

	gt, ls, eq = 5, 2, 4

	i = 0

	while True:
		print(arr[left])

		while arr[left] < x:
			left += 1

		while arr[right] > x:
			right -= 1

		while arr[eq] == x:
			eq += 1

		break

arr = [1, 2, 3, 6, 6, 8, 1, 5, 4]
partition3(arr, 6, 5, len(arr)-1)

raise Exception

# def partition(arr, x):
# 	i = 0
# 	j = len(arr)
#     while i <= j: 
#     	while (a[i] < v):
#     		i += 1
#         while a[j] > v:
#            j -= 1
#         if (i >= j) 
#            break
#         swap(a[i++], a[j--])
#      return j

# def partition(arr, x):
# 	i = 0
# 	j = len(arr) - 1

# 	while i <= j:
# 		while arr[i] < x:
# 			i += 1

# 		while arr[j] > x:
# 			j -= 1

# 		if i <= j:
# 			arr[i], arr[j] = arr[j], arr[i]
# 			i += 1
# 			j -= 1

import random


def partition(items, left, right, pivot):
	while True:
		while items[left] < pivot:
			left += 1

		while items[right] > pivot:
			right -= 1

		if left >= right:
			print(right)
			return right

		items[left], items[right] = items[right], items[left]
		right -= 1
		left += 1




def sort(items, left, right):
	length = right - left + 1

	if length < 2:
		return

	pivot = items[random.randint(left, right)]
	split_index = partition(items, left, right, pivot)
	sort(items, left, split_index)
	sort(items, split_index + 1, right)



# with open("input.txt") as f:
# 	f.readline()
# 	arr = list(map(int, f.readline().split()))
# 	# print(len(arr))
# 	sort(arr, 0, len(arr) - 1)

# with open("output.txt", "w+") as f:
# 	f.write(" ".join(list(map(str, arr))))

arr = [8, 4, 1, 2, 6, 7, 3, 4]
# arr = [1, 1, 1, 1, 1, 1]
partition(arr, 0, len(arr)-1, 6)
print(arr)

# n = input()
# arr = list(map(int, input().split()))

sort(arr, 0, len(arr)-1)

print(*arr)