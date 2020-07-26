class Binary_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None


if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____12___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	root = Binary_Tree_Node(10)
	root.left = Binary_Tree_Node(5)
	root.right = Binary_Tree_Node(12)
	a = root.left
	b = root.right
	a.left = Binary_Tree_Node(3)
	a.right = Binary_Tree_Node(7)
	b.left = Binary_Tree_Node(16)
	b.right = Binary_Tree_Node(20)
	a.left.left = Binary_Tree_Node(2)

	