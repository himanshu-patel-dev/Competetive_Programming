class AVL_TreeNode:
	""" AVL Node """
	def __init__(self,data):
		self.data 	= data
		self.bf 	= None		# balance factor
		self.right 	= None
		self.left 	= None

def calculate_bf(root):
	""" calculate balancing factor for each node in AVL tree """
	if root is None:
		return 0
	
	a = calculate_bf(root.left)
	b = calculate_bf(root.right)

	root.bf = a-b
	return max(a,b) + 1

def check_balance(root):
	""" 
	return true is tree is balanced (all nodes bf in -1 0 1) 
	(all nodes must have pre calculated bf value) 
	"""
	if root is None:
		return True

	l = check_balance(root.left)
	r = check_balance(root.right)
	m = True if root.bf in [-1,0,1] else False 

	return l and m and r

def isBST(root):
	""" return true if tree is bst """
	if root is None:
		return True
	if root.left and root.left.data >= root.data:
		return False
	if root.right and root.right.data <= root.data:
		return False
	
	l = isBST(root.left)
	r = isBST(root.right)
	if l and r:
		return True
	else:
		return False

def is_AVL(root):
	# check is tree a bst or not
	bst = isBST(root)
	# calculating bf for all nodes in tree
	calculate_bf(root)
	# checking if all bf are within range
	balanced = check_balance(root)

	return balanced and bst 


if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |			|
  2			8
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
	
	# check for AVL above tree
	print( is_AVL(root) )

	# make tree a non bst while height is same
	root.right.data = 12
	print( is_AVL(root) )
	# restore data back
	root.right.data = 18
	

	# after adding 1 to node 2
	a.left.left.left = AVL_TreeNode(1)
	print( is_AVL(root) )

