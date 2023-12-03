n = int(input())

s = input()

possible = set()
impossible = set()
read_now = None
while s != "HELP":

	if s == "YES":
		if len(possible) == 0:
			possible = set(map(int, read_now))
		else:
			possible &= set(map(int, read_now))
	elif s == "NO":
		if len(possible) != 0:
			possible -= set(map(int, read_now))
		impossible |= set(map(int, read_now))
	else:
		read_now = s.split()

	s = input()


if len(possible) == 0:
	print(*(set(range(1, n+1)) - set(impossible)))
else:
	print(*sorted(list(possible)))