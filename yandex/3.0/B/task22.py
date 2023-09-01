def get_num_vars(n, k):
    arr = []

    for i in range(n):
        if i < k:
            if i == 0:
                arr.append(1)
            else:
                arr.append(sum(arr) + 1)
        else:
            ans = 0
            for j in range(k):
                ans += arr[i - j - 1]
            arr.append(ans)
    return arr


if __name__ == "__main__":
    n, k = map(int, input().split())

    print(get_num_vars(n, k)[n - 2])

