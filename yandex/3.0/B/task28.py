if __name__ == "__main__":
    n, m = map(int, input().split())

    if n == 1 and m == 1:
        print("1")
    elif n < 2 or m < 2:
        print("0")
    else:
        board = []
        for i in range(n):
            board.append([0 for _ in range(m)])

        board[0][0] = 1

        for i in range(0, n):
            for j in range(m):
                if board[i][j] > 0:
                    if j < m - 2 and i < n-1:
                        board[i+1][j+2] += board[i][j]
                    if i < n - 2 and j < m-1:
                        board[i+2][j+1] += board[i][j]

        print(board[-1][-1])