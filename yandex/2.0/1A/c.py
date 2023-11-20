count_zero = 0
count_cross = 0

for i in range(3):
	line = input().split()
	for sign in line:
		if sign == "1":
			count_cross += 1
		if sign == "2":
			count_zero += 1

if count_cross - count_zero > 1 or count_cross - count_zero < 0:
	print("NO")
else:
	print("YES")