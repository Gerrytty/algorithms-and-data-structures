class Participant:
    def __init__(self, name, val, ids):
        self.name = name
        self.val = val
        self.ids = ids

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return f"{self.name}: {self.val}"

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    parts = []
    vinner_balls = max(arr)
    winner_indx = -1

    for i in range(len(arr)):
        if arr[i] == vinner_balls:
            winner_indx = i
            break

    for i in range(1, len(arr) - 1):
        a = arr[i]

        if str(a)[-1] == "5" and a > arr[i + 1]:
            parts.append(Participant("Vasya", a, i))
        else:
            parts.append(Participant("FN", a, i))

    parts.append(Participant("FN", arr[0], 0))
    parts.append(Participant("FN", arr[-1], len(arr) - 1))
    parts.sort(reverse=True)

    find = False

    for i, part in enumerate(parts):
        if part.name == "Vasya" and part.ids > winner_indx:
            val = part.val
            curr = i + 1
            i_back = 1
            while i - i_back > 0 and val == parts[i - i_back].val:
                curr -= 1
                i_back += 1
            print(curr)
            find = True
            break

    if not find:
        print(0)
