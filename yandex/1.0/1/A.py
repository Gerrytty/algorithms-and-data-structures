if __name__ == "__main__":
    t_room, t_cond = map(int, input().split())
    p = input()

    if p == "freeze":
        if t_cond > t_room:
            print(t_room)
        else:
            print(t_cond)

    elif p == "heat":
        if t_cond < t_room:
            print(t_room)
        else:
            print(t_cond)

    elif p == "auto":
        print(t_cond)
    else:
        print(t_room)