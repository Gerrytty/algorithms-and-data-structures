n, m = map(int, input().split())

ann = []

for i in range(n):
	ann.append(int(input()))

ann = set(ann)

boris = []

for i in range(m):
	boris.append(int(input()))

boris = set(boris)

common = ann.intersection(boris)
common = list(common)
common.sort()

print(len(common))
print(*common)

only_ann = ann - boris
only_ann = list(only_ann)
only_ann.sort()
print(len(only_ann))
print(*only_ann)

only_boris = boris - ann
only_boris = list(only_boris)
only_boris.sort()
print(len(only_boris))
print(*only_boris)