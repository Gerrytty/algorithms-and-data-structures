n, m = map(int, input().split())

W = input()
S = input()

d_of_W = {}

for letter in W:
	if letter not in d_of_W:
		d_of_W[letter] = 1
	else:
		d_of_W[letter] += 1

count = 0

s = S[:n]

d_of_S = {}

for letter in s:
	if letter not in d_of_S:
		d_of_S[letter] = 1
	else:
		d_of_S[letter] += 1

bias = 0

if d_of_W == d_of_S:
		count += 1

for i in range(1, m - n + 1):

	d_of_S[S[bias]] -= 1

	if d_of_S[S[bias]] == 0:
		del d_of_S[S[bias]]

	if  S[i + n - 1] not in d_of_S:
		d_of_S[S[i + n - 1]] = 1
	else:
		d_of_S[S[i + n - 1]] += 1

	if d_of_W == d_of_S:
		count += 1

	bias += 1

print(count)