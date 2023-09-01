if __name__ == "__main__":
    input_string = input()

    d = {}

    for i in range(len(input_string)):
        letter = input_string[i]
        if letter in d:
            d[letter] += (i+1) * (len(input_string) - i)
        else:
            d[letter] = (i+1) * (len(input_string) - i)

    keys = list(d.keys())
    keys.sort()

    for key in keys:
        print(f"{key}: {d[key]}")
