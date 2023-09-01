import math

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))

    first = 0
    last = n - 1

    for i in range(math.ceil(n/2)):
        mid = math.ceil((first + last) / 2)

        print(first, last)

        if arr[first] != arr[last]:
            last += 1

        first += 1

    print(first, last)