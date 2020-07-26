class Binary_Tree_Node:
	"""
	class for making a binary tree
	"""
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

def LevelOrder(root,result):
	""" T = O(n) S = O(n) """
	if root is None:
		return

	from collections import deque
	q = deque()
	q.append(root)

	while len(q) != 0:
		node = q.popleft()
		result.append(node.data)
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	return result

def structurally_same(root1,root2):
	if (root1.left is None and root1.right is None) and\
		(root2.left is None and root2.right is None) and\
		root1.data == root2.data:
		return True
	
	if (root1.data != root2.data) or\
		(root1.left and root2.left is None) or\
		(root1.left is None and root2.left) or\
		(root1.right and root2.right is None) or\
		(root1.right is None and root2.right):
		return False

	left = structurally_same( root1.left, root2.left )
	right = structurally_same( root1.right, root2.right )
	return left and right

if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	6		7
	"""
	root1 = Binary_Tree_Node(1)
	root1.left = Binary_Tree_Node(2)
	root1.right = Binary_Tree_Node(3)
	a = root1.left
	b = root1.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(6)
	b.right = Binary_Tree_Node(7)
	print( LevelOrder(root1,[]) )

	root2 = Binary_Tree_Node(1)
	root2.left = Binary_Tree_Node(2)
	root2.right = Binary_Tree_Node(3)
	a = root2.left
	b = root2.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(6)
	b.right = Binary_Tree_Node(7)
	print( LevelOrder(root2,[]) )

	print( structurally_same(root1,root2) )	