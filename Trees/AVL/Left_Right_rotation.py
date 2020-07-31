class AVL_TreeNode:
	""" AVL Node """
	def __init__(self,data):
		self.data 	= data
		self.bf 	= None		# balance factor
		self.right 	= None
		self.left 	= None

def PreOrder(root,order=[]):
	if root is None:
		return
	order.append( root.data )
	PreOrder(root.left, order)
	PreOrder(root.right, order)
	return order

def RightRotate(root):
	Make_root = root.left
	temp = Make_root.right

	# perform rotation
	Make_root.right = root
	root.left = temp

	# return the new root
	return Make_root

def LeftRotate(root):
	Make_root = root.right
	temp = Make_root.left

	# perform rotation
	Make_root.left = root
	root.right = temp

	# return the new root
	return Make_root


if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |			|
  2			8

	After right rotation of node 3
  			 root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
    2__		7	 16		 20
	   |	|	
	   3	8
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

	print( PreOrder(root,[]) )
	a.left = RightRotate( a.left )
	print( PreOrder(root,[]) )
