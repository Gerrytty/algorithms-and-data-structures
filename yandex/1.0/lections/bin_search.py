arr = [1, 2, 3, 4, 5, 6, 8]

target = 7

low = 0
high = len(arr) - 1

while low != high:
	mid = (low + high + 1) // 2

	if arr[mid] < target:
		low = mid
	else:
		high = mid - 1
		mid -= 1

print(mid)