a, aa, b, bb = map(int, input().split())

def gcd(a, b):
	if a == 0:
		return b
	if b == 0:
		return a
	if a > b:
		return gcd(a%b, b)
	else:
		return(gcd(a, b%a))

z = aa*bb
s = (z // aa) * a + (z // bb) * b
gc = gcd(z, s)
print(s // gc, z // gc)