def get_num(n, k, level, side):
    if k >= n:
        return None

    global_id = 2 * level + side - 1
    next_global_id = global_id + k

    next_lev = None
    next_site = None

    if next_global_id < n:

        next_level = next_global_id // 2 + 1
        next_side = next_global_id % 2 + 1

        next_lev = next_level
        next_site = next_side

    if global_id - k >= 0:
        next_global_id = global_id - k
        next_level = next_global_id // 2 + 1
        next_side = next_global_id % 2 + 1

        if next_site is not None and next_lev is not None and abs(level + 1 - next_level) >= abs(level + 1 - next_lev):
            return next_lev, next_site
        else:
            return next_level, next_side

    if next_lev is not None:
        return next_lev, next_site

    return None



if __name__ == "__main__":

    n = int(input())
    k = int(input())
    level = int(input())
    site = int(input())

    index_sit = get_num(n, k, level - 1, site)

    if index_sit is None:
        print(-1)
    else:
        print(*index_sit)