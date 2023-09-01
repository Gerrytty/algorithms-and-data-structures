if __name__ == "__main__":

    n = int(input())

    if n > 1:

        dp = [0, 0, 1, 1]
        ans = []

        for i in range(4, n+1):
            n1 = 1000000000000
            n2 = 1000000000000
            n3 = 1000000000000

            if i % 3 == 0:
                n1 = dp[i // 3] + 1

            if i % 2 == 0:
                n2 = dp[i // 2] + 1

            n3 = dp[-1] + 1
            min_n = min([n1, n2, n3])
            dp.append(min_n)

        print(dp[-1])

        ans = [n]

        i = len(dp) - 1

        while i > 1:
            n1 = 1000000000000
            n2 = 1000000000000
            n3 = 1000000000000

            if i % 3 == 0:
                n1 = dp[i // 3]

            if i % 2 == 0:
                n2 = dp[i // 2]

            n3 = dp[i - 1]
            min_n = min([n1, n2, n3])

            if min_n == n1:
                i //= 3
            elif min_n == n2:
                i //= 2
            else:
                i -= 1

            ans.append(i)

        print(*ans[::-1])
    else:
        print("0\n1")