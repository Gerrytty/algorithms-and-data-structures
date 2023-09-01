def find_less_nearest_on_right(arr):
    ans = []

    for i, num in enumerate(arr):
        # num | ans
        ans.append([num, len(arr)])

    return find(ans)

def find_less_nearest_on_left(arr):
    ans = []

    for i, num in enumerate(arr):
        ans.append([arr[len(arr) - i - 1], len(arr)])

    return find(ans, True)

def find(ans_arr, reverse=False):

    stack = []

    for i, tup in enumerate(ans_arr):
        if len(stack) == 0:
            stack.append(tup)
        else:
            last_elem_in_stack = stack[-1]
            if tup[0] >= last_elem_in_stack[0]:
                stack.append(tup)
            else:
                while tup[0] < last_elem_in_stack[0] and len(stack) != 0:
                    stack_elem = stack.pop()
                    if reverse:
                        stack_elem[1] = len(arr) - i - 1
                    else:
                        stack_elem[1] = i
                    if len(stack) != 0:
                        last_elem_in_stack = stack[-1]

    return ans_arr

if __name__ == "__main__":
    arr = [2, 4, 1, 3]

    print(find_less_nearest_on_right(arr))
    print(find_less_nearest_on_left(arr))