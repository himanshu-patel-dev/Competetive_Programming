class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def insert_node(root,data):
	if root is None or root.data == data:
		root = BST_Tree_Node(data)
		return root

	if root.data > data:
		if root.left is None:
			root.left = BST_Tree_Node(data)
			return root.left
		else:
			return insert_node(root.left,data)
	else:
		if root.right is None:
			root.right = BST_Tree_Node(data)
			return root.right
		else:
			return insert_node(root.right,data)


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
	root.right = BST_Tree_Node(12)
	a = root.left
	b = root.right
	a.left = BST_Tree_Node(3)
	a.right = BST_Tree_Node(7)
	b.left = BST_Tree_Node(16)
	b.right = BST_Tree_Node(20)
	a.left.left = BST_Tree_Node(2)

	from sort_BST import sort_BST
	print( insert_node(root,100).data )
	print( sort_BST(root,[]) )
