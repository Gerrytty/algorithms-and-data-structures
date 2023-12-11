n, m = map(int, input().split())
groups = list(map(int, input().split())) # n students in group
groups = list(zip(groups, range(n)))
groups.sort(key=lambda x: x[0])

class_rooms = list(map(int, input().split())) # k computers in room
class_rooms = list(zip(class_rooms, range(m)))
class_rooms.sort(key=lambda x: x[0])

left = 0
right = 0
ans = [0 for i in range(n)]
while left < n and right < m:
	if groups[left][0] + 1 <= class_rooms[right][0]:
		ans[groups[left][1]] = class_rooms[right][1] + 1
		left += 1
	right += 1

print(left)
print(*ans)