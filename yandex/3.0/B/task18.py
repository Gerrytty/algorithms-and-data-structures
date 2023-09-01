from collections import deque

if __name__ == "__main__":

    command = ""

    deq = deque()

    while True:
        command = input().split()

        if command[0] == "exit":
            print("bye")
            break

        if command[0] == "push_back":
            deq.append(command[1])
            print("ok")
        elif command[0] == "push_front":
            deq.appendleft(command[1])
            print("ok")
        elif command[0] == "pop_front":
            if len(deq) != 0:
                print(deq.popleft())
            else:
                print("error")
        elif command[0] == "pop_back":
            if len(deq) != 0:
                print(deq.pop())
            else:
                print("error")
        elif command[0] == "back":
            if len(deq) != 0:
                print(deq[-1])
            else:
                print("error")
        elif command[0] == "front":
            if len(deq) != 0:
                print(deq[0])
            else:
                print("error")
        elif command[0] == "size":
            print(len(deq))
        elif command[0] == "clear":
            deq.clear()
            print("ok")
