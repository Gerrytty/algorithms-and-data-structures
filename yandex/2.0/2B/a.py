a = int(input())
maximum_number = a
maximum_number_count = 1
while a != 0:
	a = int(input())

	if a == maximum_number:
		maximum_number_count += 1
	elif a > maximum_number:
		maximum_number_count = 1
		maximum_number = a

print(maximum_number_count)