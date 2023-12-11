s = input()

# ( ( ( ) ) )

def check(s):
	s = list(s)
	visited = [False for _ in range(len(s))]
	left = 0
	right = 0

	while left < len(s):
		if visited[left]:
			left += 1
			continue

		if s[left] == ")"and not visited[left]:
			return False

		finded = False
		while right < len(s):
			if s[right] == ")":
				finded = True
				visited[right] = True
				break
			right += 1

		if not finded:
			return False

		left += 1
		right += 1

	return True

if check(s):
	print("YES")
else:
	print("NO")