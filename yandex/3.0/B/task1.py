def transpose(matrix):
    result = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

import sys
if __name__ == "__main__":

    s = ""

    with open("input.txt") as f:
        for line in f:
            s += line

    d = {}
    for ch in s:

        if ch == " " or ch == "\n":
            continue

        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1

    d_list = sorted(d, key=lambda x: ord(x))

    max_val = max(d, key=d.get)


    output = []

    for ch in d_list:
        list_to_append = ["#" for _ in range(d[ch])] + [" " for _ in range((d[max_val] - d[ch]))]
        output.append(list_to_append)

    output = transpose(output)

    for i in range(len(output)):
        s = ""
        l = output[len(output) - 1 - i]
        for j in range(len(l)):
            s += l[j]
        print(s)

    print("".join(d_list))