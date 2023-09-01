if __name__ == "__main__":
    n = int(input())

    table = []

    for i in range(n):
        table.append(list(map(int, input().split())))

    dp = []

    for i in range(n):
        if i == 0:
            dp.append(table[0][0])
        elif i == 1:
            dp.append(min([table[0][0] + table[1][0], table[0][1]]))
        elif i == 2:
            dp.append(min(
                [table[0][0] + table[1][0] + table[2][0],
                 table[0][1] + table[2][0],
                 table[0][0] + table[1][1],
                 table[0][2]
                 ]
            ))
        else:
            dp.append(min(
                dp[i - 1] + table[i][0],
                dp[i - 2] + table[i - 1][1],
                dp[i - 3] + table[i - 2][2]
            ))

    print(dp[-1])