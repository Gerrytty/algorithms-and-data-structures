n = int(input())
arr = list(map(int, input().split()))

index_min = 0
index_max = 0

max_diff = 0


for i in range(0, len(arr)):
	for j in range(i + 1, len(arr)):
		count_of_gass = 1 / (arr[j] / 1000)
		diff = arr[j] * count_of_gass - arr[i] * count_of_gass
		if diff > max_diff:
			max_diff = diff
			index_min = i
			index_max = j

if index_min == index_max:
	print(0, 0)
else:
	print(index_min + 1, index_max + 1)