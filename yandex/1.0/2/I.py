def check(v):
	return v != "*"

n, m, k = map(int, input().split())

field = []

for i in range(n):
	field.append([0 for j in range(m)])

for bomb in range(k):
	i, j = map(int, input().split())
	field[i-1][j-1] = "*"

for i in range(n):
	for j in range(m):
		if field[i][j] == "*":
			if i > 0:
				if check(field[i-1][j]):
					field[i-1][j] += 1
			if j > 0:
				if check(field[i][j-1]):
					field[i][j-1] += 1
				if i > 0:
					if check(field[i-1][j-1]):
						field[i-1][j-1] += 1
				if i < n-1:
					if check(field[i+1][j-1]):
						field[i+1][j-1] += 1

			if i < n-1:
				if check(field[i+1][j]):
					field[i+1][j] += 1
				if j < m-1:
					if check(field[i+1][j+1]):
						field[i+1][j+1] += 1

			if j < m-1:
				if check(field[i][j+1]):
					field[i][j+1] += 1

				if i > 0:
					if check(field[i-1][j+1]):
						field[i-1][j+1] += 1

for i in range(n):
	print(*field[i])