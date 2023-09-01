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

    q.push(1)
    q.push(2)
    q.push(3)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
