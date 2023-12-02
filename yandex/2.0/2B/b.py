arr = list(map(int, input().split()))

n = 10

max_distance_to_shop = -1

for i in range(n):
	if arr[i] == 1:
		closest_shop = float("inf")
		closest_shop_index = -1
		for j in range(n):
			if i != j and arr[j] == 2:
				closest_shop = min(closest_shop, abs(i-j))
		max_distance_to_shop = max(max_distance_to_shop, closest_shop)

print(max_distance_to_shop)