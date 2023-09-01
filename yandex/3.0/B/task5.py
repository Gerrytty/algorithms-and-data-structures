if __name__ == "__main__":
    ans = 0

    n = int(input())

    prev = int(input())
    for i in range(n-1):
        curr = int(input())
        ans += min(prev, curr)
        prev = curr

    print(ans)