if __name__ == "__main__":
    n, m, k = map(int, input().split())

    matrix = []
    for i in range(n):
        s = list(map(int, input().split()))
        prefix = 0
        arr = []
        for j in range(m):
            arr.append(prefix + s[j])
            prefix += s[j]
        matrix.append(arr)

    prefix_sum = [[0]*(n+1) for i in range(m+1)]
    for i in range(m):
        s = 0
        arr = []
        for j in range(n):
            s += matrix[j][i]
            prefix_sum[1+i][j+1] = s

    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        full_sum = prefix_sum[y2][x2]

        full_sum += prefix_sum[y1 - 1][x1 - 1]
        full_sum -= prefix_sum[y2][x1 - 1]
        full_sum -= prefix_sum[y1 - 1][x2]

        print(full_sum)