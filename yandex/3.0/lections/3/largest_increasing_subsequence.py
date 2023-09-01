if __name__ == "__main__":
    sequence = [4, 10, 5, 12, 3, 24, 7]
    dp = []

    for i in range(len(sequence)):
        if i == 0:
            dp.append(1)
        else:
            max_dp = 0
            for j in range(i):
                if sequence[j] < sequence[i]:
                    if dp[j] > max_dp:
                        max_dp = dp[j]
            dp.append(max_dp + 1)

    print(dp)