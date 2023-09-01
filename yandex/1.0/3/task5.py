arr = set(input().split())

number = input()

number_set = set()

for letter in number:
	number_set.add(letter)

print(len(number_set - arr))