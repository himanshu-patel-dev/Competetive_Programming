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

def remove_half_nodes(root):
	""" removes only those nodes which have one child (not leaf nodes) """
	if root is None:
		return None
	# apply post order traversal - after dealing with child when comes to parent
	# decide what to return based on no of children
	root.left = remove_half_nodes(root.left)
	root.right = remove_half_nodes(root.right)

	# return node if its a leaf
	if root.left is None and root.right is None:
		return root
	# return right child if current node have left child None
	if root.right is None:
		return root.left
	# return left child if current node have right child None
	if root.left is None:
		return root.right
	
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
	root = remove_half_nodes(root)
	print( InorderTraversal(root,[]) )
