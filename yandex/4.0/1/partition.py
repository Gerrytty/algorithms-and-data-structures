n = int(input())
arr = list(map(int, input().split()))
x = int(input())

less_x = 0
for i in range(n):
	if arr[i] < x:
		less_x += 1

print(less_x)
print(n - less_x)