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

def PreOrder(root,order=[]):
	if root is None:
		return
	order.append( root.data )
	PreOrder(root.left, order)
	PreOrder(root.right, order)
	return order

def calculate_bf(root):
	""" calculate balancing factor for each node in AVL tree """
	if root is None:
		return 0
	
	a = calculate_bf(root.left)
	b = calculate_bf(root.right)

	root.bf = a-b
	return max(a,b) + 1


def min_AVL(h,count=[0]):
	if h <= 0:
		return None
	
	left = min_AVL(h-1,count)
	count[0] += 1
	root = AVL_TreeNode(count[0])
	right = min_AVL(h-2,count)

	root.right = right
	root.left = left
	return root

if __name__ == "__main__":
	"""      root
		_____ 3______
		|			 |
	____2	 	 	 4
	|			 
	1
	"""

	root = min_AVL(3,[0])
	calculate_bf(root)
	print( AVL_node_bf(root,[]) )
	print( PreOrder(root,[]) )


	"""      		  root
			  __________5_________
			  |					  |
		_____ 3______		  ____7
		|			 |		  |
	____2	 	 	 4		  6
	|			 
	1
	"""
	root = min_AVL(4,[0])
	calculate_bf(root)
	print( AVL_node_bf(root,[]) )
	print( PreOrder(root,[]) )

