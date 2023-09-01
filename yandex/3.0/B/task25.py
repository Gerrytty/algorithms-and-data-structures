if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 2:
        print(arr[1] - arr[0])
    else:

        arr.sort()

        dp = [0, arr[1] - arr[0], arr[2] - arr[0]]

        for i in range(3, n):
            a = min(dp[i - 1], dp[i-2]) + arr[i] - arr[i-1]
            dp.append(a)

        print(dp[-1])