class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def kth_smallest_element(root,k,count=[0]):
	""" returns k th smallest element in BST otherwise None """
	if root is None:
		return None
	
	l = kth_smallest_element(root.left,k,count)
	if l:
		return l
	
	count[0] += 1
	if count[0] == k:
		return root.data
	
	r = kth_smallest_element(root.right,k,count)
	if r:
		return r
	
	return None

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

	print( kth_smallest_element(root,3) )