n, m = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(m):
	left, right = map(int, input().split())

	minumum = min(arr[left:right+1])
	maximum = max(arr[left:right+1])

	if minumum == maximum:
		print("NOT FOUND")
	else:
		print(maximum)