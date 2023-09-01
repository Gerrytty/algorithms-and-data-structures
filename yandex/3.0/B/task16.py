class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return str(self.val)

class Queue:
    def __init__(self):
        self.head = None
        self.curr_node = None
        self.size = 0

    def push(self, val):
        if self.head is None:
            self.head = Node(val, None)
            self.curr_node = self.head
        else:
            new_node = Node(val, None)
            if self.curr_node is not None:
                self.curr_node.next = new_node
            self.curr_node = new_node

        self.size += 1

    def pop(self):
        if self.head is None:
            return None

        node_to_return = self.head
        self.head = self.head.next

        self.size -= 1

        return node_to_return.val

    def front(self):

        if self.head is None:
            return None

        return self.head.val

    def __len__(self):
        return self.size

    def clear(self):
        self.size = 0
        self.head = None
        self.curr_node = None


if __name__ == "__main__":
    q = Queue()

    curr_command = ""

    while True:
        curr_command = input().split()
        if curr_command[0] == "exit":
            print("bye")
            break

        if curr_command[0] == "push":
            q.push(int(curr_command[1]))
            print("ok")
        elif curr_command[0] == "pop":
            if len(q) != 0:
                print(q.pop())
            else:
                print("error")
        elif curr_command[0] == "front":
            if len(q) != 0:
                print(q.front())
            else:
                print("error")
        elif curr_command[0] == "clear":
            q.clear()
            print("ok")
        elif curr_command[0] == "size":
            print(len(q))