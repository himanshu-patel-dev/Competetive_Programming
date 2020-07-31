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

def Prune_BST(root,a,b):
	""" remove all those nodes which are not in between a and b  """
	if root is None:
		return None
	
	root.left = Prune_BST(root.left,a,b)
	root.right = Prune_BST(root.right,a,b)

	if root.data < a:
		return root.right
	elif root.data > b:
		return root.left
	else:
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
	Prune_BST(root,5,18)
	print( InorderTraversal(root,[]) )
