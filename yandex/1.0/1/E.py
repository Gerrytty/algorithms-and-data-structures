import math

if __name__ == "__main__":
    k1, m, k2, p2, n2 = map(int, input().split())

    num_rooms_in_level = math.ceil(k2 / n2)
    num_rooms_in_entrance = m * num_rooms_in_level
    p1 = math.ceil(k1 / num_rooms_in_entrance) # номер подъезда
    n2 = math.ceil((k1 - ((k1 // num_rooms_in_entrance) * num_rooms_in_entrance)) / num_rooms_in_level)

    if p2 == 1 and m == 1:
        p1 = 0
        n2 = 1

    # elif num_rooms_in_entrance * p2 > k2:
    #     p1, n2 = -1, -1

    print(p1, n2)