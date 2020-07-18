class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None


def insert_node(root,data):
	""" insert a node while traversing in level order traversal """
	node = Binary_Tree_Node(data)
	if root is None:
		return node
	
	from collections import deque
	q = deque()
	q.append(root)
	while len(q) > 0:
		n = q.popleft()
		if n.left:
			q.append(n.left)
		else:
			n.left = node
			return root
		if n.right:
			q.append(n.right)
		else:
			n.right = node
			return root


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	6		7
	"""
	root = Binary_Tree_Node(1)
	root.left = Binary_Tree_Node(2)
	root.right = Binary_Tree_Node(3)
	a = root.left
	b = root.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(6)
	b.right = Binary_Tree_Node(7)

	# insert_node(root,10)
	# print( root.left.left.left.data )

	for ele in [11,12,13]:
		root = insert_node(root,ele)
	print( root.left.left.left.data )
	print( root.left.left.right.data )
