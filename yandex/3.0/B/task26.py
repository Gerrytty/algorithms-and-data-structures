if __name__ == "__main__":
    n, m = map(int, input().split())

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    full_sum = 0

    dp = []

    for i in range(n):
        dp.append([0 for j in range(m)])

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = matrix[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    print(dp[-1][-1])