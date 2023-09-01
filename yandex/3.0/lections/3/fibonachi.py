def get_fibonachi(n):
    arr = []

    for i in range(n):
        if i == 0:
            arr.append(1)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i - 1] + arr[i - 2])

    return arr[-1]

if __name__ == "__main__":
    print(get_fibonachi(8))