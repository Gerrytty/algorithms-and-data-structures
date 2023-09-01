if __name__ == "__main__":
    stop = "-2000000000"

    input_string = input()
    type_of_seq = "CONSTANT"
    current_num = int(input_string)
    count_constant = 0
    while input_string != stop:
        input_int = int(input_string)

        if type_of_seq == "CONSTANT" and input_int > current_num and count_constant < 2:
            type_of_seq = "ASCENDING"
        elif type_of_seq == "CONSTANT" and input_int > current_num:
            type_of_seq = "WEAKLY ASCENDING"
            count_constant += 1
        elif type_of_seq == "CONSTANT" and input_int < current_num and count_constant < 2:
            type_of_seq = "DESCENDING"
        elif type_of_seq == "CONSTANT" and input_int < current_num:
            type_of_seq = "WEAKLY DESCENDING"
            count_constant += 1
        elif type_of_seq == "ASCENDING" and input_int == current_num:
            count_constant += 1
            type_of_seq = "WEAKLY ASCENDING"
        elif type_of_seq == "DESCENDING" and input_int == current_num:
            count_constant += 1
            type_of_seq = "WEAKLY DESCENDING"
        elif type_of_seq == "ASCENDING" and input_int < current_num:
            type_of_seq = "RANDOM"
        elif type_of_seq == "DESCENDING" and input_int > current_num:
            type_of_seq = "RANDOM"
        elif type_of_seq == "WEAKLY DESCENDING" and input_int > current_num:
            type_of_seq = "RANDOM"
        elif type_of_seq == "WEAKLY ASCENDING" and input_int < current_num:
            type_of_seq = "RANDOM"

        if type_of_seq == "CONSTANT":
            count_constant += 1

        current_num = input_int

        input_string = input()

    print(type_of_seq)