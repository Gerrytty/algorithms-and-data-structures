def get_correct_bracket_sequence(s):

    stack = []

    open_brackets = ["(", "[", "{"]
    dict_of_brackets = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in open_brackets:
            stack.append(ch)
        elif len(stack) != 0:
            if stack.pop() != dict_of_brackets[ch]:
                return False
        else:
            return False

    if len(stack) == 0:
        return True

    return False

if __name__ == "__main__":
    s = input()

    if get_correct_bracket_sequence(s):
        print("yes")
    else:
        print("no")