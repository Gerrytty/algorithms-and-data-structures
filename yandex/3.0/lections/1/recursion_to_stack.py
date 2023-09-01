def get_recursive_factorial(n):
    if n == 1: return 1 # 0
    prev_factorial = get_recursive_factorial(n - 1) # 1
    return n * prev_factorial

def factorial(n):
    stack = []

    returned_val = 1

    stack.append({"n": n, "prev_factorial":"?", "goto":0})

    while len(stack) > 0:
        top_stack = stack[-1]
        goto = top_stack["goto"]

        # prev_factorial state (another call function)
        if goto == 0:
            if top_stack["n"] == 1:
                returned_val = 1
                stack.pop()
            else:
                top_stack["goto"] = 1
                stack.append({"n": top_stack["n"] - 1, "prev_factorial":"?", "goto":0})
        else:
            top_stack["prev_factorial"] = returned_val
            returned_val = top_stack["prev_factorial"] * top_stack["n"]
            stack.pop()


    return returned_val


if __name__ == "__main__":

    print(factorial(5))