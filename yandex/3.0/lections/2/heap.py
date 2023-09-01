class Node:
    def __init__(self, val, left_child, right_child):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = None

    def __repr__(self):
        return f"{self.val}"

    def __lt__(self, other):
        return self.val < other.val

class NodeQ:
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
            self.head = NodeQ(val, None)
            self.curr_node = self.head
        else:
            new_node = NodeQ(val, None)
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

class Heap:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val, None, None)
        else:
            last_node = self.find_first_leaf()

            if last_node.left_child is None:
                last_node.left_child = Node(val, None, None)

                while last_node.left_child.val < last_node.val:
                    last_node.left_child.val, last_node.val = last_node.val, last_node.left_child.val

            elif last_node.right_child is None:
                last_node.right_child = Node(val, None, None)

                while last_node.right_child.val < last_node.val:
                    last_node.right_child.val, last_node.val = last_node.val, last_node.right_child.val

    def remove(self):
        left = self.head.left_child
        right = self.head.right_child

        min_node = min(left, right)
        max_node = min(left, right)

        


    def find_first_leaf(self):
        q = Queue()

        q.push(self.head)

        while len(q) != 0:
            node = q.pop()
            if node.left_child is not None and node.right_child is not None:
                q.push(node.left_child)
                q.push(node.right_child)
            else:
                return node

    def print(self, node):
        if node is not None:
            print(node.val)
            self.print(node.left_child)
            self.print(node.right_child)



if __name__ == "__main__":

    h = Heap()

    h.push(5)
    h.push(10)
    h.push(20)
    h.push(15)
    h.push(16)
    h.push(21)

    print(f"val = {h.find_first_leaf()}")