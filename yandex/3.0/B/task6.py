if __name__ == "__main__":
    m = int(input())
    n = int(input())

    not_cross_segments = []
    for i in range(n):
        segment_start, segment_end = map(int, input().split())

        if i == 0:
            not_cross_segments.append((segment_start, segment_end))
        else:
            to_remove = []
            for j in range(len(not_cross_segments)):

                if (not_cross_segments[j][0] <= segment_end <= not_cross_segments[j][1]) or (
                        not_cross_segments[j][0] <= segment_start <= not_cross_segments[j][1]) or (
                    segment_start <= not_cross_segments[j][0] and segment_end >= not_cross_segments[j][1]
                ):

                    to_remove.append(not_cross_segments[j])

            # print(to_remove)

            # print(to_remove, (segment_start, segment_end))
            for j in range(len(to_remove)):
                not_cross_segments.remove(to_remove[j])

            not_cross_segments.append((segment_start, segment_end))

            # print(not_cross_segments)

    print(len(not_cross_segments))
