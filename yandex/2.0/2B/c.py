# s = input()

s= "cognitive"

palindrome_cost = 0

for i in range(len(s)//2):
	if s[i] != s[len(s)-1-i]:
		palindrome_cost += 1

print(palindrome_cost)