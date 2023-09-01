if __name__ == "__main__":
    brackets = input()

    print_incorrect = False
    balance = 0
    for ch in brackets:
        if ch == ")":
            balance -= 1
        if ch == "(":
            balance += 1
        if balance < 0:
            print("no")
            print_incorrect = True
            break

    if balance == 0:
        print("yes")
    elif not print_incorrect:
        print("no")