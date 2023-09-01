class Node:
	def __init__(self, val):
		self.left_node = None
		self.right_node = None
		self.val = val


class Tree:
	def __init__(self):
		self.root = None
		self.length = 0

	def add(self, val):
		if self.root is None:
			self.root = Node(val)
			self.length = 1
			return 1
		else:
			curr = self.root
			curr_len = 1

			while True:
				curr_len += 1
				if curr.val == val:
					return -1
				if num > curr.val:

					if curr.right_node is None:
						curr.right_node = Node(val)
						break

					curr = curr.right_node
				else:
					if curr.left_node is None:
						curr.left_node = Node(val)
						break
					curr = curr.left_node

			self.length = max(curr_len, self.length)

			return curr_len

	def find_pre_max(self):
		curr_node = self.root
		prev_node = curr_node

		while curr_node.right_node is not None:
			prev_node = curr_node
			curr_node = curr_node.right_node

		if curr_node.left_node is not None:
			curr_node = curr_node.left_node
			while curr_node.right_node is not None:
				prev_node = curr_node
				curr_node = curr_node.right_node

			return curr_node.val

		return prev_node.val


arr = list(map(int, input().split()))[:-1]

tree = Tree()

for num in arr:
	ans = tree.add(num)
	# if ans != -1:
	# 	print(ans, end=' ')

## Maximum tree length
# print(tree.length)

print(tree.find_pre_max())