n, m = map(int, input().split())

arr = list(map(int, input().split()))

k = 0

end = n
curr_sum = arr[0]
j = 1
for i in range(n):
	while curr_sum < m and j < n:
		if curr_sum == m:
			k += 1
		curr_sum += arr[j]

		j += 1
		end = j

	if curr_sum == m:
		k += 1

	curr_sum -= arr[i]

print(k)