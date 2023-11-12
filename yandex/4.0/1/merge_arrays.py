n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

res = [0 for i in range(n + m)]

left = right = i = 0

while i < n + m:

	if left == n or right == m:
		break

	if arr1[left] <= arr2[right]:
		res[i] = arr1[left]
		left += 1
		
	elif right < m:
		res[i] = arr2[right]
		right += 1

	i += 1

while left < n:
	res[i] = arr1[left]
	i += 1
	left += 1
while right < m:
	res[i] = arr2[right]
	i += 1
	right += 1

print(*res)