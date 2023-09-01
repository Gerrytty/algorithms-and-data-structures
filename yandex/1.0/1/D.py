if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    if c < 0:
        print("NO SOLUTION")
    elif a == 0 and c * c == b:
        print("MANY SOLUTIONS")
    elif a == 0:
        print("NO SOLUTION")
    else:

        if (c*c - b) % a == 0:
            print((c*c - b) // a)
        else:
            print("NO SOLUTION")
