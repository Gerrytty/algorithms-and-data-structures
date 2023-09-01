
arr = list(map(int, input().split()))

first_max = float("-inf")
first_max_id = -1
second_max = float("-inf")
first_min = float("inf")
first_min_id = -1
second_min = float("inf")

for i in range(len(arr)):
	if arr[i] > first_max:
		first_max = arr[i]
		first_max_id = i

for i in range(len(arr)):
	if arr[i] > second_max and i != first_max_id:
		second_max = arr[i]

for i in range(len(arr)):
	if arr[i] < first_min:
		first_min = arr[i]
		first_min_id = i

for i in range(len(arr)):
	if arr[i] < second_min and i != first_min_id:
		second_min = arr[i]

if first_max * second_max > first_min * second_min:
	print(second_max, first_max)
else:
	print(first_min, second_min)
