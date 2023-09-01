priors = {"+":1, "-":1, "*":2, "/":2}


def to_postfix(s):

    ans = []

    stack = []

    for ch in s:
        if ch not in priors and ch != " " and ch != "(" and ch != ")":
            ans.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            last_ch = stack[-1]
            while last_ch != "(":
                ans.append(last_ch)
                stack.pop()
                last_ch = stack[-1]
            stack.pop()
        else:
            if len(stack) != 0:
                last_ch = stack[-1]
                if last_ch != "(":
                    while priors[last_ch] >= priors[ch]:
                        ans.append(last_ch)
                        stack.pop()
                        if len(stack) == 0:
                            break
                        last_ch = stack[-1]
                stack.append(ch)
            else:
                stack.append(ch)

    while len(stack) != 0:
        ans.append(stack.pop())

    return ans

def calc(postfix):

    stack = []

    for p in postfix:
        if p not in priors:
            stack.append(int(p))
        else:

            if len(stack) != 0:
                x1 = stack.pop()
                x2 = stack.pop()

                if p == "+":
                    stack.append(x1 + x2)
                elif p == "-":
                    stack.append(x2 - x1)
                elif p == "/":
                    stack.append(x2 / x1)
                else:
                    stack.append(x1 * x2)

    return stack[0]


if __name__ == "__main__":
    # s = input().split() # 8 9 + 1 7 - *
    # print(calc(s)[0])

    prefix_expression = "6+3*(1+4*5)*2"
    postfix = to_postfix(prefix_expression)

    print(postfix)
    print(calc(postfix))
