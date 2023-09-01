if __name__ == "__main__":
    input_list = list(map(int, input().split()))

    increase = True

    for i in range(len(input_list) - 1):
        if input_list[i] >= input_list[i + 1]:
            increase = False
            break

    if len(input_list) == 0:
        print("NO")
    elif increase:
        print("YES")
    else:
        print("NO")