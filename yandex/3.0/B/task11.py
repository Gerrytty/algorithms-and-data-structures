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

        return node.val

    def back(self):
        return self.tail.val

    def clear(self):
        self.tail = None
        self.len = 0

if __name__ == "__main__":

    stack = Stack()

    with open("input.txt") as file:
        for line in file:
            s = line.split()

            if s[0] == "push":
                stack.push(int(s[1]))
                print("ok")
            elif s[0] == "back":
                if len(stack) != 0:
                    print(stack.back())
                else:
                    print("error")
            elif s[0] == "size":
                print(len(stack))
            elif s[0] == "exit":
                print("bye")
                break
            elif s[0] == "clear":
                stack.clear()
                print("ok")
            elif s[0] == "pop":
                if len(stack) != 0:
                    print(stack.pop())
                else:
                    print("error")