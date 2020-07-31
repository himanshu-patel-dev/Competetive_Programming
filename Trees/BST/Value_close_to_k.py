class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def Closest_Value(root,k):
	""" return node data whichever is close to k """
	if root is None:
		return 0
	elif root.data == k:
		return root.data 
	elif root.data > k:
		if root.left is None:
			return root.data 
		# go left and search
		t = Closest_Value(root.left,k)
		if abs(t-k) < abs(root.data - k):
			return t
		else:
			return root.data
	else:
		if root.right is None:
			return root.data 
		# go right and search
		t = Closest_Value(root.right,k)
		if abs(t-k) < abs(root.data - k):
			return t
		else:
			return root.data


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

	print( Closest_Value(root,11) )
	print( Closest_Value(root,12) )
	print( Closest_Value(root,15) )