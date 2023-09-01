if __name__ == "__main__":
    n = int(input())
    input_list = list(map(int, input().split()))
    num = int(input())

    min_diff = abs(input_list[0] - num)
    guess_num = input_list[0]

    for a in input_list:
        if abs(a - num) < min_diff:
            min_diff = abs(a - num)
            guess_num = a

    print(guess_num)