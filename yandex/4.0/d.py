a = input()
b = input()

if len(a) != len(b):
	print("NO")
else:
	ad = {}
	bd = {}

	for letter in a:
		if letter in ad:
			ad[letter] += 1
		else:
			ad[letter] = 1

	for letter in b:
		if letter in bd:
			bd[letter] += 1
		else:
			bd[letter] = 1

	if ad == bd:
		print("YES")
	else:
		print("NO")