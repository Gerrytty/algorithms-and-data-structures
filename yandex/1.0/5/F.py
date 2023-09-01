n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())

classes = []

for i in range(m):
	power, price = map(int, input().split())
	classes.append((power, price))

classes.sort(key=lambda x: x[1])

# print(classes)

full = 0

i = 0
for clazz in arr:
	while i < len(classes) and classes[i][0] < clazz:
		i += 1

	# print(classes[i])

	# if in_while:
	# 	i -= 1

	# print(i, classes[i], clazz)

	full += classes[i][1]

print(full)