def ok(a, b, c):
    if a + b < c:
        return False

    if a + c < b:
        return False

    if b + c < a:
        return False

    return True

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    if ok(a, b, c):
        print("YES")
    else:
        print("NO")

