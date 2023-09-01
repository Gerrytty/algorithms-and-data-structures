n = int(input())
times = input().strip().split()

minutes = []
for time in times:
    hh, mm = map(int, time.split(':'))
    minutes.append(hh * 60 + mm)

minutes.sort()

min_interval = minutes[0] - minutes[-1]

if min_interval < 0:
    min_interval += 24 * 60

for i in range(1, n):
    interval = minutes[i] - minutes[i-1]
    if interval < 0:
        min_interval += 24 *60
    if interval < min_interval:
        min_interval = interval

print(min_interval)