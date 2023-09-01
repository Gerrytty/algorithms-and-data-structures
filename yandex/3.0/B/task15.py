if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))

    ans = []

    for price in prices:
        ans.append([price, -1])

    stack = []

    for i, tup in enumerate(ans):
        if len(stack) == 0:
            stack.append(tup)
        else:
            last_elem_in_stack = stack[-1]
            while len(stack) > 0 and tup[0] < last_elem_in_stack[0]:
                elem = stack.pop()
                elem[1] = i
                if len(stack) != 0:
                    last_elem_in_stack = stack[-1]
            else:
                stack.append(tup)

    print(" ".join([str(a[1]) for a in ans]))