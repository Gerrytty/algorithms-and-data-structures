n, m = map(int, input().split())

W = input()
S = input()

d_of_W = {}

for letter in W:
	if letter not in d_of_W:
		d_of_W[letter] = 1
	else:
		d_of_W[letter] += 1

count_ok = 0

s = S[:n]

d_of_S = {}

for letter in s:
	if letter not in d_of_S:
		d_of_S[letter] = 1
	else:
		d_of_S[letter] += 1

bias = 0

count_comp = 0

for key in d_of_S.keys():
	if key in d_of_W and d_of_W[key] == d_of_S[key]:
		count_comp += 1

if count_comp == len(d_of_W):
	count_ok += 1

def modify(sd, wd, letter, flag):

	ans = 0

	if letter not in sd:
		sd[letter] = 0

	if letter in wd and  sd[letter] == wd[letter]:
		ans -= 1

	sd[letter] += flag

	if letter in wd and sd[letter] == wd[letter]:
		ans += 1

	return ans

for i in range(1, m - n + 1):

	letter_to_delete = S[i - 1]
	letter_to_add = S[i + n - 1]

	# print(S[i-1:i+n-1], count_non_comp)

	count_comp += modify(d_of_S, d_of_W, letter_to_delete, -1)
	count_comp += modify(d_of_S, d_of_W, letter_to_add, 1)

	if count_comp == len(d_of_W):
		count_ok += 1

print(count_ok)