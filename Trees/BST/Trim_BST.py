class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def sort_BST(root,inorder=[]):
	if root is None:
		return
	sort_BST(root.left, inorder)
	inorder.append(root.data)
	sort_BST(root.right, inorder)
	return inorder

def trim_tree(root,mini,maxi):
	if root is None:
		return None

	root.left = trim_tree(root.left,mini,maxi)
	root.right = trim_tree(root.right,mini,maxi)
	
	if mini <= root.data <= maxi:
		return root
	elif root.data < mini:
		return root.right
	else:
		return root.left


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

	root = trim_tree(root,6,19)
	print( sort_BST(root) )