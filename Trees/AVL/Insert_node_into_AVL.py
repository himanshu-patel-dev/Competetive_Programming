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

def calculate_bf(root):
	""" calculate balancing factor for each node in AVL tree """
	if root is None:
		return 0
	
	a = calculate_bf(root.left)
	b = calculate_bf(root.right)

	root.bf = a-b
	return max(a,b) + 1

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

def insert_node(root,data):
	""" 
	root is the top most node of AVL tree and 
	data is what we want to put in tree 
	"""

	if root is None:
		return AVL_TreeNode(data)
	elif root.data > data:
		root.left = insert_node(root.left,data)
	else:
		root.right = insert_node(root.right,data)
	
	# update balancing factor for for current and children nodes
	calculate_bf(root)
	# make rotations to balance out the tree

	# case 1: LL 
	# root is left heavy (bf=2) and left child of root is also left heavy 
	if root.bf > 1 and root.left.data > data:
		return RightRotate(root)
	
	# case 2: RR
	# root is right heavy (bf=-2) and right child of root is also right heavy
	elif root.bf < -1 and root.right.data < data:
		return LeftRotate(root)

	# case 3: LR
	# root is left heavy (bf=2) but left child is right heavy
	elif root.bf > 1 and root.left.data < data:
		left_child = root.left_child
		# left rotation of child
		root.left = LeftRotate(left_child)
		# right rotate root
		return RightRotate(root)

	# case 4: RL
	# root is right heavy (bf=-2) but child is left heavy
	elif root.bf < -1 and root.right.data > data:
		right_child = root.right
		# right rotation of child
		root.right = RightRotate(right_child)
		# left rotate root
		return LeftRotate(root)

	return root


if __name__ == "__main__":
	"""
	      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |			|
  2			8
  |
  1 -- inserted

	         root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __2__		7	 16		 20
  |	   |	|
  1	   3	8

	"""

	root = AVL_TreeNode(10)
	lst = [5,18,3,7,16,20,2,8]	# order is important to cons the same tree

	# see after each insert how bf get modified and balanced
	# bf is not 2 or -2 when printing
	for ele in lst:
		insert_node(root,ele)
		print( AVL_node_bf(root,[]) )

	# insert a node to create a LL imbalance
	insert_node(root,1)
	print( AVL_node_bf(root,[]) )