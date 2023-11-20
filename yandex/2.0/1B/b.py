n, from_station, to_station = map(int, input().split())

forward = abs(to_station - from_station)
backward1 = abs(n - from_station) + to_station
backward2 = abs(n - to_station + from_station)

print(min((forward, backward1, backward2)) - 1)