if __name__ == "__main__":
    a, b, c, d = map(int, input().split())

    area1 = (a + c) * max([b, d])
    area2 = (b + d) * max([a, c])
    area3 = (a + d) * max([c, b])
    area4 = (b + c) * max([a, d])

    min_area = min([area1, area2, area3, area4])

    if min_area == area1:
        print(a+c, max(b, d))
    elif min_area == area2:
        print((b + d), max([a, c]))
    elif min_area == area3:
        print((a + d), max([c, b]))
    else:
        print((b + c), max([a, d]))