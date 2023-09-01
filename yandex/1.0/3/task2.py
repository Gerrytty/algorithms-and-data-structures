l1 = set(map(int, input().split()))
l2 = set(map(int, input().split()))

out = list(l1.intersection(l2))
out.sort()
print(*out)