if __name__ == "__main__":
    n = int(input())
    train = list(map(int, input().split()))

    stack = []

    ans = []

    curr_start = 1

    for curr_pos in range(len(train)):

        if train[curr_pos] == curr_start:
            ans.append(curr_start)
            curr_start += 1
            curr_pos += 1
            continue

        if len(stack) == 0:
            stack.append(train[curr_pos])
        else:
            prev_stack = stack[-1]
            while len(ans) != 0 and prev_stack - ans[-1] == 1:
                ans.append(stack.pop())
                if len(stack) != 0:
                    prev_stack = stack[-1]
            curr_val = train[curr_pos]
            stack.append(curr_val)


    while len(stack) != 0:
        prev_stack = stack[-1]
        if prev_stack - ans[-1] == 1:
            ans.append(stack.pop())
        else:
            break

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")