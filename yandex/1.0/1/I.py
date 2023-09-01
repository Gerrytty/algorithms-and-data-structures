if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    p = [a, b, c]
    p.sort()

    minx = p[0]
    miny = p[1]

    if d < e:
        mind = d
        mine = e
    else:
        mind = e
        mine = d

    ok = True

    if a == 0 or b == 0 or c == 0 or d == 0 or e == 0:
        print("NO")
        ok = False

    if ok:
        if minx > mind or miny > mine:
            print("NO")
        else:
            print("YES")