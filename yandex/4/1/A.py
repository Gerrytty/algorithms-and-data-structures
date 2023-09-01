import math

n = int(input())

s = 0

if n == 1:
	print(1)

for i in range(1, n):
	s += (i + 1)

	if s >= n:
		print(i)
		break