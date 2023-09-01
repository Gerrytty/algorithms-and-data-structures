if __name__ == "__main__":
    A_h, A_m, A_s = map(int, input().split(":"))
    A = A_h * 3600 + A_m * 60 + A_s
    B_h, B_m, B_s = map(int, input().split(":"))
    B = B_h * 3600 + B_m * 60 + B_s
    C_h, C_m, C_s = map(int, input().split(":"))
    C = C_h * 3600 + C_m * 60 + C_s

    if C_h < A_h:
        C += 24 * 3600

    delay = (C - A) // 2
    if (C - A) % 2 != 0:
        delay += 1

    time = B + delay

    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60

    hours_s = int(hours)
    if hours_s >= 24:
        new_hours = str(int(int(hours_s) % 24))
        if len(new_hours) < 2:
            hours_s = "0" + new_hours
        else:
            hours_s = new_hours
    else:
        hours_s = str(hours_s)
    if len(hours_s) < 2:
        hours_s = "0" + hours_s
    minutes_s = str(int(minutes))
    if len(minutes_s) < 2:
        minutes_s = "0" + minutes_s
    seconds_s = str(int(seconds))
    if len(seconds_s) < 2:
        seconds_s = "0" + seconds_s
    print(f"{hours_s}:{minutes_s}:{seconds_s}")
