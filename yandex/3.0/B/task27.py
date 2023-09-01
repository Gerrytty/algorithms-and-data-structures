if __name__ == "__main__":
    n, m = map(int, input().split())

    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    full_sum = 0

    dp = []

    for i in range(n):
        dp.append([0 for j in range(m)])

    path = []

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = matrix[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    curr_i = n - 1
    curr_j = m - 1

    for i in range(0, n + m - 1):

        if curr_i > 0 and curr_j > 0:

            if dp[curr_i - 1][curr_j] >= dp[curr_i][curr_j - 1]:
                curr_i -= 1
                path.append("D")
            else:
                curr_j -= 1
                path.append("R")

        elif curr_i == 0:
            curr_j -= 1
            path.append("R")
        else:
            path.append("D")

    print(dp[-1][-1])
    print(*path[::-1][1:])