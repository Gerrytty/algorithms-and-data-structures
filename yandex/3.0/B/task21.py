if __name__ == "__main__":
    n = int(input())

    dp = []

    for i in range(n):
        if i == 0:
            dp.append(2)
        elif i == 1:
            dp.append(4)
        elif i == 2:
            dp.append(7)
        else:
            dp.append(sum([dp[-1], dp[-2], dp[-3]]))

    print(dp[-1])