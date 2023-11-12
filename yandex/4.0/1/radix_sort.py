def print_bucket(bucket, i):
	if bucket:
		print(f"Bucket {i}:", ", ".join(bucket))
	else:
		print(f"Bucket {i}:", "empty")

n = int(input())

if n == 0:
	print("Initial array:\n")
	print("**********\nSorted array:\n")
else:

	initial_array = []

	for i in range(n):
		initial_array.append(input())

	phase = 1

	print("Initial array:")
	print(", ".join(initial_array))
	print(f"**********\nPhase {phase}")

	phase += 1

	buckets = [[] for i in range(10)]

	curr_number = 1

	for i in range(n):
		buckets[int(initial_array[i][-curr_number])].append(initial_array[i])

	for i, bucket in enumerate(buckets):
		print_bucket(bucket, i)

	curr_number += 1

	end = False
	while not end:
		new_buckets = [[] for i in range(10)]
		for bucket in buckets:
			for num in bucket:
				if curr_number > len(num):
					end = True
					break
				new_buckets[int(num[-curr_number])].append(num)

			if end:
				break
		curr_number += 1
		if not end:
			buckets = new_buckets

			print(f"**********\nPhase {phase}")
			for i, bucket in enumerate(buckets):
				print_bucket(bucket, i)
			phase += 1


	res_arr = []

	for bucket in buckets:
		for num in bucket:
			res_arr.append(num)

	print("**********\nSorted array:")
	print(", ".join(map(str, res_arr)))
