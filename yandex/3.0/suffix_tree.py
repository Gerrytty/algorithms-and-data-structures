class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.list_words = []

    def __repr__(self):
        return str(self.val)

class SuffixTree:
    def __init__(self):
        self.head = Node("root")

    # def add_letter(self, letter):
    #     current_node = self.head
    #     for child in self.head.children:


    def add_word(self, word, num_line):
        i = 0
        curr_node = self.head
        while i < len(word):

            find_child = False
            for child in curr_node.children:
                if child.val == word[i]:
                    find_child = True
                    curr_node = child
                    break

            if not find_child:
                new_node = Node(word[i])
                curr_node.children.append(new_node)
                curr_node = new_node

            curr_node.list_words.append(num_line)

            i += 1

    def find_prefix(self, prefix):
        curr_node = self.head

        i = 0
        in_words = []
        while i < len(prefix):
            find_child = False
            for child in curr_node.children:
                if child.val == prefix[i]:
                    find_child = True
                    curr_node = child
                    in_words.extend(curr_node.list_words)

            if not find_child:
                return []

            i += 1

        return curr_node.list_words


if __name__ == "__main__":
    s = SuffixTree()
    s.add_word("abc", 1)
    s.add_word("def", 2)
    s.add_word("abe", 3)
    s.add_word("abf", 4)
    s.add_word("aaf", 5)
    s.add_word("defender", 6)


    print(s.head.children)

    print(s.find_prefix("def"))

