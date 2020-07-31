class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def InorderTraversal(root,inorder=[]):
	""" inorder traversal of BST is sorted bst data """
	if root is None:
		return
	InorderTraversal(root.left, inorder)
	inorder.append(root.data)
	InorderTraversal(root.right, inorder)
	return inorder

def remove_leaf_nodes(root):
	""" removes only leaf nodes """
	if root is None:
		return None

	# return None if its a leaf
	if root.left is None and root.right is None:
		return None
	else: 
		root.right = remove_leaf_nodes(root.right)
		root.left = remove_leaf_nodes(root.left)

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

	print( InorderTraversal(root,[]) )
	root = remove_leaf_nodes(root)
	print( InorderTraversal(root,[]) )
