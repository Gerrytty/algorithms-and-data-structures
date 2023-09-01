if __name__ == "__main__":
    input_list = list(map(int, input().split()))

    num_ok_nums = 0

    for i in range(1, len(input_list) - 1):
        if input_list[i] > input_list[i - 1] and input_list[i] > input_list[i + 1]:
            num_ok_nums += 1

    print(num_ok_nums)