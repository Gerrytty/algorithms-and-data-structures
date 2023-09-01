n, k = map(int, input().split())
nums = list(map(int, input().split()))

d = {}

ans_if_find = False

for i, num in enumerate(nums):
	if num not in d:
		d[num] = [i]
	else:
		for a in d[num]:
			if abs(i - a) <= k:
				ans_if_find = True
				break
		d[num].append(i)
	if ans_if_find:
		break

if ans_if_find:
	print("YES")
else:
	print("NO")