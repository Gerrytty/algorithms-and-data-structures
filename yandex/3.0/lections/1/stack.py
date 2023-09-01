class Node:
    def __init__(self, val, prev_node):
        self.val = val
        self.prev_node = prev_node

    def __repr__(self):
        return str(self.val)

class Stack:
    def __init__(self):
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def push(self, val):
        if self.tail is None:
            self.tail = Node(val, None)
        else:
            new_node = Node(val, self.tail)
            self.tail = new_node

        self.len += 1

    def pop(self):
        if self.tail is None:
            return None
        node = self.tail
        self.tail = node.prev_node

        self.len -= 1

        return node

    def back(self):
        return self.tail.val

    def clear(self):
        self.tail = None

if __name__ == "__main__":

    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(len(stack))
    # print(stack.pop())