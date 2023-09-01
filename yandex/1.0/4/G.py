d = {}

with open("input.txt") as file:
	for line in file:
		operations = line.split()

		if operations[0] == "DEPOSIT":
			if operations[1] not in d:
				d[operations[1]] = int(operations[2])
			else:
				d[operations[1]] += int(operations[2])
		elif operations[0] == "INCOME":
			for key in d:
				if d[key] > 0:
					d[key] += int(d[key] / 100 * int(operations[1]))
		elif operations[0] == "BALANCE":
			if operations[1] not in d:
				print("ERROR")
			else:
				print(d[operations[1]])
		elif operations[0] == "WITHDRAW":
			if operations[1] not in d:
				d[operations[1]] = -int(operations[2])
			else:
				d[operations[1]] -= int(operations[2])
		elif operations[0] == "TRANSFER":
			if operations[1] not in d:
				d[operations[1]] = 0
			if operations[2] not in d:
				d[operations[2]] = 0

			d[operations[1]] -= int(operations[3])
			d[operations[2]] += int(operations[3])
