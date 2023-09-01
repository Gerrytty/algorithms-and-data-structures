def get_count(N, K, M):
    if N < M:
        return 0
    if K < M:
        return 0

    full_weight = N
    count_details = 0

    while full_weight >= K:

        n = full_weight // K
        m = K // M
        count_details += n*m
        full_weight -= n*m * M


    return count_details


if __name__ == "__main__":
    weight_of_alloy, weight_of_prepare_detail, weight_of_detail = map(int, input().split())

    print(get_count(weight_of_alloy, weight_of_prepare_detail, weight_of_detail))