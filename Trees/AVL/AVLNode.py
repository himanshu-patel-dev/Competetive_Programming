class AVL_TreeNode:
	""" AVL Node """
	def __init__(self,data):
		self.data 	= data
		self.bf 	= None		# balance factor
		self.right 	= None
		self.left 	= None

def AVL_node_bf(root,inorder=[]):
	""" traversal of AVL is to give root data with corresponding bf """
	if root is None:
		return
	AVL_node_bf(root.left, inorder)
	inorder.append( (root.data,root.bf) )
	AVL_node_bf(root.right, inorder)
	return inorder

def height(root):
	if root is None:
		return 0
	
	l = height(root.left)
	r = height(root.right)
	return 1 + max(l,r)

def calculate_bf(root):
	if root is None:
		return 0
	
	a = calculate_bf(root.left)
	b = calculate_bf(root.right)

	root.bf = abs(a-b)
	return root.bf + 1

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

	root = AVL_TreeNode(10)
	root.left = AVL_TreeNode(5)
	root.right = AVL_TreeNode(18)
	a = root.left
	b = root.right
	a.left = AVL_TreeNode(3)
	a.right = AVL_TreeNode(7)
	b.left = AVL_TreeNode(16)
	b.right = AVL_TreeNode(20)
	a.left.left = AVL_TreeNode(2)
	a.right.right = AVL_TreeNode(8)

	calculate_bf(root)
	print( AVL_node_bf(root) )
