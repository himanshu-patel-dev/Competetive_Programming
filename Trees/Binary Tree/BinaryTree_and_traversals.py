class Binary_Tree_Node:
	"""
	class for making a binary tree
	"""
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

def PreOrder(root,result):
	""" recursive T = O(n) S = O(n) """
	if root is None:
		return
	result.append( root.data )
	PreOrder(root.left, result)
	PreOrder(root.right, result)
	return result

def Inorder(root,result):
	""" recursive T = O(n) S = O(n)"""
	if root is None:
		return
	Inorder(root.left,result)
	result.append(root.data)
	Inorder(root.right,result)
	return result

def PostOrder(root,result):
	""" recursive T = O(n) S = O(n)"""
	if root is None:
		return
	PostOrder(root.left,result)
	PostOrder(root.right,result)
	result.append(root.data)
	return result

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

if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	6		7
	|
	100
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
	a.left.left = Binary_Tree_Node(100)

	print( PreOrder(root,[]) )
	print( Inorder(root,[]) )
	print( PostOrder(root,[]) )
	print( LevelOrder(root,[]) )
