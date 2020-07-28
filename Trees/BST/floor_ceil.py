class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def floor(root,data):
	""" return floor (element smaller than or equal to data) if exist else inf"""
	if root is None:
		return float('inf')

	if root.data == data:
		return root.data
	elif root.data > data:
		return floor(root.left,data)
	else:
		r = floor(root.right,data)
		if r <= data:
			return r
		else:
			return root.data

def ceil(root,data):
	""" return ceil (element greater than or equal to data) if exist else -inf """
	if root is None:
		return float('-inf')
	
	if root.data == data:
		return data
	elif root.data < data:
		return ceil(root.right,data)
	else:
		l = ceil(root.left,data)
		if l >= data:
			return l
		else:
			return root.data

if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	root = BST_Tree_Node(10)
	root.left = BST_Tree_Node(5)
	root.right = BST_Tree_Node(18)
	a = root.left
	b = root.right
	a.left = BST_Tree_Node(3)
	a.right = BST_Tree_Node(7)
	b.left = BST_Tree_Node(16)
	b.right = BST_Tree_Node(20)
	a.left.left = BST_Tree_Node(2)

	print(floor(root,1))
	print(floor(root,4))
	print(floor(root,7))
	print(floor(root,15))
	print(floor(root,50))

	print('------------')

	print(ceil(root,1))
	print(ceil(root,4))
	print(ceil(root,7))
	print(ceil(root,15))
	print(ceil(root,50))