def get_number(number):
    ok_number = ""

    for i, ch in enumerate(number):

        if i == 0 and ch == "7":
            return False

        if ord("0") <= ord(ch) <= ord("9"):
            if ch == "8":
                ok_number += "7"
            else:
                ok_number += ch

    if len(ok_number) == 7:
        return "7495" + ok_number

    return ok_number

if __name__ == "__main__":

    ok_number = ""

    with open("input.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                ok_number = get_number(line).replace(" ", "")
            else:
                if get_number(line) == ok_number:
                    print("YES")
                else:
                    print("NO")