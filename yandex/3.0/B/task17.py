from task16 import Queue

if __name__ == "__main__":

    cards1 = list(map(int, input().split()))
    cards2 = list(map(int, input().split()))

    q1 = Queue()
    q2 = Queue()

    for i in range(5):
        q1.push(cards1[i])
        q2.push(cards2[i])

    count = 0

    while len(q1) != 0 and len(q2) != 0:

        current_card_1 = q1.pop()
        current_card_2 = q2.pop()

        tmp_current_card_1 = current_card_1
        tmp_current_card_2 = current_card_2

        if current_card_1 == 0 and current_card_2 == 9:
            tmp_current_card_1 = 10
        if current_card_2 == 0 and current_card_1 == 9:
            tmp_current_card_2 = 10

        if tmp_current_card_1 > tmp_current_card_2:
            q1.push(current_card_1)
            q1.push(current_card_2)
        else:
            q2.push(current_card_1)
            q2.push(current_card_2)

        count += 1

    if len(q1) == 0:
        print("second", count)
    else:
        print("first", count)