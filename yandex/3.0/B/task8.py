if __name__ == "__main__":
    n = int(input())

    tuples = []

    for i in range(n):
        tuples.append(tuple(map(int, input().split())))

    print(min(tuples, key=lambda x: x[0])[0], min(tuples, key=lambda x: x[1])[1], max(tuples, key=lambda x: x[0])[0], max(tuples, key=lambda x: x[1])[1])