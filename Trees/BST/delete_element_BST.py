class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def InorderSuccessor(root,parent):
	while root.left:
		parent,root = root,root.left
	return (parent,root)

def delete_node(root,data):
	if root.data == data:
		if root.left and root.right:
			parent_IS, IS = InorderSuccessor(root.right,root)
			# IS is the last member is left most branch its right is either null or some element
			if parent_IS is not root:
				parent_IS.left = IS.right
			else:
				parent_IS.right = IS.right
			# replacing root's data by the inorder successor
			root.data = IS.data		# or IS.left = root.left and IS.right = root.right
			return root
		elif root.left:
			return root.left
		else: # root.right or both None
			return root.right
	elif root.data > data:
		if root.left:
			root.left = delete_node(root.left,data)		
	else:	# root.data < data
		if root.right:
			root.right = delete_node(root.right,data)
	return root


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

	from sort_BST import sort_BST
	root = delete_node(root,18)
	print( sort_BST(root,[]) )
